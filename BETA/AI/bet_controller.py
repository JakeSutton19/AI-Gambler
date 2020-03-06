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


	def Setup_(self):
		try:
			#Setup 
			self.Controller = Setup_Controller()
			self.Bot, self.conn, self.euro_tag, self.Argentina_tag, self.sk_tag, self.NBA_tag = self.Controller.Setup_()

			#Get Starting Balance
			time.sleep(.5)
			self.money = Scrape_Balance(self.Bot)
			time.sleep(.5)

			#Identify Live Tags
			if (self.euro_tag):
				self.run_euro = True

			if (self.Argentina_tag):
				self.run_argen = True

			if (self.sk_tag):
				self.run_sk = True

			if (self.NBA_tag):
				self.run_nba = True

			#Return
			Info_Message("Setup complete.")
			return True
		except:
			Error_Message("Setup failed..")
			return False

	def Show_Live_Games(self):
		#Identify Live Tags
		if (self.run_euro):
			print("\nLive Games - Euroleague: ")
			print("---------------")
			df = Sql_to_DF(self.conn, 'live_euro_games')
			print(df)

		elif (self.run_argen):
			print("\nLive Games - Argentina: ")
			print("---------------")
			df = Sql_to_DF(self.conn, 'live_argentina_games')
			print(df)

		elif (self.run_sk):
			print("\nLive Games - South Korea: ")
			print("---------------")
			df = Sql_to_DF(self.conn, 'live_sk_games')
			print(df)

		elif (self.run_nba):
			print("\nLive Games - NBA: ")
			print("---------------")
			df = Sql_to_DF(self.conn, 'live_nba_games')
			print(df)


	def Search_for_Live_Games(self):
		#Euroleage
		if (self.run_euro):
			Info_Message("Starting Euroleage Monitoring..")
			self.Run_EUR_Monitor()

		#Argentina
		elif (self.run_argen):
			Info_Message("Starting Argentina Monitoring..")
			self.Run_ARG_Monitor()

		#South Korea
		elif (self.run_sk):
			Info_Message("Starting SK Monitoring..")
			self.Run_SK_Monitor()

		#NBA
		elif (self.run_nba):
			Info_Message("Starting NBA Monitoring..")
			self.Run_NBA_Monitor()

		else:
			Info_Message("No games to monitor.")
			print("Closing session..")
			time.sleep(2)
			Error_Quit(self.Bot)


	def Run_EUR_Monitor(self):
		#Create the Controller
		self.eur_controller = Game_Controller(self.Bot, self.conn)

		#Create NBA Monitor
		self.live_eur_games = self.eur_controller.Create_EUR_Monitor()

		#Return
		print(len(self.live_eur_games))


	def Run_ARG_Monitor(self):
		#Create the Controller
		self.arg_controller = Game_Controller(self.Bot, self.conn)

		#Create NBA Monitor
		self.live_arg_games = self.arg_controller.Create_ARG_Monitor()

		#Return
		print(len(self.live_arg_games))


	def Run_SK_Monitor(self):
		#Create the Controller
		self.sk_controller = Game_Controller(self.Bot, self.conn)

		#Create NBA Monitor
		self.live_sk_games = self.sk_controller.Create_SK_Monitor()

		#Return
		print(len(self.live_sk_games))


	def Run_NBA_Monitor(self):
		#Create the Controller
		self.nba_controller = Game_Controller(self.Bot, self.conn)

		#Create NBA Monitor
		self.live_nba_games = self.nba_controller.Create_NBA_Monitor()

		#Return
		print(len(self.live_nba_games))
		


	def Run(self):
		self.setup_status = self.Setup_()
		self.Show_Live_Games()
		self.Search_for_Live_Games()