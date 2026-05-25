# Sports Raise

Sports Raise is a donation-first sports engagement platform that helps campaign operators turn game-day energy into repeat contributions for causes.

## Current status

This repo currently contains the landing-page prototype, brand/design system foundations, and planning docs for the Sports Raise product.

## Key files

- `landing-page.html` — current standalone landing page prototype.
- `DESIGN.md` — machine-readable design system / brand token spec for Hermes, Codex, and future implementation work.
- `assets/sports-raise-3d-hero.png` — current premium 3D hero asset.
- `docs/brand-kit.md` — working brand kit and logo direction.
- `docs/project-brief.md` — concise project context.
- `docs/roadmap.md` — phased roadmap.
- `docs/site-architecture.md` — product/site architecture skeleton.

## Product docs

- `docs/campaign-builder.md`
- `docs/sharing-toolkit.md`
- `docs/ai-video-assets.md`
- `docs/admin-ops.md`
- `docs/donor-flow.md`
- `docs/rewards-prize-pool.md`

## Brand guardrails

Use public-facing language:
- game-day action
- picks
- predictions
- challenges
- non-cash credits
- donated rewards
- prize pool
- leaderboards
- campaign play
- impact

Avoid public-facing language:
- sportsbook
- wagering
- cash betting
- cash-out
- gambling-first framing

Visual guardrail: no purple/violet/lavender as main brand colors.

## Agent workflow

Hermes acts as project manager/orchestrator. Codex or subagents can implement scoped tasks using `DESIGN.md`, `docs/project-brief.md`, and task-specific docs as context.

Before sending previews, verify:
- desktop visual QA
- mobile visual QA
- public preview HTTP 200
- no banned public terms/colors
