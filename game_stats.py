from pathlib import Path
import json

class GameStats: 
    """Track stats for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics"""
        self.settings = ai_game.settings
        self.reset_stats()
        # High score should never be reset.
        self.high_score = self.load_high_score()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def load_high_score(self):
        """Load saved high score"""
        path = Path('highscore.json')
        contents = path.read_text()
        highscore = json.loads(contents)
        return highscore
    