#Imports Bot
from .bot import *


class Bovada_Future_Game:
	def __init__(self, Start_Time, Team1, Team2, Over, Under):
		#Time
		self.Start_Time = Start_Time

		#Teams
		self.Team1 = Team1
		self.Team2 = Team2

		#O/U
		self.Over = Over
		self.Under = Under
		

