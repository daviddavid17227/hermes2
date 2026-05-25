# Codex task: Sports Raise landing-page one-shot premium redesign

You are redesigning `/root/projects/sports-raise/landing-page.html` for **Sports Raise**.

The user is unhappy with the current mobile hero image and wants a complete high-end redesign using the master design brief below. Do not make a tiny CSS tweak. Rebuild the page so it looks premium on first load on both desktop and mobile.

## Project context you must use

- Sports Raise is a campaign-operator-first sports-tech fundraising platform.
- Primary audience: nonprofits, charitable organizers, individual fundraisers, campaign operators.
- Secondary/future audience: fans/supporters who donate and participate.
- Core promise: **Give your supporters a reason to come back every game day.**
- Mechanism: campaign pages + donations + non-cash credits + picks/challenges + donated rewards/prize pool + leaderboards + sharing toolkit + AI-ready short campaign videos + impact reporting.
- Launch context: football season is a key hook; early pilots may launch with 5–10 campaigns soon.
- Tone: premium sports-tech + fintech trust + cinematic game-day energy. Not a generic nonprofit page, not a gambling page.

## Existing resources

Read and use:

- `DESIGN.md` — current Sports Raise design tokens and constraints.
- `docs/sports-raise-landing-page-outline.md` — page strategy and positioning if present.
- `assets/sports-raise-3d-hero.png` — usable existing 3D hero image, but only if it looks excellent. You may also create CSS/SVG/product mockup compositions if that produces a better result.
- `assets/logo-route-field.svg` and other logo SVGs — usable brand marks.

## Non-negotiable Sports Raise constraints

- No purple/violet/lavender as main colors or gradient colors. Avoid AI-slop purple/pink.
- Avoid public terms: sportsbook, wagering, cash betting, cash-out, gambling-first framing.
- Use terms: game-day action, picks, predictions, challenges, non-cash credits, rewards, impact, campaign play, supporter energy.
- Header must be present but **not sticky/fixed**. It should scroll away.
- Logo must be symbol + wordmark text, not a single letter in a circle.
- Mobile must be genuinely excellent at 390×844. No awkward chopped hero image. No horizontal overflow. Buttons must not wrap.
- Desktop must remain excellent; do not solve mobile by ruining desktop.
- Remove placeholder/template energy. No bracketed numeric markers like [01], [02], [03]. Prefer premium custom SVG icons.
- Every CTA must go somewhere real on this static page. Hero and final CTA should match. Use `mailto:hello@sportsraise.com?subject=Sports%20Raise%20pilot%20campaign` for pilot CTA unless a same-page anchor is more appropriate.
- Keep the page self-contained HTML/CSS/JS except existing local assets. Do not require a build step.

## The user's master design brief to apply

Apply these rules as binding acceptance criteria:

- Infer page type, niche, funnel, audience awareness, traffic temperature, and brand assets autonomously.
- Page Type should be treated as a SaaS/landing-feature conversion homepage for a campaign-operator platform.
- Design philosophy: every section should feel like it costs $20K to design; screenshot test must feel premium, on-brand, finished.
- Fonts: modern tech/SaaS/fintech should use a geometric sans such as Geist, General Sans, Switzer, Satoshi, Inter Display, SF Pro Display, Helvetica Now. Do not use Montserrat, Barlow, Poppins, Roboto, Open Sans, Lato, Oswald.
- Main headlines: 2–3 lines max. Never 4+. Rewrite copy if needed.
- Headlines 2–3x larger than subheads.
- Headline weight medium or semi-bold; avoid ultra-black unless it is intentional brand identity.
- No letter clipping. Use line-height 1.15–1.25 when needed, especially with gradient/text clipping. Descenders/ascenders must show.
- Eyebrows must be emotional/page-specific microcopy, not generic labels like “THE PROBLEM” or “OUR FEATURES”.
- Body copy 16–18px desktop, line-height 1.5–1.7, 65–75 char max line.
- Color: 2–3 main brand colors + 1 accent. No flat plain single-color sections. Use atmosphere: gradient mesh, lighting, subtle patterns, photo/product/mockup backdrops.
- Alternate dark/light section rhythm; do not have 5+ same-toned sections in a row.
- Section count for SaaS homepage/landing page: 8–12 sections, with header, hero, trust strip, features, at least one bento grid, social proof, FAQ accordion before footer, final CTA, footer.
- Grid max columns: never 5+. Use 3–4 max columns.
- Bento grid is mandatory and must tessellate: no gaps, no orphan holes, aligned row heights.
- Header: top only, never sticky, 56–80px high, high-contrast nav.
- Buttons: one-line text only, pill/rounded consistent radius, primary CTA with subtle glow, hover scale/glow. No default Bootstrap blue.
- Atmosphere is mandatory: light rays, volumetric glow, gradient mesh, stadium/product lighting, subtle patterns.
- Layered composition: floating cards, stat callouts, product mockups composited into hero.
- Animations: scroll fade/slide, counters if simple, graph draw/pulse, hover state on every interactive element, reduced-motion support.
- Imagery: real/commissioned/generated visuals or product mockups. Never stock cartoons.
- Icons: replace numbers with custom premium icons. Unique icons for cards. No emojis or clipart.
- Copy: specific, confident, active voice, 8th-grade reading level. No “game-changing”, “stunning”, “amazing”, lorem ipsum, placeholders, merge tags.
- Person/trust visuals: if showing people, use real photos/AI faces or star ratings only. No colored circle avatars/initials.
- Pre-launch checklist: no placeholders, no lorem ipsum, no template tags, no duplicate icons for different features, no spelling errors, brand colors applied, real CTA destinations, section count matches, bento present and gapless, FAQ accordion, header/footer present, 2–3 line headlines, no letter clipping, no banned fonts, no 5+ columns, mobile responsive.

## Specific design direction to hit

Create a premium, cinematic sports-tech/fintech landing page that feels closer to Apple/Revolut/Framer quality than a generic SaaS template.

Recommended direction:

- Dark navy immersive hero with stadium-light atmosphere and product/campaign ecosystem visual.
- Use `assets/sports-raise-3d-hero.png` in a controlled hero art frame only if it looks premium on mobile; otherwise create a CSS/SVG mockup composition around the product workflow.
- Mobile hero should prioritize a polished composition: headline, subhead, CTAs, then a contained/faded hero visual that fits within the first screen without looking chopped.
- Include a trust strip/launch proof row for “Campaign pages”, “One-click sharing”, “Non-cash credits”, “Donated rewards”, “Impact reporting” — but not as generic numbers.
- Include a bento section for the operator system: campaign page, sharing toolkit, game-day challenges, rewards/prize pool, impact dashboard.
- Include a process section with icons, not numeric markers.
- Include sharing/video assets section because that is imperative to this project.
- Include football-season readiness section.
- Include social proof/trust style without fake named testimonials if no real names are known. Use star-rating cards or operator-ready trust statements instead of fake people.
- Include FAQ accordion.
- Include final CTA.

## Files to edit

- Edit `landing-page.html` directly.
- You may add small local SVG/icon assets under `assets/` if useful, but prefer inline SVG symbols for icons.
- Do not delete existing assets.
- Do not commit.

## Verification you should do before finishing

After editing, run simple checks yourself where possible:

- `grep -iE 'purple|violet|lavender|sportsbook|wagering|lorem|LOGO HERE|Your Company|\{\{' landing-page.html` should return nothing relevant.
- Ensure no `position: fixed` or sticky header on `.site-header`.
- Ensure no bracketed numeric markers like `[01]` or `[02]` visible.
- Ensure the page has a viewport meta tag.
- Ensure FAQ accordion JS works or uses native `<details>`.

Return a concise summary of changed files and design decisions.
