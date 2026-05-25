import json
import os
from datetime import datetime, timezone

# Mock provider for NFL matchups
class NFLMockProvider:
    def __init__(self):
        self.source = "NFL_MOCK_API"
        
    def fetch_matchups(self):
        """
        Returns a list of mock NFL matchups for the current week.
        In a real scenario, this would call an external API (e.g., ESPN, OddsAPI).
        """
        # Week 1-4 sample data
        return [
            {
                "id": "nfl_2026_w1_kc_bal",
                "league": "NFL",
                "week": 1,
                "home_team": "Kansas City Chiefs",
                "away_team": "Baltimore Ravens",
                "start_time": "2026-09-10T20:20:00Z",
                "odds": {
                    "home_ml": -150,
                    "away_ml": +130,
                    "spread": -3.0,
                    "over_under": 46.5
                },
                "status": "scheduled",
                "dynamics": {
                    "pot": 12500,
                    "boosters": 42
                }
            },
            {
                "id": "nfl_2026_w1_phi_gb",
                "league": "NFL",
                "week": 1,
                "home_team": "Philadelphia Eagles",
                "away_team": "Green Bay Packers",
                "start_time": "2026-09-11T20:15:00Z",
                "odds": {
                    "home_ml": -110,
                    "away_ml": -110,
                    "spread": -1.0,
                    "over_under": 48.0
                },
                "status": "scheduled",
                "dynamics": {
                    "pot": 8200,
                    "boosters": 29
                }
            }
        ]

def sync_matchups():
    provider = NFLMockProvider()
    matchups = provider.fetch_matchups()
    
    data_path = "/root/projects/sports-raise/data/matchups.json"
    
    # Load existing or start fresh
    if os.path.exists(data_path):
        with open(data_path, 'r') as f:
            existing = json.load(f)
    else:
        existing = []
        
    # Simple merge logic (update if ID matches, else append)
    existing_ids = {m['id'] for m in existing}
    
    for m in matchups:
        if m['id'] in existing_ids:
            # Update existing entry
            for i, item in enumerate(existing):
                if item['id'] == m['id']:
                    existing[i].update(m)
                    break
        else:
            existing.append(m)
            
    with open(data_path, 'w') as f:
        json.dump(existing, f, indent=2)
    
    return len(matchups)

if __name__ == "__main__":
    count = sync_matchups()
    print(f"Synced {count} NFL matchups.")
