# Bovada Bot 
# - written by Jacob Sutton

#--------------------------------------------------------------------- IMPORTS ---------------------------------------------------------------------#
#Imports (General)
import time

# #Bovada Imports
from .setup_controller import *



class Bet_Monitor:
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


	def Setup_(self):
		try:
			#Setup 
			self.Controller = Setup_Controller()
			self.Bot, self.conn, self.euro_tag, self.Argentina_tag, self.sk_tag, self.NBA_tag = self.Controller.Setup_()

			#Get Starting Balance
			time.sleep(.5)
			self.money = Scrape_Balance(self.Bot)
			time.sleep(.5)
			print('[Initial Balance]: {}'.format(self.money))

			#Display Games
			print("\nLive Games")
			print("---------------")

			#Identify Live Tags
			if (self.euro_tag):
				print("[Euroleague]: ")
				df = Sql_to_DF(self.conn, 'live_euro_games')
				print(df)
				self.run_euro = True

			if (self.Argentina_tag):
				print("[Argentina]: ")
				df = Sql_to_DF(self.conn, 'live_argentina_games')
				print(df)
				self.run_argen = True

			if (self.sk_tag):
				print("[South Korea]: ")
				df = Sql_to_DF(self.conn, 'live_sk_games')
				print(df)
				self.run_sk = True

			if (self.NBA_tag):
				print("[NBA]: ")
				df = Sql_to_DF(self.conn, 'live_nba_games')
				print(df)
				self.run_nba = True

			#Return
			return True
		except:
			Error_Message("Setup failed..")
			return False


	def Search_for_Live_Games(self):
		#Euroleage
		if (self.run_euro):
			Info_Message("Starting Euroleage Monitoring..")

		#Argentina
		elif (self.run_argen):
			Info_Message("Starting Argentina Monitoring..")

		#South Korea
		elif (self.run_sk):
			Info_Message("Starting SK Monitoring..")

		#NBA
		elif (self.run_nba):
			Info_Message("Starting NBA Monitoring..")

		else:
			Info_Message("No games to monitor.")
		


	def Run_Test(self):
		self.setup_status = self.Setup_()
		self.Search_for_Live_Games()

		End_Test(self.Bot)