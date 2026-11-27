# Keyword phrase architecture

Use this reference while classifying candidate keywords and before allocating them to Listing fields. It is a copy-planning method, not evidence of Amazon search ranking.

## Build intent clusters before writing

Create a small phrase bank from verified, SKU-relevant terms. Keep each candidate linked to one intent:

| Intent cluster | Typical components | Example shape |
| --- | --- | --- |
| Product identity | color/look + product type | `black wood contact paper` |
| Installation format | product type + peel-and-stick form | `peel and stick wallpaper` |
| Visual finish | color/look + grain + product type | `black wood grain contact paper` |
| Verified task or surface | product type + one supported task/surface | `contact paper for cabinets` |

Do not manufacture every possible permutation. A phrase needs a verified product meaning and, where available, keyword evidence. Similar terms belong in the same cluster rather than being scattered across every field.

## Candidate tiers supplied by the user

Treat the user's three lists as a starting hierarchy, not pre-approved copy:

- **Core keywords:** product-identity phrases. They are the first title candidates when verified and relevant.
- **Secondary keywords:** differentiating terms such as color, grain, finish, installation form, or another SKU-specific distinction. Use them to refine the core phrase or cover an additional intent.
- **Long-tail keywords:** a complete, validated task or surface phrase. They may appear in a title, Highlight, Bullet, Description, or Backend only when the phrase is natural and supported; do not treat every scene word as a long-tail keyword.

For each term, retain its source (`SIF-MCP competitor reverse search` or `user keyword pack`), source ASIN if applicable, relevant SKU fact, and intended buyer question. A source tier guides priority but never overrides relevance or factual support.

## Allocate phrases by field

- **Title:** Brand + one primary category phrase + one distinguishing visual/product attribute + size. Add at most one task or surface phrase, only when it remains a natural query phrase and is high priority.
- **Highlights:** State decision-critical verified functions first. If space remains, use one compact surface or task cluster. Do not list rooms, furniture items, and audiences in sequence.
- **Bullets and Description:** Answer a different buyer question in each section. Use complete phrases in context, not a chain of aliases.
- **Backend:** Reserve uncovered synonyms and one or two supported long-tail phrases. Arrange terms in intent bundles, separated by spaces. Do not add individual room names, use cases, or decorative nouns just to reach the byte target.

## Scenario-word controls

Classify a term as a scenario word when it names a room, audience, lifestyle, furniture object, or project rather than the product category, verified function, visual finish, or installation format.

- A title normally uses no scenario word, and never more than one surface/task phrase.
- A Highlight uses at most one compact scenario cluster.
- Backend terms must contain no standalone scenario word unless it completes a verified, useful long-tail phrase.
- If the source keyword is a broad scene query but the SKU facts do not establish that use, exclude it and state why.

## Phrase quality review

Before finalizing, test each phrase:

1. Would a US shopper recognize it as a natural product query or a clear sentence fragment?
2. Does every word still describe this exact SKU?
3. Does it add a distinct intent, rather than repeat a title/highlight phrase?
4. If its scenario word were removed, would the remaining phrase be more accurate? If yes, remove it unless the full long-tail phrase has validated value.

Report phrase choices as `core`, `secondary`, `long-tail`, or `excluded`, with the field assignment and reason. Do not call an unmeasured phrase high-volume, high-ranking, or Rufus-preferred.
