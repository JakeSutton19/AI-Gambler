# Bovada Bot 
# - written by Jacob Sutton

#--------------------------------------------------------------------- IMPORTS ---------------------------------------------------------------------#
#Imports (General)
import time

#Bovada Imports
from .Build.__init__ import *
from .Bovada.__init__ import *
from .Database.__init__ import *
from .actions import Create_Euroleague_Schedule, Create_Argentina_Schedule, Create_SK_Schedule, Create_NBA_Schedule
from .setup_controller import Setup_Controller
from .game_controller import Game_Controller, Live_Game_Session


class Bet_Controller:
	def __init__(self):
		#Bot
		self.Bot = None

		#DB
		self.conn = None

		#Controller
		self.Controller = None

		#Tags
		self.euro_tag = None
		self.Argentina_tag = None
		self.sk_tag = None
		self.NBA_tag = None

		#Status
		self.setup_status = None

		#Monitor Direction
		self.run_euro = None
		self.run_argen = None
		self.run_sk = None
		self.run_nba = None

		#Betting
		self.money = None

		#NBA
		self.eur_controller = None
		self.live_eur_games = None

		#NBA
		self.arg_controller = None
		self.live_arg_games = None

		#NBA
		self.sk_controller = None
		self.live_sk_games = None

		#NBA
		self.nba_controller = None
		self.live_nba_games = None


	def Search_for_Live_Games(self):
		#Euroleage
		if (self.run_euro):
			self.Run_EUR_Monitor()

		#Argentina
		elif (self.run_argen):
			self.Run_ARG_Monitor()

		#South Korea
		elif (self.run_sk):
			self.Run_SK_Monitor()

		#NBA
		elif (self.run_nba):
			self.Run_NBA_Monitor()

		else:
			Info_Message("No games to monitor.")
			print("Closing session..")
			time.sleep(2)
			Error_Quit(self.Bot)


	def Run_EUR_Monitor(self):
		Info_Message("Starting Euroleage Monitoring..")


	def Run_ARG_Monitor(self):
		Info_Message("Starting Argentina Monitoring..")

		#Live Games
		print("\nLive Games - Argentina: ")
		print("---------------")
		df = Sql_to_DF(self.conn, 'live_argentina_games')
		print(df)

		#Go to Game
		Nav_to_Argentina_Page(self.Bot)

		
	def Run_SK_Monitor(self):
		Info_Message("Starting SK Monitoring..")


	def Run_NBA_Monitor(self):
		Info_Message("Starting NBA Monitoring..")

		