class GameStats():
	def __init__(self, ai_setings):
		self.ai_settings = ai_setings
		self.game_active = False
		self.reset_stats()
	
	def reset_stats(self):
		self.ships_left = self.ai_settings.ship_limit
		self.score = 0