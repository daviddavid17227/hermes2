---
version: alpha
name: Sports Raise
description: "Premium sports-tech fundraising brand: cinematic, donation-first, game-day energy with fintech trust."
colors:
  primary: "#1178FF"
  secondary: "#1BCF8F"
  tertiary: "#F4B743"
  neutral: "#F5F8FB"
  night: "#020814"
  navy: "#061424"
  navyElevated: "#0A2036"
  ink: "#07182A"
  cloud: "#F5F8FB"
  white: "#FFFFFF"
  textOnDark: "#F6FBFF"
  mutedOnDark: "#AAB9C8"
  mutedOnLight: "#64758A"
  lineLight: "#D9E5EF"
  lineDark: "#24384D"
  actionBlue: "#1178FF"
  actionCyan: "#18C7FF"
  impactEmerald: "#1BCF8F"
  impactMint: "#68F2B9"
  rewardGold: "#F4B743"
  rewardCream: "#FFE08A"
typography:
  display-xl:
    fontFamily: Inter
    fontSize: 7.25rem
    fontWeight: 950
    lineHeight: 0.88
    letterSpacing: "-0.065em"
  display-md:
    fontFamily: Inter
    fontSize: 4rem
    fontWeight: 900
    lineHeight: 0.98
    letterSpacing: "-0.055em"
  headline:
    fontFamily: Inter
    fontSize: 2rem
    fontWeight: 850
    lineHeight: 1.08
    letterSpacing: "-0.035em"
  body-lg:
    fontFamily: Inter
    fontSize: 1.22rem
    fontWeight: 400
    lineHeight: 1.58
    letterSpacing: "-0.01em"
  body-md:
    fontFamily: Inter
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
  label:
    fontFamily: Inter
    fontSize: 0.74rem
    fontWeight: 900
    lineHeight: 1.2
    letterSpacing: "0.12em"
rounded:
  sm: 10px
  md: 16px
  lg: 24px
  xl: 34px
  pill: 999px
spacing:
  xs: 6px
  sm: 10px
  md: 16px
  lg: 24px
  xl: 36px
  section: 84px
components:
  button-primary:
    backgroundColor: "{colors.actionCyan}"
    textColor: "{colors.ink}"
    rounded: "{rounded.pill}"
    padding: 14px 18px
  button-primary-hover:
    backgroundColor: "{colors.white}"
  button-secondary:
    backgroundColor: "{colors.navyElevated}"
    textColor: "{colors.textOnDark}"
    rounded: "{rounded.pill}"
    padding: 14px 18px
  card-dark:
    backgroundColor: "{colors.navyElevated}"
    textColor: "{colors.textOnDark}"
    rounded: "{rounded.lg}"
    padding: 24px
  card-light:
    backgroundColor: "{colors.white}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    padding: 24px
---

## Overview

Sports Raise is a premium sports-tech fundraising brand. It should feel like a polished fintech/product launch crossed with game-day energy: credible enough for nonprofits and campaign operators, exciting enough for sports fans, and visually memorable enough to make a new company feel serious.

The brand promise is donation-first participation. Sports Raise helps campaign operators turn game-day attention into repeat contributions through non-cash credits, picks/challenges, donated rewards, sharing tools, and visible impact.

The visual center of gravity is cinematic dark navy, electric blue action, emerald impact, and gold rewards. Purple/violet/lavender are intentionally excluded because they read as generic AI/SaaS slop for this brand.

## Colors

- **Night (#020814):** Primary immersive background for hero, premium sections, and video/storytelling surfaces.
- **Navy (#061424):** Secondary dark background for product UI surfaces and page transitions.
- **Navy Elevated (#0A2036):** Dark cards, consoles, overlays, and secondary buttons.
- **Ink (#07182A):** Primary text on light backgrounds.
- **Cloud (#F5F8FB):** Light page background, used sparingly to create contrast after dark cinematic sections.
- **White (#FFFFFF):** High-emphasis text and light card surfaces.
- **Text on Dark (#F6FBFF):** Main text on dark surfaces.
- **Muted on Dark (#AAB9C8):** Secondary text on dark surfaces.
- **Muted on Light (#64758A):** Secondary text on light surfaces.
- **Action Blue (#1178FF) and Action Cyan (#18C7FF):** Primary action, links, route glows, progress, sport-tech energy.
- **Impact Emerald (#1BCF8F) and Impact Mint (#68F2B9):** Giving, successful campaign momentum, impact signals.
- **Reward Gold (#F4B743) and Reward Cream (#FFE08A):** Prize pool, memorabilia, reward moments, celebratory accents.

Use blue/cyan for action, emerald for impact, and gold for rewards. Do not introduce rainbow palettes. Never use purple/violet/lavender as a main color.

## Typography

Use Inter as the default practical production typeface until a final custom brand typeface is selected.

Headlines should be large, tight, confident, and sports-broadcast/editorial in posture. Use negative letter spacing and tight line height on desktop, but loosen slightly on mobile to avoid clipping. Body text should be calm, readable, and trust-building.

Recommended hierarchy:

- Display XL: hero headlines and major launch statements.
- Display MD: section headlines.
- Headline: card titles and product/module headings.
- Body LG: hero subheads and major explanatory copy.
- Body MD: normal content.
- Label: uppercase section labels and status chips.

## Layout

Default layout should feel cinematic and premium, not like a generic SaaS card grid.

- Use dark immersive hero sections with a dominant visual asset.
- Use light sections as relief, not as the main brand personality.
- Keep campaign-operator comprehension clear: headline, subhead, CTA, visual proof, then workflow.
- On mobile, no horizontal overflow, no clipped text, thumb-friendly CTAs, and the hero visual should remain visible when it is central to the concept.
- Recommended max content width: 1180px.
- Section padding: around 84px desktop, 56px mobile.

## Elevation & Depth

Depth should come from cinematic lighting, glows, image treatment, layered cards, and realistic shadows — not generic glassmorphism everywhere.

Use:
- Deep navy gradients.
- Blue/cyan aura behind premium 3D visuals.
- Emerald/gold pin lights for impact and rewards.
- Soft, large shadows for hero assets.
- Thin dark/light borders for product panels.
- Subtle grain or grid texture only when it makes the surface feel premium.

Avoid heavy border-only cards, default drop shadows, and fake dashboards with meaningless numbers.

## Shapes

- Buttons: pill radius.
- Product cards: 16–24px radius.
- Cinematic panels/video surfaces: 24–34px radius.
- Brand mark: rounded square, currently 10–12px radius.
- Avoid over-rounded generic SaaS blobs.

## Components

Primary CTA:
- Cyan/blue gradient or action cyan fill.
- Ink text for maximum contrast.
- Pill shape.
- 46–52px minimum height on mobile.

Secondary CTA:
- Dark translucent/elevated navy surface.
- Light text.
- Subtle border.

Hero visual:
- Dominant, premium, cinematic, and tied to the actual Sports Raise system.
- Should communicate campaign page, donation credits, game-day picks, sharing toolkit, prize pool, and impact.
- Use real generated or designed assets when CSS-only visuals are not meeting the bar.

Campaign cards and consoles:
- Must show only meaningful product concepts: campaign page, sharing assets, reward pool, donor flow, impact updates.
- Avoid fake metrics unless marked as illustrative.

## Do's and Don'ts

Do:
- Keep the fundraiser/campaign as the star.
- Use donation-first language.
- Make sharing toolkit and AI video assets feel operational, not decorative.
- Test desktop and phone screenshots before sending previews.
- Give Codex/Hermes this file before visual implementation tasks.

Don't:
- Use purple/violet/lavender.
- Use public language such as sportsbook, wagering, cash betting, cash-out, or gambling-first framing.
- Let the page become a generic fan betting page.
- Ship a landing page that looks good only on desktop.
- Use decorative icons/cards that do not explain the business.
