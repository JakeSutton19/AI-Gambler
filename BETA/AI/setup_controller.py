# Bovada Bot 
# - written by Jacob Sutton

#--------------------------------------------------------------------- IMPORTS ---------------------------------------------------------------------#
#Imports (General)
import time

# #Bovada Imports
from .actions import *



#Bovada Controller
class Setup_Controller:
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

		#DB
		self.conn = None
		self.db_path = '/home/human/AI-Gambler/CONFIG/Data/Databases/test.db'
		

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

		# #Create Tables
		# create_future_games_table(self.conn)


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


	#Create Game Schedules
	def Make_Schedules(self):
		try:
			# Create_Euroleague_Schedule(self.Bot, self.conn) #Euro
			# Create_Argentina_Schedule(self.Bot, self.conn) #Argentina
			# Create_SK_Schedule(self.Bot, self.conn) #Korea
			Create_NBA_Schedule(self.Bot, self.conn) #NBA
			return True 
		except:
			Error_Message("Unable to Make_Schedules")
			return False

	


	def Run(self):
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
		self.Make_Schedules()

		#Read for SQL
		df1 = Sql_to_DF(self.conn, 'live_nba_games')
		print(df1)
		

		End_Test(self.Bot)
