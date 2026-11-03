# Revision 09 — final review build

- Home photo and Discover link now point to `/journal/christmas-tradition/`. The former `/projects/christmas-game/` is a temporary redirect for old inbound links.
- Restored AI / Family / Making Things and location: Between Seattle & London. New Yorker at heart.
- Article image is alongside title on desktop; full copy flows below. The original photo file is unchanged. Caption supplied by user: December 2020.
- Simplified article typography; restrained cobalt and burgundy on the human-judgment pull quote and transparency line.
- Removed redundant ending, compact pale-orange AI Receipts, moved Argos disclaimer below as The Fine Print.
- Added tested share and copy-link controls at top and bottom (browser test still required).
- Reduced listing headline size.

## Publishing to a private preview
Do not send the production URL to reviewers yet. Upload the contents of the ZIP (not the ZIP itself) to the `editorial-redesign` branch of `jca-studio/JCA-Studio-Website`. Vercel should generate a preview deployment. Review the Deployments list and open the new preview link. By default Vercel Authentication may block other reviewers; keep protection in place, and invite reviewers through Vercel access controls or use a scoped Vercel shareable preview link if supported by your account. Do not turn off all deployment protection globally.

Before going public, approve preview desktop/mobile, verify the complete article and homepage links, ensure analytics and HTTPS work, then merge into `main` and assess production authentication separately.
