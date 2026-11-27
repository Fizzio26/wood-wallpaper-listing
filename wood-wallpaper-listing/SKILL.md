---
name: wood-wallpaper-listing
description: Write or renovate Amazon US wood grain self-adhesive wallpaper and contact paper listings from SKU facts, keyword research, competitor research, and confirmed history.
---

# Amazon US Woodgrain Wallpaper Listing

Use this skill for new or renovated Amazon US listings for wood grain self-adhesive wallpaper or contact paper. Read `references/knowledge-map.md` first, then load only the references needed for the current task. Competitor claims and search hypotheses are research inputs, never proof of the user's SKU.

## Workflow

1. Identify new versus renovation work and build the SKU profile. Brand, product type, color, wood grain, width × length, thickness, surface texture, package contents, supported surfaces, limitations, and marketplace are the key inputs. Package quantity defaults to 1. Product type is `wood contact paper` or `wood wallpaper`. If material is absent, record vinyl as the internal default, but do not place `vinyl` in the title.
2. If one or more competitor ASINs are supplied, run the competitor research gate before keyword planning and drafting. Read each competitor's public listing for selling points and use SIF-MCP to reverse-search its keywords. Record search volume, natural rank, query date/month, source ASIN, and the relevant product intent. Build the candidate pool from relevant competitor reverse-search terms first, then add relevant terms from the user's keyword pack. Keep only terms that match the user's SKU. If SIF-MCP is not connected or returns no usable data, mark the ranking evidence as pending and fall back to the keyword pack without claiming search or ranking results. Never transfer competitor-only claims to the user's SKU.
3. Classify candidate keywords as core, secondary, long-tail, or excluded. These are candidate tiers, not fixed field assignments. Filter for SKU relevance first; then prioritize competitor reverse-search terms, followed by the user's keyword pack, and finally any clearly-labelled research hypotheses. Within a source tier, use search volume, then competitor natural rank when those data exist. Explain exclusions for cross-category, unsupported, duplicate, brand, ASIN, typo, or policy-risk terms.
4. Map each verified feature to buyer task or intent, scenario, benefit, evidence, and limitation. For question-led planning, read `references/cosmo.md`; use only questions answerable from verified SKU facts. For keyword allocation and phrase construction, read `references/keyword-architecture.md`. Prepare a field plan and wait for user approval before drafting.
5. Draft according to the field logic below. For renovation, map source content to retain, optimize, delete, or add and preserve useful source claims and keywords. Keep more than 60% continuity with the original listing unless the user directs otherwise.
6. Run `scripts/check_listing.py` and model review. Report every issue with field, location, reason, and suggested correction. On edits, change only requested parts and rerun affected checks.
7. Save only after explicit final confirmation. Store confirmed versions according to `references/history-schema.md`. Generate Word only when explicitly requested.

## Field writing logic

### Title

Begin with the brand and include the primary size. Format size as `17.3×78.7in`: use the multiplication sign when available, use `in` for inches, and write `in` only once after the complete size. Build the title around one verified category phrase and one differentiating visual or product attribute; do not turn it into a catalogue of surfaces or rooms. Add a use or surface phrase only when it is a high-priority, SKU-relevant query phrase and remains natural. `Peel and Stick` may appear as part of a relevant `peel and stick wallpaper`、`wallpaper peel and stick` or `peel and stick contact paper`、`contact paper peel and stick` phrase; do not use it as a standalone selling-point phrase. Do not use `vinyl`, `self adhesive`, `removable`, `waterproof`, `thicken`, `seamless`, audience terms, or other selling-point words in the title. Keep the title at the configured 70–75 character target, use Title Case for major words, and do not repeat a word more than twice.

### Item Highlights

Use 120–125 characters when the field is available. The highlights must contain the functional terms `self adhesive`, `removable`, and `waterproof`, subject to the user's confirmed product facts and stated limitations. Write Highlights in strict Title Case: capitalize each word except prepositions and `and`. State the feature or buyer task before any use context. Use one compact, validated surface cluster at most; do not pad the field with a string of rooms, furniture types, or scenarios. Put high-relevance terms first, then high-search-volume terms, then terms with strong competitor natural rank. Use keyword-library and SIF terms naturally; do not force a term that changes the product meaning.

### Backend keywords

Use lowercase, relevant uncovered terms. Compose compact phrase bundles around distinct intents instead of appending isolated scene nouns. Core word roots such as `wood` may appear more than once when they belong to distinct relevant phrases. Do not repeat selling-point phrases already used in the title or highlights, except where a policy or field requirement makes the phrase necessary. Remove brands, ASINs, punctuation, duplicates, stop words, unsupported uses, and irrelevant category terms. The configured target is 240–249 bytes because the current ceiling is under 250 bytes. Do not fill unused bytes with speculative scenario words; report a fact-preserving shortfall when the available terms cannot support the target.

### Bullet points

Use 5–8 bullets, aiming for about 200 characters each. Bullet 1 must state the size. Rotate the order of the remaining themes across listings to reduce repetitive structure while covering product features, installation, supported surfaces, scenarios, and limitations. Every claim must match the SKU. Do not promise heat resistance, antibacterial performance, zero bubbles, permanent adhesion, or other unsupported capabilities.

### Description

Use 1800–2000 characters when the verified facts support that length. Explain the product's appearance, supported surfaces, buyer tasks, realistic scenarios, installation sequence, and practical limitations. Allocate keywords by intent and avoid repeating a keyword merely to fill the field. Use COSMO as an intent-mapping framework, not as evidence of ranking or conversion.

## Product defaults and evidence

Material defaults to `vinyl`; installation defaults to `self adhesive / peel and stick`; package quantity defaults to 1; supported surfaces default to dry, smooth, clean surfaces; excluded surfaces default to wet, uneven, dusty, or textured surfaces; grid backing is present by default. Dry, smooth, clean countertops are a supported default surface, but never imply food-contact suitability, heat resistance, direct shower use, soaking, or prolonged water exposure. Waterproof means ordinary splashes and wipe-down care only. Removable means it may be removed with care; never promise residue-free or damage-free removal on every substrate. These are company-wide defaults and do not need to be re-entered per SKU unless the SKU differs. Thickness, surface texture, and scenes follow the existing intake rules; ask only when a SKU-specific ambiguity affects a claim. The current product is not heat resistant or antibacterial. Do not claim either.

## Quality checks

Read `references/listing-rules.md` and `references/prohibited-terms.md` for final review. Check factual support, competitor attribution, dimensions, material, installation, supported surfaces, keyword relevance, title restrictions, field lengths, capitalization, bullet count, backend byte count, prohibited terms, and history overlap. Deterministic checks come from `scripts/check_listing.py`; semantic similarity, structural similarity, relevance, and fact review remain model judgments. Generic category phrases may recur when necessary.

## Output sequence

1. Research and planning, including the competitor gate when ASINs are provided.
2. User approval or edits to the plan.
3. English listing draft and issue report.
4. Requested iterations with affected checks rerun.
5. Explicit final confirmation, then history storage.
