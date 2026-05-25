import unittest
import os
import json
from server.providers.nfl_provider import NFLMockProvider, sync_matchups

class TestNFLProvider(unittest.TestCase):
    def setUp(self):
        self.test_data_path = "/root/projects/sports-raise/data/matchups.json"
        # Backup existing matchups if any
        self.backup = None
        if os.path.exists(self.test_data_path):
            with open(self.test_data_path, 'r') as f:
                self.backup = json.load(f)

    def tearDown(self):
        # Restore backup
        if self.backup:
            with open(self.test_data_path, 'w') as f:
                json.dump(self.backup, f, indent=2)

    def test_mock_fetch(self):
        provider = NFLMockProvider()
        matchups = provider.fetch_matchups()
        self.assertEqual(len(matchups), 2)
        self.assertEqual(matchups[0]['home_team'], "Kansas City Chiefs")

    def test_sync(self):
        # Run sync and check file
        count = sync_matchups()
        self.assertGreater(count, 0)
        
        with open(self.test_data_path, 'r') as f:
            data = json.load(f)
            ids = [m['id'] for m in data]
            self.assertIn("nfl_2026_w1_kc_bal", ids)

if __name__ == "__main__":
    unittest.main()
