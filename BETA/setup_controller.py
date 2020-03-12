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



#Bovada Controller
class Setup_Controller:
	def __init__(self):
		#Bot
		self.Bot = None
		self.create_bot = None

		#Bovada
		self.bovada_login = None
		self.bovada_login_check = None

		#Navigation
		self.bovada_basketball_home = None
		self.navigate = None

		#Data
		self.success_scrape = None
		self.create_schedule = None
		self.schedules = None
		self.live_error_count = 0
		self.future_error_count = 0

		#DB
		self.conn = None
		self.db_path = '/home/human/AI-Gambler/CONFIG/Data/Databases/test.db'

		#Tags
		self.euro_tag = None
		self.Argentina_tag = None
		self.sk_tag = None
		self.NBA_tag = None
		

	#Setup the Bot
	def Setup_Bot(self):
		try:
			self.Bot, self.create_bot = Create_Bot()
			return True 
		except:
			Error_Message("Unable to Setup_Bot")
			return False

	def Setup_DB(self):
		#Connect to DB
		self.conn = Bovada_DB(self.db_path)


	#Check login status
	def Check_Bovada_Login(self):
		try:
			#Get Starting Balance
			time.sleep(1.5)
			money = Scrape_Balance(self.Bot)

			#if balace is false, manual login
			if (money):
				Info_Message("Quick login successful.")
				return True 
			else:
				Info_Message("Quick login failed. Running manual setup..")
				self.bovada_login = Bovada_Setup_Login(self.Bot)
				return True
		except:
			Error_Message("Unable to Check_Bovada_Login")
			return False


	#Setup Bovada home
	def Setup_Bovada(self):
		try:
			#Login to Bovada
			Info_Message("Setting up Bovada.")
			self.bovada_login = Bovada_Quick_Login(self.Bot) #Login

			#Check for login
			self.bovada_login_check = self.Check_Bovada_Login()
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


	#Create Game Schedules
	def Make_Schedules(self):
		Info_Message("Generating schedules.")
		try:
			self.live_error_count, self.future_error_count, self.euro_tag = Create_Euroleague_Schedule(self.Bot, self.conn, self.live_error_count, self.future_error_count) #Euro
			self.live_error_count, self.future_error_count, self.Argentina_tag = Create_Argentina_Schedule(self.Bot, self.conn, self.live_error_count, self.future_error_count) #Argentina
			self.live_error_count, self.future_error_count, self.sk_tag = Create_SK_Schedule(self.Bot, self.conn, self.live_error_count, self.future_error_count) #Korea
			self.live_error_count, self.future_error_count, self.NBA_tag = Create_NBA_Schedule(self.Bot, self.conn, self.live_error_count, self.future_error_count) #NBA

			#Handle Tables
			live_count = 4 - self.live_error_count
			future_count = 4 - self.future_error_count

			#Return
			return True
		except:
			Error_Message("Unable to Make_Schedules")
			return False


	def Setup_(self):
		#Message
		print("SETUP LOG")
		print("---------")
		Info_Message("Creating Bot.")

		#Start Bot
		self.Setup_Bot()

		#Connect DB
		self.Setup_DB()

		#Setup Bovada
		if (self.create_bot):
			self.Setup_Bovada()

		#Setup Basketball Monitoring
		if (self.bovada_login):
			self.Setup_Basketball_Home()
			
		#Create schedules
		if (self.bovada_basketball_home):
			self.Make_Schedules()

		#Export Details
		return self.Bot, self.conn, self.euro_tag, self.Argentina_tag, self.sk_tag, self.NBA_tag
		