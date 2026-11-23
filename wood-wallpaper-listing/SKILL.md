---
name: wood-wallpaper-listing
description: Write or renovate Amazon US wood grain self-adhesive wallpaper and contact paper listings from SKU facts, keyword research, competitor research, and confirmed history.
---

# Amazon US Woodgrain Wallpaper Listing

Use this skill for new or renovated Amazon US listings for wood grain self-adhesive wallpaper or contact paper. Read `references/knowledge-map.md` first, then load only the references needed for the current task. Competitor claims and search hypotheses are research inputs, never proof of the user's SKU.

## Workflow

1. Identify new versus renovation work and build the SKU profile. Brand, product type, color, wood grain, width × length, thickness, surface texture, package contents, supported surfaces, limitations, and marketplace are the key inputs. Package quantity defaults to 1. Product type is `wood contact paper` or `wood wallpaper`. If material is absent, record vinyl as the internal default, but do not place `vinyl` in the title.
2. If one or more competitor ASINs are supplied, run the competitor research gate before keyword planning and drafting. Read the competitor's public listing for selling points and use SIF to retrieve its keyword data. Record search volume, natural rank, query date/month, source ASIN, and the relevant product intent. Keep only terms that match the user's SKU. If SIF is not connected, mark the ranking evidence as pending and do not claim search or ranking results. Never transfer competitor-only claims to the user's SKU.
3. Classify candidate keywords as core, secondary, long-tail, or excluded. Rank usable terms by SKU relevance first, then search volume, then competitor natural rank when those data exist. Explain exclusions for cross-category, unsupported, duplicate, brand, ASIN, typo, or policy-risk terms.
4. Map each verified feature to buyer task or intent, scenario, benefit, evidence, and limitation. Prepare a field plan and wait for user approval before drafting.
5. Draft according to the field logic below. For renovation, map source content to retain, optimize, delete, or add and preserve useful source claims and keywords. Keep more than 60% continuity with the original listing unless the user directs otherwise.
6. Run `scripts/check_listing.py` and model review. Report every issue with field, location, reason, and suggested correction. On edits, change only requested parts and rerun affected checks.
7. Save only after explicit final confirmation. Store confirmed versions according to `references/history-schema.md`. Generate Word only when explicitly requested.

## Field writing logic

### Title

Begin with the brand and include the primary size. Format size as `17.3×78.7in`: use the multiplication sign when available, use `in` for inches, and write `in` only once after the complete size. `Peel and Stick` may appear as part of a relevant `peel and stick wallpaper` or `peel and stick contact paper` phrase; do not use it as a standalone selling-point phrase. Do not use `vinyl`, `self adhesive`, `removable`, `waterproof`, `thicken`, `seamless`, audience terms, or other selling-point words in the title. Keep the title at the configured 70–75 character target, use Title Case for major words, and do not repeat a word more than twice.

Title, Item Highlights, and Backend Keywords must be composed from relevant keyword groups and word roots. Prefer adjacent words that form a complete phrase, while also allowing a phrase to be formed across a short intervening word when the resulting wording remains natural and factually accurate. Do not concatenate unrelated terms or insert keywords in a way that changes product meaning. For example, `wood grain contact paper`, `peel and stick wallpaper`, and `contact paper for cabinets` may be planned as reusable phrase units; unsupported scenes or uses must still be excluded.

Allocate high-value keyword groups across fields instead of repeating the same group at the start of both Title and Item Highlights. Use one primary group in the Title, a different verified group in Item Highlights, and uncovered variants or long-tail groups in Backend Keywords. Before drafting, make a compact allocation map with the source keyword, evidence status, assigned field, and reason. A word root may recur when it is part of distinct phrase units, but do not waste prime field space by duplicating an identical high-value phrase across fields without a specific indexing reason.

Every non-brand, non-size word in the Title must belong to a verified keyword group or be necessary grammar. Do not add filler words such as `roll`, `makeover`, `update`, `project`, or `home` merely to reach the character target. If the title is short, add a more relevant verified group rather than a generic product word.

### Item Highlights

Use 120–125 characters when the field is available. The highlights must contain the functional terms `self adhesive`, `removable`, and `waterproof`, subject to the user's confirmed product facts and stated limitations. Write Highlights in strict Title Case: capitalize each word except prepositions and `and`. Put high-relevance terms first, then high-search-volume terms, then terms with strong competitor natural rank. Use keyword-library and SIF terms naturally; do not force a term that changes the product meaning.

Do not use filler nouns or promotional wording such as `makeovers`, `projects`, `updates`, or similar terms as keyword substitutes unless they are verified in the supplied keyword library or SIF evidence and materially improve a supported phrase. If a term has no recorded search-volume or ranking evidence and is not needed for grammatical completeness, omit it and use a verified, relevant keyword group instead.

### Backend keywords

Use lowercase, relevant uncovered terms and construct them from keyword groups and word roots, including natural phrase units and valid phrases separated by a short intervening word. Core word roots such as `wood` may appear more than once when they belong to distinct relevant phrases. Do not repeat selling-point phrases already used in the title or highlights, except where a policy or field requirement makes the phrase necessary. Remove brands, ASINs, punctuation, duplicates, stop words, unsupported uses, and irrelevant category terms. The configured target is 240–249 bytes because the current ceiling is under 250 bytes.

Prioritize exact supplied core and secondary groups, then verified competitor/SIF variants, then relevant long-tail groups. Do not fill unused bytes with random nouns. When a repeated root is necessary to preserve multiple distinct keyword groups, keep the groups readable and record that the repetition is intentional; do not treat the backend field as a comma-separated keyword dump.

Avoid spending multiple backend positions on near-duplicate wording for one intent. For example, do not include both `countertop contact paper` and `contact paper for countertops` unless both have separate evidence and a materially different search intent; select the stronger, more relevant group and use the remaining bytes for another uncovered intent.

Use keyword-chain composition when it creates multiple valid overlapping phrases from one continuous sequence. For example, `wood grain contact paper peel and stick for cabinets wallpaper` can expose `wood grain contact paper`, `wood contact paper`, `contact paper`, `contact paper peel and stick`, `contact paper peel and stick for cabinets`, `cabinets wallpaper`, `cabinet wallpaper`, and `wallpaper`. Keep the chain semantically related and factually supported; do not append unrelated words merely to manufacture combinations. The chain may include a second related cluster after a space when needed to reach the byte target.

### Bullet points

Use 5–8 bullets, aiming for about 200 characters each. Bullet 1 must state the size. Rotate the order of the remaining themes across listings to reduce repetitive structure while covering product features, installation, supported surfaces, scenarios, and limitations. Every claim must match the SKU. Do not promise heat resistance, antibacterial performance, zero bubbles, permanent adhesion, or other unsupported capabilities.

Every bullet must begin with a short functional subheading followed by a colon, such as `SIZE AND COVERAGE:` or `SUITABLE SURFACES:`. Keep the body after the subheading in normal sentence case. Do not capitalize every word in bullet bodies; strict Title Case is reserved for the Title and Item Highlights.

### Description

Use 1800–2000 characters when the verified facts support that length. Explain the product's appearance, supported surfaces, buyer tasks, realistic scenarios, installation sequence, and practical limitations. Allocate keywords by intent and avoid repeating a keyword merely to fill the field. Use COSMO as an intent-mapping framework, not as evidence of ranking or conversion.

## Product defaults and evidence

Installation defaults to `self adhesive / peel and stick`; package quantity defaults to 1; supported surfaces default to dry, smooth, clean surfaces; excluded surfaces default to wet, uneven, dusty, or textured surfaces; grid backing is present by default. Waterproof and removable follow the existing company defaults, but the SKU profile must retain their limitations. Thickness, surface texture, and scenes follow the existing intake rules; ask only when a SKU-specific ambiguity affects a claim. The current product is not heat resistant or antibacterial. Do not claim either.

## Quality checks

Read `references/listing-rules.md` and `references/prohibited-terms.md` for final review. Check factual support, competitor attribution, dimensions, material, installation, supported surfaces, keyword relevance, title restrictions, field lengths, capitalization, bullet count, backend byte count, prohibited terms, and history overlap. Deterministic checks come from `scripts/check_listing.py`; semantic similarity, structural similarity, relevance, and fact review remain model judgments. Generic category phrases may recur when necessary.

## Output sequence

1. Research and planning, including the competitor gate when ASINs are provided.
2. User approval or edits to the plan.
3. English listing draft in this field order: Title, Item Highlights, Backend Keywords, Bullet Points, Description; then provide the issue report.
4. Requested iterations with affected checks rerun.
5. Explicit final confirmation, then history storage.
