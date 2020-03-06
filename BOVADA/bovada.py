# Bovada Bot 
# - written by Jacob Sutton

#--------------------------------------------------------------------- IMPORTS ---------------------------------------------------------------------#
#Imports (General)
import time

#Bovada Imports
from Build.__init__ import *
from Bet.__init__ import *
from Data.__init__ import *
# from DB.__init__ import *





#Bovada Controller
class Controller:
	def __init__(self):
		#Bot
		self.Bot = None
		self.create_bot = None

		#Bovada
		self.bovada_login = None

		#Navigation
		self.bovada_basketball_home = None
		self.navigate = None

		#Data
		self.success_scrape = None
		self.create_schedule = None
		self.schedule = None
		

	#Setup the Bot
	def Setup_Bot(self):
		try:
			self.Bot, self.create_bot = Create_Bot()
			return True 
		except:
			Error_Message("Unable to Setup_Bot")
			return False


	#Setup Bovada home
	def Setup_Bovada(self):
		#Login to Bovada
		try:
			self.bovada_login = Bovada_Quick_Login(self.Bot) #Login
			return True 
		except:
			Error_Message("Unable to Setup_Bovada")
			return False


	#Betting Monitor
	def Setup_Basketball_Home(self):
		try:
			#Navigate to Basketball Home
			self.bovada_basketball_home = Nav_to_Basketball_Page(self.Bot)
			time.sleep(1)
			return True 
		except:
			Error_Message("Unable to Setup_Basketball_Home")
			return False


	#Euroleague Schedule
	def Create_Euroleague_Schedule(self):
		try:
			#Navigate to Basketball Home
			self.navigate = Nav_to_Euroleague_Page(self.Bot)
			time.sleep(1)

			#Scrape the Page
			future_games, self.success_scrape = Create_Future_Games_List(self.Bot)

			#Format and Save to CSV
			self.create_schedule = Create_Future_Games_CSV(self.Bot, future_games, 'EUROLEAGUE_PATH')

			#Return
			return True 
		except:
			Error_Message("Unable to Create_Euroleague_Schedule")
			return False
		

	#Argentina Schedule
	def Create_Argentina_Schedule(self):
		try:
			#Navigate to Basketball Home
			self.navigate = Nav_to_Argentina_Page(self.Bot)
			time.sleep(1)

			#Scrape the Page
			# future_games, self.success_scrape = Create_Future_Games_List(self.Bot)
			live_games = Create_Live_Games_List(self.Bot)

			#Format and Save to CSV
			# self.create_schedule = Create_Future_Games_CSV(self.Bot, future_games, 'ARGENTINA_PATH')
			update_live_games = Create_Live_Games_CSV(self.Bot, live_games, 'ARGENTINA_PATH')

			gam = Read_Live_Games_CSV(self.Bot, 'ARGENTINA_PATH')
			print(gam)

			#Return
			return True 
		except:
			Error_Message("Unable to Create_Argentina_Schedule")
			return False


	#Argentina Schedule
	def Create_SK_Schedule(self):
		try:
			#Navigate to Basketball Home
			self.navigate = Nav_to_SK_Page(self.Bot)
			time.sleep(1)

			#Scrape the Page
			future_games, self.success_scrape = Create_Future_Games_List(self.Bot)

			#Format and Save to CSV
			self.create_schedule = Create_Future_Games_CSV(self.Bot, future_games, 'SK_PATH')

			#Return
			return True 
		except:
			Error_Message("Unable to Create_SK_Schedule")
			return False


	def Run(self):
		#Start Bot
		self.Setup_Bot()

		#Setup Bovada
		if (self.create_bot):
			self.Setup_Bovada()

		#Setup Basketball Monitoring
		if (self.bovada_login):
			self.Setup_Basketball_Home()

		#Test
		if (self.bovada_basketball_home):
			self.Create_Argentina_Schedule()
			
			

		End_Test(self.Bot)
