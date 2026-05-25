# Sports Raise | Product Architecture & User Experience (v1)

## 1. The Core Architecture

The system is designed as a **multi-funnel platform** that bridges donors (fans) and organizers (nonprofits).

### A. Public Marketing Funnel (current work)
*   **Target:** Campaign Operators (Nonprofits / Individuals).
*   **Goal:** Conversion to "Start a Pilot."
*   **Key Surface:** `landing-page.html` (The "pitch" for the system).

### B. Campaign Operator System (The "Control Room")
*   **Target:** The person running the fundraiser.
*   **Surfaces:**
    *   **Onboarding:** Step-by-step setup (Cause title, story, target goal, donation tiers).
    *   **Reward Manager:** Repository of donated prizes/memorabilia.
    *   **Content Factory:** Sharing toolkit (One-click social posts, email templates).
    *   **AI Video Center:** 15–30s reels generator (Narrates the cause + game-day matchup).
    *   **Impact Console:** Dashboard showing total raised vs. goal + supporter leaderboard.

### C. Supporter Experience (The "Star of the Show")
*   **Target:** Fans, Alumni, Local Supporters.
*   **Goal:** Conversion: Donate -> Participate -> Share.
*   **Key Surface: The Campaign Page.**
    *   **Header:** Cause Branding (Sports Raise "Powered By").
    *   **Story Block:** Why we are raising money.
    *   **Engagement Widget:** Live "Matchup of the Week" + Pick options.
    *   **Reward Gallery:** What you can win with your credits.
*   **Secondary Surface: Fan Dashboard.**
    *   Login-less (magic link/email) view of "My Credits" and "My Picks."

---

## 2. The User Experience Flow (Happy Path)

1.  **Step 1: Onboarding.** Operator lands on Sports Raise, clicks "Start Pilot," and enters basic cause info.
2.  **Step 2: Setup.** Operator defines the reward pool (e.g., "Signed Jersey," "VIP Dinner") and links the upcoming football schedule.
3.  **Step 3: Promotion.** Operator uses the **Sharing Toolkit** to blast the campaign to their list.
4.  **Step 4: Contribution.** Supporter lands on the Campaign Page, donates $100, and instantly receives 100 Credits.
5.  **Step 5: Engagement.** Supporter uses Credits to "Pick the Winner" of Saturday's game.
6.  **Step 6: Realization.** Post-game, Supporters see if they won rewards, receive an "Impact Update" (e.g., "Your $100 just bought 20 jerseys for the team"), and are prompted to share the result.

---

## 3. Immediate Implementation Priorities

| Module | Priority | Status |
| :--- | :--- | :--- |
| **Landing Page** | High | Complete (Redesign phase) |
| **Branding Kit** | High | Concepts created; need selection |
| **Sharing Toolkit** | Critical | Drafting HTML/CSS templates now |
| **Campaign Page** | Critical | Designing next (most important individual surface) |
| **AI Video Engine** | Medium | Scripted foundation in place |
