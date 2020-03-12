# Bovada Bot 
# - written by Jacob Sutton

#--------------------------------------------------------------------- IMPORTS ---------------------------------------------------------------------#
#Imports (General)
import time

#Bovada Imports
from .Build.__init__ import *
from .Bovada.__init__ import *
from .Database.__init__ import *
from .actions import Create_Euroleague_Schedule, Create_Argentina_Schedule, Create_SK_Schedule, Create_NBA_Schedule, Update_Live_Games_






class Live_Game_Session:
	def __init__(self, Bot, DB, Time, Quarter, Team1, Team2, Over, Over_Bet, Under, Under_Bet, Score1, Score2, game_id):
		#Initialization
		self.Bot = Bot
		self.conn = DB
		self.game_id = game_id

		#Time
		self.Time = Time
		self.Quarter = Quarter

		#Teams
		self.Team1 = Team1
		self.Team2 = Team2

		#O/U
		self.Init_Over = Over
		self.Init_Under = Under
		self.Over_Bet = Over_Bet
		self.Under_Bet = Under_Bet
		self.current_over = None
		self.current_under = None

		#Score
		self.Score1 = Score1
		self.Score2 = Score2

		#Bet
		self.make_bet = None
		self.select_bet = None

		#Run
		if (self.Check_Bet_Availablity()):
			self.Watch_Game()
		else:
			return "inactive"


	def Check_Bet_Availablity(self):
		#Look at Time
		return False


	def Make_Bet(self, over_under):
		#Select over under
		self.select_bet = Select_Over_Under(self.Bot, self.game_id, over_under)

		#Make Bet
		self.make_bet = Make_Bet(self.Bot)


	def Watch_Game(self):
		while (1):
			#Grab the current values
			Update_Live_Games_('temp_live_games')

			#Create DF
			df = Sql_to_DF(self.conn, 'temp_live_games')
			self.current_over = df['Over'][self.game_id]
			self.current_under = df['Under'][self.game_id]

			#Check if Bet can be made
			#Over
			if (self.current_over >= self.Over_Bet):
				self.Make_Bet('over')
				break

			#Under
			elif(self.current_under <= self.Under_Bet):
				self.Make_Bet('under')
				break

			else:
				#Wait
				time.sleep(1)




class Game_Controller:
	def __init__(self, Bot, DB):
		#Initialize
		self.Bot = Bot
		self.conn = DB

		#Time
		self.Start_Time = time.time()

		#Games
		self.Games = []

	def Create_Game_Session(self, Time, Quarter, Team1, Team2, Over, Over_Bet, Under, Under_Bet, Score1, Score2, game_id):
		game = Live_Game_Session(self.Bot, self.conn, Time, Quarter, Team1, Team2, Over, Over_Bet, Under, Under_Bet, Score1, Score2, game_id)

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
			game_id = game

			#Create Game Session
			self.Create_Game_Session(t,q,t1,t2,o,o_b,u,u_b,s1,s2, game_id)

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


