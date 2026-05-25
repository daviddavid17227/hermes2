# Codex implementation brief — Sports Raise wow 3D hero rebuild

Hermes PM context: the previous landing page is not visually good enough. It is generic CSS-isometric and the user explicitly rejected it. We need a major visual quality jump, not incremental polish.

## Goal
Rebuild `/root/projects/sports-raise/landing-page.html` so the first impression feels premium, cinematic, and campaign-manager impressive. The user should open the preview and say: “wow, this looks fantastic.”

Use the generated 3D asset as the hero centerpiece:

- Asset path: `assets/sports-raise-3d-hero.png`
- Dimensions: 1536×1024 PNG
- Visual contents: premium dark navy 3D/isometric sports fundraising ecosystem with glowing path, stadium, donation/credits, rewards, mobile/social/QR/video, analytics, gold/emerald/cobalt accents.

This asset is the hero. Do NOT bury it inside small CSS cards. Make the page around it feel like a high-end product launch.

## Non-negotiable constraints
- No purple/violet/lavender anywhere.
- Do not use public terms: sportsbook, wagering, cash betting, cash-out.
- Public language: game-day action, picks, predictions, challenges, non-cash credits, donated rewards, prize pool, leaderboards, campaign play, impact.
- Primary audience: campaign operators — nonprofits, charitable organizers, individuals raising for a cause.
- Make campaign/fundraiser the star, powered by Sports Raise.
- The sharing toolkit is now strategic: campaign page builder, email/social templates, widgets/links, AI-generated 15–30 second videos.

## Visual target
Think: Runway/Apple cinematic hero + fintech trust + sports-tech energy.

Not acceptable:
- generic SaaS card grid
- fake CSS 3D pretending to be art
- crowded icons everywhere
- glassmorphism slop
- low-contrast pale marketing page
- hero image too small
- every section same white card pattern

Acceptable direction:
- above-the-fold hero is dark/cinematic/full-bleed or near-full-bleed
- huge tight headline on the left, hero image huge on the right or behind/right
- 3D asset should occupy at least 50–60% of hero visual area on desktop
- subtle gradient/vignette behind hero; image should glow, not sit in a box
- layered image treatment: mask/fade edges, spotlight, soft reflection or aura, optional orbiting labels that are tasteful
- typography: large, tight, editorial/sports-tech; no default-looking bland H1
- accents: electric blue, emerald, gold only
- nav should be minimal and not compete with visual
- sections below should support story, but first screen matters most

## Suggested structure
1. Hero:
   - dark navy cinematic background
   - eyebrow: Campaign operator platform
   - H1: Give your supporters a reason to come back every game day.
   - subheadline: Sports Raise helps campaign organizers turn fans’ love of picks, predictions, and prizes into repeat contributions for causes that matter.
   - CTAs: Start a pilot campaign; See how it works
   - proof chips: Donation-first setup; One-click campaign sharing; AI-ready video assets
   - huge `assets/sports-raise-3d-hero.png` with premium visual treatment
2. Short dark/black cinematic walkthrough or chapter strip:
   - Campaign page → Donation credits → Game-day picks → Sharing toolkit → Rewards + impact
3. How it works cards — but make them refined, not generic.
4. Campaign sharing toolkit — make this visually important.
5. Video asset section — show 15s/30s campaign video concept.
6. Football season / rewards / trust / final CTA.

## Specific implementation requirements
- Keep as standalone HTML/CSS/JS file at `landing-page.html` unless existing repo structure demands otherwise.
- Use local image: `assets/sports-raise-3d-hero.png`. Relative path from HTML should work.
- Preserve responsive behavior. On mobile, show image below headline, large enough to impress but no horizontal overflow.
- Add subtle motion only if high quality: image parallax/tilt on scroll, glowing particles, tasteful reveal. Respect `prefers-reduced-motion`.
- Use CSS variables and semantic sections.
- Remove or heavily de-emphasize old CSS-generated isometric scene; the generated image is the star now.
- The result should look good at desktop 1280×700 and mobile 390×844.
- Do not commit.

## Verification checklist before handing back
- `curl` local returns 200.
- Browser opens with no console errors.
- Visual screenshot at desktop: hero looks premium; 3D asset dominates; no obvious layout defects.
- Scan source for purple/violet/lavender and banned terms.
- Public Cloudflare link returns 200.

## Final note
Do not over-explain. Implement the visual upgrade. If a choice is needed, choose the more cinematic and premium option.
