# Competitor and SIF keyword research

Use this reference when the user provides competitor ASINs or asks for competitor-informed keyword planning. When one or more competitor ASINs are present, query every supplied ASIN through SIF-MCP before drafting. Competitor reverse-search output is the first keyword source; the user's keyword pack is the second source.

## Required record

For each ASIN, record marketplace, ASIN, public listing URL or source, access date, observed selling points, product type, dimensions, material and claims, SIF query month, keyword, search volume, natural rank, traffic or conversion fields when available, and research notes.

## Evidence separation

- User SKU facts: usable for claims after the user's evidence or confirmation supports them.
- Public competitor information: usable for market language, buyer concerns and candidate selling points; it does not prove the user's SKU.
- SIF metrics: usable for keyword prioritization; they do not prove product compatibility or copy accuracy.
- Model hypotheses: usable for planning only and must be labelled as hypotheses.

## Source and selection order

1. Collect SIF-MCP reverse-search terms for every supplied competitor ASIN. Retain the source ASIN and query month for each record.
2. Add the user's keyword-pack terms as a distinct source. They remain useful for coverage, particularly where SIF-MCP has no result.
3. Remove terms that conflict with the SKU, represent another product category, contain another brand or ASIN, or require an unsupported claim.
4. Classify retained terms as `core`, `secondary`, or `long-tail`; this labels intent and priority, not a required Listing field.
5. Allocate each selected term to the field where it reads naturally and adds uncovered buyer intent.

If SIF-MCP data are unavailable, state that the reverse-search evidence is pending and use the relevant keyword pack without inventing volume, rank, or traffic values.

## Selection order within each source

1. Remove terms that conflict with the SKU, represent another product category, contain another brand or ASIN, or require an unsupported claim.
2. Group spelling variants and duplicate word roots.
3. Score relevance as high, medium or low with a short reason.
4. Within the relevant group, prioritize search volume, then competitor natural rank, then scenario fit and field coverage.
5. Assign each selected term to Title, Highlight, Bullet, Description or Backend. Do not repeat a selling-point phrase in Backend when it already appears in Title or Highlights.

If SIF is unavailable, preserve the keyword candidate and mark its ranking and volume evidence as pending. Never invent a metric.
