# Codex brief — landing page typography quick change

Task: update `/root/projects/sports-raise/landing-page.html` typography so the large bold headline/display font no longer has overly tight letter spacing or characters touching.

Context:
- User specifically asked to delegate one quick change to Codex.
- Current large display headline is too tightly tracked; minimum goal is more normal letter spacing.
- Keep Sports Raise premium sports-tech feel and existing content/sections.
- Do not redesign the page or change layout/hero/logo.
- Do not commit.

Requirements:
1. In `landing-page.html`, change the large display headline typography to a more readable, less compressed style.
2. At minimum, reduce extreme negative letter spacing on `h1`, `h2`, and any display-like headline selectors.
3. Prefer values around `-0.025em` to `-0.035em` for large display and closer to `-0.015em` for smaller headings.
4. Increase line-height slightly if needed so descenders/ascenders do not visually collide, especially on mobile.
5. If adding a web font, keep it stable and lightweight; otherwise use system/Inter stack. Do not add fragile dependencies.
6. Preserve mobile responsiveness and no horizontal clipping.
7. Leave logo/assets/docs alone except this brief.

Verification to run/enable:
- Check local page returns 200.
- Generate/inspect desktop and mobile screenshots if possible.
- Search source for very tight values like `letter-spacing: -.07em`, `-.065em`, `-.055em` and normalize them.
