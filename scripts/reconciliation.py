import os
import json
import datetime

# Root logic for Sports Raise 1:1 Payout Reconciliation
class ReconciliationEngine:
    def __init__(self, user_id):
        self.user_id = user_id
        self.vig_rate = 0.0  # Mandate: No vig, 1:1 payout

    def process_win(self, amount):
        """
        Reconciles a winning contribution (boost).
        Formula: Original Contribution + (Contribution * 1)
        """
        payout = amount * 2
        print(f"DEBUG: Processing Win for {self.user_id} | Amount: {amount} | Payout: {payout}")
        return payout

    def process_loss(self, amount):
        """
        Reconciles a losing contribution.
        User retains only the impact, but credits are removed.
        """
        print(f"DEBUG: Processing Loss for {self.user_id} | Credits Deducted: {amount}")
        return 0

# Kickoff Lockout Logic
def is_locked(game_start_time_iso):
    now = datetime.datetime.now(datetime.timezone.utc)
    start_time = datetime.datetime.fromisoformat(game_start_time_iso)
    return now >= start_time

if __name__ == "__main__":
    # Smoke Test
    engine = ReconciliationEngine("User_8622")
    assert engine.process_win(100) == 200
    assert engine.process_loss(100) == 0
    print("RECONCILIATION_LOGIC: PASS")
