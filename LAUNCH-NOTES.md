# JCA Studio — Revision 06 launch candidate

Built from Revision 05. Preserves homepage imagery, article text, and analytics scripts.

Added: page-specific canonical/Open Graph/Twitter metadata, sitemap, robots sitemap reference, and conservative Vercel security headers (X-Content-Type-Options, Referrer-Policy, X-Frame-Options, Permissions-Policy).

**Important:** The OG image uses the ORIGINAL uploaded portrait photograph. LinkedIn may crop this image in its link preview. Inspect the preview and consider replacing it with a deliberately composed 1.91:1 social card after launch.

**CSP intentionally NOT added**: Google Analytics uses inline script; strict CSP without hashes/nonces will break current scripts. Add after testing. These headers do not constitute a penetration test.

Do not change or remove preview authentication. Check production domain accessibility and deployment protection after merging.

GitHub: upload all contents to editorial-redesign, inspect Vercel preview, merge to main only after approving. No deployment was made by generating this ZIP.
