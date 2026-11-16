import argparse
import json
import re
from pathlib import Path

RANGES = {
    'title': (70, 75),
    'highlights': (120, 125),
    'keywords': (240, 250),
    'description': (1800, 2000),
}


def terms_from_reference(path: Path):
    terms = []
    for line in path.read_text(encoding='utf-8-sig').splitlines():
        if line.startswith('| ') and not line.startswith('| 原始') and not line.startswith('|---'):
            term = line.split('|', 2)[1].strip()
            if term:
                terms.append(term)
    return terms


def words(text):
    return re.findall(r"[A-Za-z0-9]+(?:['’-][A-Za-z0-9]+)*", text.lower())


def scan(text, terms):
    findings = []
    for term in terms:
        pattern = r'(?<![A-Za-z0-9])' + re.escape(term).replace(r'\ ', r'[\s-]+') + r'(?![A-Za-z0-9])'
        for match in re.finditer(pattern, text, re.IGNORECASE):
            findings.append({'term': term, 'start': match.start(), 'context': text[max(0, match.start()-35):match.end()+35]})
    return findings


def similarity(a, b):
    wa, wb = words(a), words(b)
    if not wa or not wb:
        return 0.0
    sa, sb = set(zip(wa, wa[1:])), set(zip(wb, wb[1:]))
    return round(len(sa & sb) / max(1, len(sa | sb)) * 100, 2)


def main():
    parser = argparse.ArgumentParser(description='Check listing field lengths, prohibited terms, and text overlap.')
    parser.add_argument('--field', action='append', default=[], help='FIELD=TEXT. Supported fields: title, highlights, keywords, description, bullet1...')
    parser.add_argument('--compare', action='append', default=[], help='FIELD=OLD_TEXT')
    parser.add_argument('--terms', type=Path, default=Path(__file__).parents[1] / 'references' / 'prohibited-terms.md')
    args = parser.parse_args()
    fields = dict(item.split('=', 1) for item in args.field)
    old = dict(item.split('=', 1) for item in args.compare)
    banned = terms_from_reference(args.terms)
    result = {'checks': {}, 'overlap_percent': {}, 'pass': True}

    for name, limits in RANGES.items():
        if name in fields:
            text = fields[name]
            count = len(text)
            passed = limits[0] <= count <= limits[1]
            result['checks'][f'{name}_characters'] = {'count': count, 'required_range': list(limits), 'pass': passed}
            result['pass'] &= passed

    if 'title' in fields:
        title_words = words(fields['title'])
        repeats = sorted({word for word in title_words if title_words.count(word) > 2})
        passed = not repeats
        result['checks']['title_repeated_words'] = {'words': repeats, 'pass': passed}
        result['pass'] &= passed

    if 'keywords' in fields:
        keywords = fields['keywords']
        byte_count = len(keywords.encode('utf-8'))
        byte_pass = byte_count < 250
        lower_pass = keywords == keywords.lower()
        result['checks']['keywords_bytes'] = {'count': byte_count, 'maximum_exclusive': 250, 'pass': byte_pass}
        result['checks']['keywords_lowercase'] = {'pass': lower_pass}
        result['pass'] &= byte_pass and lower_pass

    hits = []
    for name, text in fields.items():
        hits.extend({'field': name, **hit} for hit in scan(text, banned))
    banned_pass = not hits
    result['checks']['prohibited_terms'] = {'count': len(hits), 'findings': hits, 'pass': banned_pass}
    result['pass'] &= banned_pass

    for name, text in fields.items():
        if name in old:
            result['overlap_percent'][name] = similarity(text, old[name])
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
