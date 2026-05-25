# Sports Raise | Data Architecture & Account Ecosystem

This document outlines every data point collected and the specific logic for account views for both Operators and Contributors.

## 1. Persona: The Campaign Operator (President)
*The person setting up the fundraiser (Nonprofit Leader, High School Coach, Individual Organizer).*

### Data Collected (Onboarding + Settings)
| Category | Fields |
| :--- | :--- |
| **Operator Identity** | Full Name, Email, Organization Name, Contact Phone. |
| **Cause Definition** | Campaign Title, The "Mission" Story, Target Goal ($), End Date. |
| **Game-Day Mapping** | Linked Team(s), Season Schedule (API-synced), Rivalry Weeks. |
| **Prize Pool** | Reward Titles, Descriptions, Photos, "Point Cost" for redemption. |
| **Financials** | Bank Routing/Account for payout, IRS status (if 501c3). |

### The Operator View (The Control Room)
*   **Impact Overview:** Big metric showing $ Raised vs. Target + Supporter Count.
*   **Engagement Delta:** A "Game-Day Energy" graph showing how many people are making picks weekly.
*   **Live Activity Feed:** List of transactions (e.g., "John D. donated $200 and picked Riverside").
*   **Sharing Cockpit:** Shortcuts to the generated SOCIAL OVERLAYS and EMAIL TEMPLATES.
*   **Reward Vault:** Inventory tracker for prizes remaining.

---

## 2. Persona: The Contributor (The Donor)
*The supporter/fan who donates and participates.*

### Data Collected (Low-Friction Flow)
*   **Donation Event:** Amount ($), Identity (Email/Phone), Selected Matchup Pick.
*   **Payment Data:** PCI-compliant token (Stripe), Billing Zip.
*   **Account Access:** Magic Link (No password required).

### The Fan View (Supporter Dashboard)
*   **Active Pursuits:** Tabbable view of all current campaigns they support.
*   **Credit Wallet:** Real-time point balance across all campaigns.
*   **The Locker:** A list of "My Picks" for the upcoming weekend.
*   **Impact Gallery:** "Your giving provided [20 meals / 5 jerseys]" — translating $ into meaning.

---

## 3. Database Schema (Draft)

### table: Users
- id (UUID)
- role (operator | fan)
- email (unique)
- phone
- name
- avatar_url
- stripe_customer_id

### table: Campaigns
- id (UUID)
- operator_id (FK)
- title
- story_markdown
- goal_amount
- raised_amount
- status (active | completed)

### table: Contributions
- id (UUID)
- campaign_id (FK)
- user_id (FK)
- amount
- credits_granted
- matchup_pick
- timestamp

### table: Rewards
- id (UUID)
- campaign_id (FK)
- title
- credit_cost
- stock_count
- image_url

### table: Pick_Outcomes
- id (UUID)
- contribution_id (FK)
- points_awarded
- result (won | lost)
