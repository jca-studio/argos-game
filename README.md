# JCA Studio — Editorial revision 02

This is a **review draft**, not an automatically published site. No live Vercel or GitHub changes were made.

## Changes from first editorial redesign
- Cooler off-white background, brighter burgundy, cobalt headline emphasis, orange hero eyebrow.
- More compact JC/A logo with STUDIO centered.
- Smaller, tighter homepage hero.
- Journal title now strong contemporary sans-serif rather than expressive serif.
- November 2026 and orange journal date accent.
- Revised About copy to emphasize original creativity, leadership, and AI-assisted hands-on building.
- Contact section on home, Contact navigation link, email + LinkedIn in all footers.
- Reusable AI Receipts component pattern in first journal article: Granola, ChatGPT, Gemini, Claude, based ONLY on user-confirmed use.

## Still intentionally pending
- **Article editorial approval:** Story kept substantively unchanged.
- **Featured project artwork:** Existing typographic graphic kept as a temporary visual; develop a distinct visual together before launch.
- **Logo alignment, mobile, and style** need review in the actual Vercel preview.
- Verify Google Analytics measurement ID/property belongs to you and traffic is captured.

## Deployment
1. Keep current production (`main`) protected.
2. Open GitHub repo's `editorial-redesign` branch.
3. Upload the **contents** of this folder to repository root; commit on `editorial-redesign`.
4. Open Vercel Preview deployment for the branch.
5. Review on desktop and mobile; do not merge until approved.

GA4 ID retained from previous site source. Game is a separate Vercel project and remains untouched.

## Vercel Analytics added in Revision 03
- Added Vercel Web Analytics tracking to the `<head>` of **all four HTML pages**.
- Uses the static-site script endpoint `/_vercel/insights/script.js`; no npm, React, or Next.js required.
- Vercel Web Analytics must be enabled for the `jca-studio-website` project (as shown in the dashboard).
- After deploying, visit multiple pages and check Vercel Analytics, selecting the Preview environment if necessary. If the script returns 404, consult Vercel's analytics dashboard HTML/Other instructions for a project-specific randomized `/<unique-path>/script.js` and replace the script URL in each HTML page.
- Existing Google Analytics tag remains unchanged; verify its property is yours.
- Production and GitHub were not modified. Upload this revision's contents to `editorial-redesign` only.


## Revision 04 — Selected Work Christmas image update
- Replaced the homepage's temporary black “30” typographic artwork with the user's original Argos game photograph (`assets/argos-game-original.jpg`). The original photo is copied byte-for-byte; no AI-generated products or handwriting.
- Added the approved “THE GAME MUST GO ON.” caption as accessible HTML text, plus orange rule, burgundy wine naturally present in the photo, and cobalt corner accent via CSS.
- Kept the project headline, description, category, link, and layout on the right unchanged.
- Added responsive styling at the existing breakpoints.
- No other page HTML was changed; existing Google Analytics and Vercel Analytics script tags remain intact.
- For live review, deploy to `editorial-redesign` preview only. The zip is not deployed.
- The portrait photograph is cropped using CSS `object-fit: cover` for the wide card, so some margins/details may not all show simultaneously. The source file retains every original detail.


## Revision 05 — Full Christmas launch article

- Restored the fuller user-supplied narrative to `journal/christmas-tradition/index.html`, including the opening family game story, the Google Meet detail, the fuller AI-build explanation, the six-week challenge, and the closing audience question.
- Kept the approved public headline **Can AI Help Me Save a 30-Year-Old Christmas Tradition?** instead of the working draft title.
- Omitted unapproved working name **Project Argos**.
- Omitted the 2026 Argos campaign aside, which was marked in the draft as a possible voice mismatch; this can be reinstated after editorial review.
- Changed “Three countries. Three time zones.” to “Three countries.” to avoid a potentially inaccurate claim across Seattle, Portugal, and the UK.
- Preserved the original homepage feature, original photograph, styles, project overview, navigation, analytics scripts, and recurring AI Receipts section.
- This is an editorial integration for review, **not** a deployment or final publication approval.
