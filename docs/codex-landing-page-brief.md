# Codex Brief — Sports Raise Campaign Operator Landing Page v2

## Mission

Replace the old `landing-page.html` with a new high-polish, responsive landing page for Sports Raise. This page is for **campaign operators**: nonprofits, charitable organizers, and individuals raising money for a cause.

The page must feel premium and credible, with a high-end 3D/isometric wow-factor hero inspired by the visual quality of these references, but not copied:

- https://dribbble.com/shots/26973886-3d-video-for-a-Cyber-Security-Ecosystem
- https://dribbble.com/shots/26371249-3D-Visuals-Animation-for-Websline-s-campaign

Build the hero in HTML/CSS/SVG/JS as an editable CSS-driven 3D/isometric product world. Do not depend on external image assets.

## Hard requirements

1. **No purple as a main color.** Do not use purple, violet, lavender, or `#533afd` style accents.
2. **Do not use public-facing “sportsbook” or “wagering” language.** Use donation-first language.
3. **Audience is campaign operators**, not primarily fan contributors.
4. **Responsive from day 1.** Must work at 360px, 390px, 430px, 768px, 1024px, and desktop widths. No horizontal scroll.
5. **Mobile-first CSS.** Use fluid type, grid stacking, and touch-friendly 44px+ hit targets.
6. **Self-contained static artifact.** Update `/root/projects/sports-raise/landing-page.html` with embedded CSS/JS only.
7. **High visual bar.** Avoid generic SaaS cards, AI-slop gradients, fake testimonials, generic metrics, and overused icon grids.
8. **Keep claims careful.** This is a concept/pilot page; don’t invent legal guarantees or fake customer logos/testimonials.

## Visual direction

Premium sports-tech + fundraising trust:

- Background: off-white / very pale blue-gray
- Text: deep navy / ink
- Primary accent: electric/cobalt blue
- Impact accent: emerald green
- Reward accent: gold/amber
- Dark section: deep stadium navy/ink
- Shadows: soft, blue-tinted, layered
- Materials: frosted glass, matte blocks, subtle internal glow, light film grain

Suggested tokens:

```css
--bg: #f6f9fc;
--surface: #ffffff;
--ink: #061b31;
--muted: #64748d;
--line: #dfe8f2;
--blue: #0f62fe;
--blue-dark: #0747a6;
--impact: #0e9f6e;
--gold: #d99a2b;
--stadium: #071827;
```

## Page sections

### 1. Header

- Logo: Sports Raise
- Links: How it works, Football season, Rewards, Impact
- CTA: Start a pilot campaign
- Mobile: compact nav; do not overflow.

### 2. Hero

**Headline:** Give your supporters a reason to come back every game day.

**Subheadline:** Sports Raise helps campaign organizers turn sports fans’ love of picks, predictions, and prizes into repeat contributions for causes that matter.

**Primary CTA:** Start a pilot campaign
**Secondary CTA:** See how it works

**Hero visual concept:**
Create a 3D/isometric “fundraising arena” with connected modules:

1. Campaign Launch
2. Donation + Credits
3. Game-Day Picks
4. Prize Pool
5. Impact Dashboard

The visual should have:
- perspective/isometric base plane
- glowing path connecting modules
- modular frosted/matte blocks
- embedded labels
- mini football field/scoreboard detail
- reward objects/cards (jersey/tickets/trophy abstracted)
- impact dashboard card
- subtle CSS animation: path pulse, floating modules, gentle glow
- reduced motion support

### 3. The operator insight

Explain: people already want game-day action. Sports Raise lets campaign operators redirect that energy toward a cause and create reasons for supporters to re-contribute throughout a season.

Do not say sportsbook/wagering in public copy.

### 4. How it works

Four steps:

1. Start a campaign for your cause.
2. Seed a prize pool with donated rewards or sponsor items.
3. Invite supporters to donate and receive non-cash credits.
4. Run picks, challenges, leaderboards, and impact updates through the season.

### 5. Why fundraisers use it

Cards/tiles, but make them polished and not generic:

- Repeat engagement beyond a static donation page
- Built around sports moments people already care about
- Prize pools can be donated, sponsored, or seeded by Sports Raise
- Supporters can re-up through the season
- Transparent impact keeps the cause central

### 6. Football season section

Headline idea: Be ready before kickoff.

Copy: NFL and college football create a natural campaign calendar. Launch now, build your supporter list, seed rewards, and prepare game-day challenges before Week 1.

### 7. Prize pool section

Explain reward sources:
- campaign creators
- local businesses
- sponsors
- athletes/teams
- memorabilia donors
- Sports Raise starter items for early campaigns

### 8. Trust / guardrails

Use careful trust copy:
- donation-first campaigns
- non-cash credits
- donated prizes and rewards
- configurable campaign rules
- transparent impact reporting

### 9. Final CTA

Headline: Ready to launch a campaign before football season?
CTA: Start a pilot campaign
Secondary: Talk through an idea

## Responsive behavior requirements

- At <= 767px:
  - hero text stacks above hero visual
  - CTAs become full width or nearly full width
  - 3D hero simplifies/scales; no tiny unreadable labels
  - all grids become single column
  - nav does not overflow
  - no horizontal scroll
- At 768–1023px:
  - use 2-column sections where appropriate
  - hero may remain stacked if needed
- At >= 1024px:
  - hero can be side-by-side
  - 3D scene should be the wow-factor visual

## Acceptance checks

After writing the page, run:

```bash
python3 - <<'PY'
from pathlib import Path
text = Path('landing-page.html').read_text().lower()
for bad in ['#533afd', 'purple', 'violet', 'lavender', 'sportsbook', 'wagering']:
    print(bad, text.count(bad))
PY
```

Expected: all zero except words inside comments are still not allowed.

Also verify:
- `<meta name="viewport" ...>` exists
- at least 3 responsive `@media` sections or equivalent fluid/container-query behavior
- no external image dependency
- no console errors from obvious broken JS

## Deliverable

Modify only what is needed, primarily:
- `/root/projects/sports-raise/landing-page.html`

Do not commit. Hermes will verify visually and commit later.
