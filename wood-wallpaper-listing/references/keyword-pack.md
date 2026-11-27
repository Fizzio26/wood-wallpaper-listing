# Default SIF US wood keyword pack

Use this reference for every wood wallpaper or wood contact paper Listing task before keyword planning. The bundled source workbook is [wood-keyword-pack-sif-2026-11-27.xlsx](wood-keyword-pack-sif-2026-11-27.xlsx). It replaces the need to ask the user for a general wood keyword pack on later tasks.

## Source scope

- Marketplace: Amazon US.
- Source: SIF reverse-search collection for the user's top wood-pattern products.
- Workbook package date: 2026-11-27. The workbook reports data refreshed through 2026-11-26; retain its stated date when reporting results.
- Sheets: `关键词包` is the de-duplicated keyword library; `反查明细` is ASIN × keyword evidence; `ASIN覆盖` records the collected ASIN pattern/color classification and coverage.
- The library contains 2,897 unique keyword rows and 21,176 ASIN × keyword detail rows. Blank metric cells mean no reported value in the source; do not convert them to zero.

## Required usage

1. Start with `关键词包` to find candidate terms and their pattern/category classification, usage note, monthly search-volume range, best ABA rank, and source ASINs.
2. Cross-check a selected term in `反查明细` when its source ASIN, natural rank, traffic share, or SIF label affects priority.
3. If a task supplies competitor ASINs, run a new SIF-MCP reverse search for those exact ASINs first. Use this bundled pack second, even when the current task has no additional keyword file.
4. Record whether each retained term came from the current competitor reverse search or this bundled pack.

## Pattern and category filter

The pack combines several visual/product families. It is a candidate library, never proof that every term fits every wood product.

- Match the SKU's actual color and wood-pattern facts first. White-only, black-only, walnut-only, shiplap, slat/fluted-panel, herringbone, chevron, and mixed-color terms require a direct match.
- Exclude wood panel, wood slat, fluted panel, shiplap, herringbone, chevron, wall-plank, and other structurally different product terms unless the SKU actually has that construction or pattern.
- Treat broad category and scenario terms as candidates, not automatic inclusions. A room, furniture item, or project may appear only as part of a natural, verified phrase with distinct buyer intent.
- Remove non-English, brand, ASIN, accessory, tool, unrelated color, and unsupported-performance terms unless the task explicitly supports them.
- Do not infer product claims from an ASIN's appearance, title, or traffic metrics. Competitor evidence prioritizes search language only.

## Selection rules

- Prefer relevant current-competitor SIF-MCP terms, then relevant terms from this pack.
- Within the same source, prefer SKU relevance, then reported monthly search volume, then natural rank. Use traffic-share fields only within their source ASIN; never add them across ASINs.
- Use the source workbook's pre-classification as a review cue, not final judgment. Color and pattern classifications may be ambiguous and must be checked against the current SKU.
- Keep the final field allocation governed by `keyword-architecture.md`; this package does not authorize scenario-word stacking or keyword stuffing.
