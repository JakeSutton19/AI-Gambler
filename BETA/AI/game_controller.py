# Bovada Bot 
# - written by Jacob Sutton

#--------------------------------------------------------------------- IMPORTS ---------------------------------------------------------------------#
#Imports (General)
import time

#Bovada Imports
from .Build.__init__ import *
from .Bovada.__init__ import *
from .Database.__init__ import *



class Game_Controller:
	def __init__(self, Bot, DB):
		#Initialize
		self.Bot = Bot
		self.conn = DB

		#Time
		self.Start_Time = time.time()

		#Games
		self.Games = []

	def Create_Game_Session(self, Time, Quarter, Team1, Team2, Over, Over_Bet, Under, Under_Bet, Score1, Score2):
		game = Live_Game_Session(Time, Quarter, Team1, Team2, Over, Over_Bet, Under, Under_Bet, Score1, Score2)

		self.Games.append(game)


	def Create_EUR_Monitor(self):
		#Create DF
		df = Sql_to_DF(self.conn, 'live_euro_games')

		#Find Length and iterate through each row
		for game in len(df):
			t = df['Time'][game]
			q = df['Quarter'][game]
			t1 = df['Team1'][game]
			t2 = df['Team2'][game]
			o = df['Over'][game]
			o_b = df['Over_Bet'][game]
			u = df['Under'][game]
			u_b = df['Under_Bet'][game]
			s1 = df['Score1'][game]
			s2 = df['Score2'][game]

			#Create Game Session
			self.Create_Game_Session(t,q,t1,t2,o,o_b,u,u_b,s1,s2)

		#Return Game list
		return self.Games

	def Create_ARG_Monitor(self):
		#Create DF
		df = Sql_to_DF(self.conn, 'live_argentina_games')

		#Find Length and iterate through each row
		for game in len(df):
			t = df['Time'][game]
			q = df['Quarter'][game]
			t1 = df['Team1'][game]
			t2 = df['Team2'][game]
			o = df['Over'][game]
			o_b = df['Over_Bet'][game]
			u = df['Under'][game]
			u_b = df['Under_Bet'][game]
			s1 = df['Score1'][game]
			s2 = df['Score2'][game]

			#Create Game Session
			self.Create_Game_Session(t,q,t1,t2,o,o_b,u,u_b,s1,s2)

		#Return Game list
		return self.Games

	def Create_SK_Monitor(self):
		#Create DF
		df = Sql_to_DF(self.conn, 'live_sk_games')

		#Find Length and iterate through each row
		for game in len(df):
			t = df['Time'][game]
			q = df['Quarter'][game]
			t1 = df['Team1'][game]
			t2 = df['Team2'][game]
			o = df['Over'][game]
			o_b = df['Over_Bet'][game]
			u = df['Under'][game]
			u_b = df['Under_Bet'][game]
			s1 = df['Score1'][game]
			s2 = df['Score2'][game]

			#Create Game Session
			self.Create_Game_Session(t,q,t1,t2,o,o_b,u,u_b,s1,s2)

		#Return Game list
		return self.Games

	def Create_NBA_Monitor(self):
		#Create DF
		df = Sql_to_DF(self.conn, 'live_nba_games')

		#Find Length and iterate through each row
		for game in len(df):
			t = df['Time'][game]
			q = df['Quarter'][game]
			t1 = df['Team1'][game]
			t2 = df['Team2'][game]
			o = df['Over'][game]
			o_b = df['Over_Bet'][game]
			u = df['Under'][game]
			u_b = df['Under_Bet'][game]
			s1 = df['Score1'][game]
			s2 = df['Score2'][game]

			#Create Game Session
			self.Create_Game_Session(t,q,t1,t2,o,o_b,u,u_b,s1,s2)

		#Return Game list
		return self.Games


class Live_Game_Session:
	def __init__(self, Time, Quarter, Team1, Team2, Over, Over_Bet, Under, Under_Bet, Score1, Score2):
		#Time
		self.Time = Time
		self.Quarter = Quarter

		#Teams
		self.Team1 = Team1
		self.Team2 = Team2

		#O/U
		self.Over = Over
		self.Under = Under
		self.Over_Bet = Over_Bet
		self.Under_Bet = Under_Bet

		#Score
		self.Score1 = Score1
		self.Score2 = Score2
