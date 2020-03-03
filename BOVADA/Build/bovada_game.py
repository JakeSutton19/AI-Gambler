#Imports Bot
from .bot import *


class Bovada_Game:
	def __init__(self, Team1, Team2, Over, Under):
		#Teams
		self.Team1 = Team1
		self.Team2 = Team2

		#O/U
		self.Over = Over
		self.Under = Under
		
		#Score
		self.Score1 = None
		self.Score2 = None

		#Time
		self.Game_Time = None
		self.Start_Time = None
		self.Current_Time = None
		self.Quarter = None

		#Status
		self.status = None

		#Bet
		self.new_bet_possible = None
		self.bet_made = None
		self.bet_result = None