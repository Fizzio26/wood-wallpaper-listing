# Listing rules

## Amazon US rules recorded in the knowledge base

Use the policy snapshot recorded in `03-Amazon美国站Listing规范.md`. The 2026-07-27 title change is the configured baseline. Do not autonomously refresh policies each task. The user will tell the skill when to update policy rules. If a current Seller Central field explicitly rejects the planned content, report that concrete conflict and ask how to proceed.

Title: maximum 75 characters including spaces, brand first, same word at most twice. Main words use initial capitals and prepositions lowercase. Keep punctuation minimal.

Item Highlights: when available for the category, maximum 125 characters. Same capitalization convention, concise, avoid title repetition.

Bullets: company convention is minimum five and maximum eight bullets, aiming around 200 characters each. Use a short lead-in differentiated by punctuation or capitalization if useful. This internal content convention takes priority over the older generic five-bullet assumption in the policy summary. If the target submission interface has fewer fields, report the mismatch and present the company-preferred copy in the requested format without claiming the interface accepts extra fields.

Description: provide useful details, usage and limitations without keyword stuffing, unsupported claims, HTML or code.

Backend Search Terms: lowercase and under 250 bytes. Favor relevant uncovered synonyms and long-tail terms. Separate by spaces. Avoid repeats, unnecessary punctuation, stop words, ASINs and brands. Amazon does not guarantee using all supplied terms.

## Company product facts

Waterproof and removable are verified by default. Thickness and surface texture require user input or confirmation. Current product has no heat-resistant or antibacterial capability. Do not claim these capabilities. Competitor facts do not transfer to the user's SKU.

## User-facing copy style

Prefer clear US English and natural descriptions. In the title/highlights, capitalize major words and lowercase prepositions. Backend keyword field is lowercase. Avoid unnecessary punctuation. Never insert a prohibited term to preserve a keyword. Explain excluded keywords and offer a fact-preserving alternative where possible.

## Product intake defaults

- Product type choice: wood contact paper or wood wallpaper.
- Material defaults to vinyl when omitted.
- Installation defaults to self adhesive / peel and stick.
- Applicable surface defaults to dry, smooth, clean surfaces.
- Excluded surfaces default to wet, uneven, dusty, or textured surfaces.
- Grid backing is present on every product and can be included.
- Ask thickness as one of: thicken or upgrade thicken. Ask for surface texture only if it remains material to a claim and is not already specified.
- All task-specific information, including keywords, audience, scenarios, and supplementary benefits, is optional. If absent, derive candidates from supplied product information and available research. Label assumptions and research hypotheses. Do not invent search volume or ranking evidence.

## Updated company field-length targets and formatting

- Title target: 70–75 characters including spaces. Keep title word repetition at no more than twice and begin with the brand.
- Item Highlights target: 120–125 characters when the field is available.
- Backend Search Terms target: 240–250 characters, all lowercase. Keep within Amazon's configured byte ceiling and use the deterministic byte check; English ASCII terms generally count one byte each.
- Product Description target: 1800–2000 characters. Cover supported product features, suitable surfaces, audiences, scenarios, and application steps. Build clear links between product attributes and buyer tasks/intents based on COSMO. Do not invent product-specific performance, compatibility, or installation claims.
- Bullet Points remain 5–8 items, aiming around 200 characters each.
- Listing upload processing strips rich text. Deliver plain text. Differentiate bullet lead-ins with punctuation or capitalization only. Do not use bold, font changes, or rely on rich formatting.
- If meaningful factual inputs cannot support a field-length target, explain the shortfall and request only the missing facts. Do not pad with repetition or unsupported claims.
