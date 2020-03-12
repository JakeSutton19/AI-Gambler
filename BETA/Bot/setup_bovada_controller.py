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
class Setup_Bovada_Controller:
	def __init__(self, Bot, DB, Controller_Status):
		#Initialize
		self.Bot = Bot
		self.conn = DB
		self.controller = Controller_Status

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

		#Tags
		self.euro_tag = None
		self.Argentina_tag = None
		self.sk_tag = None
		self.NBA_tag = None

		#Setup_
		self.Setup_Bovada()
		

	#Check login status
	def Check_Bovada_Login(self):
		try:
			#Get Starting Balance
			time.sleep(1.5)
			money = Scrape_Balance(self.Bot)

			#if balace is false, manual login
			if (money):
				# Info_Message("Quick login successful.")
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
			# Info_Message("Setting up Bovada.")
			self.bovada_login = Bovada_Quick_Login(self.Bot) #Login

			#Check for login
			self.bovada_login_check = self.Check_Bovada_Login()
		except:
			Error_Message("Unable to Setup_Bovada")
			return False

	#Setup Bovada
	def Setup_(self):
		#Setup Bovada
		if (self.controller):
			self.Setup_Bovada()


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

	
	#Setup BB monitoring
	def Initialize_Basketball_Games(self):
		#Setup Basketball Monitoring
		if (self.bovada_login_check):
			self.Setup_Basketball_Home()
			
		#Create schedules
		if (self.bovada_basketball_home):
			self.Make_Schedules()

		#Export Details
		return self.euro_tag, self.Argentina_tag, self.sk_tag, self.NBA_tag
		