"""Deterministic checks for wood wallpaper Listing drafts.

The script checks format and declared requirements. Product facts, keyword
relevance, competitor attribution, semantic similarity, and structural
similarity still require model review.
"""

import argparse
import json
import re
from datetime import date
from pathlib import Path

RANGES = {
    "title": (70, 75),
    "highlights": (120, 125),
    "keywords": (240, 249),
    "description": (1800, 2000),
}
TITLE_FORBIDDEN = [
    "vinyl", "self adhesive", "removable", "waterproof", "thicken", "seamless",
]
DEFAULT_HIGHLIGHT_TERMS = ["self adhesive", "removable", "waterproof"]
DEFAULT_COVERED_TERMS = ["self adhesive", "removable", "waterproof"]
TITLE_SMALL_WORDS = {
    "and", "as", "at", "by", "for", "from", "in", "into", "of", "on",
    "to", "with", "over", "under", "through", "within", "without",
}


def parse_pairs(values):
    result = {}
    for item in values:
        if "=" not in item:
            raise ValueError(f"Expected FIELD=TEXT, got: {item}")
        key, value = item.split("=", 1)
        result[key.strip()] = value
    return result


def terms_from_reference(path: Path):
    terms = []
    for line in path.read_text(encoding="utf-8-sig").splitlines():
        if line.startswith("| ") and not line.startswith("| 原始") and not line.startswith("|---"):
            term = line.split("|", 2)[1].strip()
            if term:
                terms.append(term)
    return terms


def words(text):
    return re.findall(r"[A-Za-z0-9]+(?:['’-][A-Za-z0-9]+)*", text.lower())


def scan(text, terms):
    findings = []
    for term in terms:
        pattern = r"(?<![A-Za-z0-9])" + re.escape(term).replace(r"\ ", r"[\s-]+") + r"(?![A-Za-z0-9])"
        for match in re.finditer(pattern, text, re.IGNORECASE):
            findings.append({
                "term": term,
                "start": match.start(),
                "context": text[max(0, match.start() - 35):match.end() + 35],
            })
    return findings


def similarity(a, b):
    wa, wb = words(a), words(b)
    if not wa or not wb:
        return 0.0
    sa = set(zip(wa, wa[1:]))
    sb = set(zip(wb, wb[1:]))
    return round(len(sa & sb) / max(1, len(sa | sb)) * 100, 2)


def title_case_violations(text, ignore_terms=()):
    ignored = {word for term in ignore_terms for word in words(term)}
    violations = []
    for match in re.finditer(r"\b[A-Za-z][A-Za-z0-9'’-]*\b", text):
        word = match.group(0)
        lower = word.lower()
        if lower in TITLE_SMALL_WORDS or lower in ignored:
            continue
        if word[0].islower():
            violations.append(word)
    return sorted(set(violations))


def find_size(text):
    return re.findall(r"\b\d+(?:\.\d+)?\s*[×x]\s*\d+(?:\.\d+)?\s*in\b", text, re.IGNORECASE)


def check_range(result, field, text):
    minimum, maximum = RANGES[field]
    count = len(text)
    passed = minimum <= count <= maximum
    result["checks"][f"{field}_characters"] = {
        "count": count,
        "required_range": [minimum, maximum],
        "pass": passed,
    }
    result["pass"] &= passed


def add_check(result, name, details, passed):
    details = dict(details)
    details["pass"] = bool(passed)
    result["checks"][name] = details
    result["pass"] &= bool(passed)


def main():
    parser = argparse.ArgumentParser(description="Check wood wallpaper Listing format, claims, and history overlap.")
    parser.add_argument("--field", action="append", default=[], help="FIELD=TEXT; repeat for title, highlights, keywords, description, bullet1...")
    parser.add_argument("--compare", action="append", default=[], help="FIELD=OLD_TEXT; repeat for field-level overlap")
    parser.add_argument("--terms", type=Path, default=Path(__file__).parents[1] / "references" / "prohibited-terms.md")
    parser.add_argument("--brand", help="Expected title-leading brand")
    parser.add_argument("--size", help="Expected primary size, e.g. 17.3×78.7in")
    parser.add_argument("--required-highlight-term", action="append", dest="highlight_terms", default=None)
    parser.add_argument("--covered-term", action="append", default=None, help="Selling-point phrase already covered in title/highlights")
    parser.add_argument("--description-term", action="append", default=[], help="Term that description must contain")
    parser.add_argument("--title-exclude", action="append", default=[], help="Additional title phrase that must not appear")
    parser.add_argument("--save-history", type=Path, help="Directory for confirmed JSON history records")
    parser.add_argument("--confirmed", action="store_true", help="Required before --save-history can write")
    parser.add_argument("--sku")
    parser.add_argument("--marketplace", default="Amazon-US")
    parser.add_argument("--product-type")
    parser.add_argument("--version", default="v1")
    parser.add_argument("--source-listing-id")
    parser.add_argument("--change-notes", default="")
    args = parser.parse_args()

    try:
        fields = parse_pairs(args.field)
        old = parse_pairs(args.compare)
    except ValueError as exc:
        parser.error(str(exc))

    banned = terms_from_reference(args.terms)
    result = {"checks": {}, "overlap_percent": {}, "pass": True, "saved_history": None}

    for name, _limits in RANGES.items():
        if name in fields:
            check_range(result, name, fields[name])

    title = fields.get("title")
    if title is not None:
        if args.brand:
            add_check(result, "title_brand_first", {"brand": args.brand}, title.lower().startswith(args.brand.lower()))
        forbidden_hits = scan(title, TITLE_FORBIDDEN + args.title_exclude)
        add_check(result, "title_forbidden_terms", {"findings": forbidden_hits}, not forbidden_hits)
        size_matches = find_size(title)
        size_ok = bool(size_matches)
        if args.size:
            normalized = re.sub(r"\s+", "", args.size.lower()).replace("x", "×")
            size_ok = normalized in {re.sub(r"\s+", "", item.lower()).replace("x", "×") for item in size_matches}
        add_check(result, "title_size_format", {"expected": args.size, "matches": size_matches}, size_ok)
        repeats = sorted({word for word in words(title) if words(title).count(word) > 2})
        add_check(result, "title_repeated_words", {"words": repeats}, not repeats)
        add_check(result, "title_case", {"violations": title_case_violations(title, [args.brand] if args.brand else ())}, not title_case_violations(title, [args.brand] if args.brand else ()))

    highlights = fields.get("highlights")
    if highlights is not None:
        required = args.highlight_terms if args.highlight_terms is not None else DEFAULT_HIGHLIGHT_TERMS
        missing = [term for term in required if not re.search(re.escape(term), highlights, re.IGNORECASE)]
        add_check(result, "highlight_required_terms", {"required": required, "missing": missing}, not missing)
        add_check(result, "highlight_case", {"violations": title_case_violations(highlights)}, not title_case_violations(highlights))

    keywords = fields.get("keywords")
    if keywords is not None:
        byte_count = len(keywords.encode("utf-8"))
        keyword_words = words(keywords)
        duplicate_terms = sorted({word for word in keyword_words if keyword_words.count(word) > 1 and word != "wood"})
        add_check(result, "keywords_bytes", {"count": byte_count, "required_range": [240, 249]}, 240 <= byte_count <= 249)
        add_check(result, "keywords_lowercase", {}, keywords == keywords.lower())
        add_check(result, "keywords_punctuation", {"findings": re.findall(r"[^a-z0-9\s]", keywords)}, not re.search(r"[^a-z0-9\s]", keywords))
        add_check(result, "keywords_duplicate_words", {"words": duplicate_terms}, not duplicate_terms)
        covered = args.covered_term if args.covered_term is not None else DEFAULT_COVERED_TERMS
        covered_hits = scan(keywords, covered)
        add_check(result, "keywords_repeated_selling_points", {"covered_terms": covered, "findings": covered_hits}, not covered_hits)

    bullets = sorted((name, text) for name, text in fields.items() if re.fullmatch(r"bullet[1-8]", name))
    if bullets:
        count_ok = 5 <= len(bullets) <= 8
        add_check(result, "bullet_count", {"count": len(bullets), "required_range": [5, 8]}, count_ok)
        lengths = {name: len(text) for name, text in bullets}
        length_issues = {name: value for name, value in lengths.items() if not 160 <= value <= 240}
        add_check(result, "bullet_lengths", {"counts": lengths, "target_range": [160, 240]}, not length_issues)
        if "bullet1" in fields:
            size_ok = bool(find_size(fields["bullet1"])) and (not args.size or args.size.lower().replace("x", "×") in fields["bullet1"].lower().replace("x", "×"))
            add_check(result, "bullet1_size", {"expected": args.size, "matches": find_size(fields["bullet1"])}, size_ok)

    if "description" in fields and args.description_term:
        missing = [term for term in args.description_term if not re.search(re.escape(term), fields["description"], re.IGNORECASE)]
        add_check(result, "description_required_terms", {"required": args.description_term, "missing": missing}, not missing)

    hits = []
    for name, text in fields.items():
        hits.extend({"field": name, **hit} for hit in scan(text, banned))
    add_check(result, "prohibited_terms", {"count": len(hits), "findings": hits}, not hits)

    for name, text in fields.items():
        if name in old:
            result["overlap_percent"][name] = similarity(text, old[name])

    if args.save_history:
        if not args.confirmed:
            add_check(result, "history_confirmation", {"message": "--confirmed is required before saving history"}, False)
        elif not args.sku:
            add_check(result, "history_identity", {"message": "--sku is required before saving history"}, False)
        elif result["pass"]:
            args.save_history.mkdir(parents=True, exist_ok=True)
            record = {
                "sku": args.sku,
                "marketplace": args.marketplace,
                "product_type": args.product_type,
                "brand": args.brand,
                "version": args.version,
                "confirmation_date": date.today().isoformat(),
                "source_listing_id": args.source_listing_id,
                "change_notes": args.change_notes,
                "fields": {name: text for name, text in fields.items()},
                "overlap_percent": result["overlap_percent"],
                "prohibited_terms_pass": True,
            }
            path = args.save_history / f"{args.sku}_{args.marketplace}_{args.version}.json"
            path.write_text(json.dumps(record, ensure_ascii=False, indent=2), encoding="utf-8")
            result["saved_history"] = str(path)

    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
