---
name: wood-wallpaper-listing
description: Write or renovate Amazon US wood grain self-adhesive wallpaper and contact paper listings using SKU facts, keyword research, company rules, and confirmed historical listings.
---

# Amazon US Woodgrain Wallpaper Listing

Use this skill for new or renovated Amazon US listings for wood grain self-adhesive wallpaper/contact paper. First read `references/knowledge-map.md`, then load only the references needed for the task. Never treat competitor claims or search hypotheses as facts for the user's SKU.

## Workflow

Identify whether the task is new or renovation and identify the SKU/product profile. Brand name is required and starts the title. Product type is selected as wood contact paper or wood wallpaper. If the user does not specify material, default to vinyl. Installation defaults to self adhesive / peel and stick. Applicable surfaces default to dry, smooth, clean surfaces. Excluded surfaces default to wet, uneven, dusty, or textured surfaces. Grid backing is present on every product and may be used. Waterproof and removable are verified by user default. Ask about thickness using the options thicken or upgrade thicken when absent. Do not ask users to list product limitations already captured here. Ask follow-up questions only for material facts that remain SKU-specific and unclear. The current product is not heat resistant or antibacterial. Do not claim either.

本次任务信息均为选填。若用户未提供关键词、场景、人群或补充卖点，根据产品档案、已提供材料及可访问的竞品 ASIN 信息自行整理候选内容，并区分已验证事实与研究假设。没有竞品 ASIN 或关键词数据时，不得声称获得搜索量、排名或流量数据。Classify keywords as core, secondary, long-tail, or excluded. Assess relevance and duplication, then explain rejected terms. Rank candidate selling points by verified truth, buyer need, relevance, distinctiveness, and scenario fit. Map feature → consumer task/intent → scenario → benefit. Prepare a planning table with priority and field placement. For new listings, present the outline. For renovations, map source content to retain, optimize, delete, or add and protect existing useful claims and keywords. Do not infer keyword value without performance data. Renovation copy should retain over 60% continuity with its source listing.

Wait for user approval or edits to the plan before drafting listing text. After drafting, run all relevant checks and report each issue with location, reason, and suggested correction. On user edits, change only requested parts and rerun relevant checks. Save only user-confirmed final listings. Generate Word only when explicitly requested.

## Listing rules

Follow `references/listing-rules.md`. Company targets: title 70–75 characters, highlights 120–125 characters, backend keywords 240–250 characters, and description 1800–2000 characters. Title begins with brand and no word repeats more than twice. Title/highlights use Title Case except prepositions. Bullets 5–8, about 200 characters each. Backend keywords lowercase. Listing output is plain text because upload processing removes rich formatting. Company word-count guidance is distinct from Amazon field capability. Apply the user-defined field-specific historical thresholds.

## Description should explain product use broadly, including supported surfaces, audiences, scenarios, and practical application steps when supported by known facts. Use COSMO as an intent-coverage framework, not as a reason to repeat keywords or invent claims. Format bullet lead-ins with punctuation or capitalization only. Do not rely on bold, font changes, or other rich formatting.\n\n## Quality checks

Read `references/prohibited-terms.md` and check every listing field. Check factual support, competitor attribution, performance claims, use conditions, dimensions/material/installation consistency, natural English, keyword coverage, and policy formatting. Compare title, highlights, keywords, bullets and description against confirmed history by field. Report text overlap and semantic/structural similarity separately. Generic product phrases can recur when needed. Never distort facts or language to lower overlap.

Use `scripts/check_listing.py` for deterministic title length, repeated title words, backend byte length, prohibited term matches, and field-level text overlap. Model judgment remains responsible for semantic similarity, structure, relevance, facts, and wording. Historical storage begins empty. Follow `references/history-schema.md` when adding a confirmed final version.

## Output sequence

1. Plan and wait for approval.
2. Draft English listing and quality findings.
3. Iterate on requested changes.
4. Save only after explicit final confirmation.
5. Create Word only after explicit request.



