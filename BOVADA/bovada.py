#Imports (General)
import time

#Imports (Build)
from Build.__init__ import *




class Bovada_Controller:
	def __init__(self, Bot):
		#Initialize
		self.Bot = Bot

		#Status
		self.login_successful = None
		self.Nav_successful = None
		self.Scrape_Live = None
		self.Scrape_Future = None


	def Game_Monitoring(self):
		if (self.Scrape_Live == False):
			data_df = Read_Future_Games_CSV(self.Bot)




	def Setup(self):
		#Create Bot
		self.Bot = Bot()

		#LogIn to Bovada
		try:
			Bovada_Quick_Login(self.Bot)
			self.login_successful = True
		except:
			print("[ERROR]: Unable to Bovada_Quick_Login. Attempt Manual Login")
			self.login_successful = False


		#Go to Basketball Page
		try:
			Nav_to_Basketball_Page(self.Bot)
			self.Nav_successful = True
		except:
			print("[ERROR]: Unable to Nav_to_Basketball_Page.")
			self.Nav_successful = False


		#Scrape Live Games
		try:
			live_games = Create_Live_Games_List(self.Bot)
			self.Scrape_Live = True
		except:
			print("[ERROR]: Unable to Create_Live_Games_List.")
			self.Scrape_Live = False


		#Check Data Status
		if (self.Scrape_Live == False):
			try:
				#Scrape Future Data
				future_games = Create_Future_Games_List(self.Bot)
				self.Scrape_Future = True
			except:
				print("[ERROR]: Unable to Create_Future_Games_List.")
				self.Scrape_Future = False
			#Create CSV
			try:
				Create_Future_Games_CSV(self.Bot, future_games)
			except:
				print("[ERROR]: Unable to Create_Future_Games_CSV.")
		else:
			#Create CSV
			try:
				Create_Live_Games_CSV(self.Bot, live_games)
			except:
				print("[ERROR]: Unable to Create_Live_Games_CSV.")
			



def Test_Run(Bot):
	# Bovada_Quick_Login(Bot)
	# Nav_to_Basketball_Page(Bot)
	# games = Create_Future_Games_List(Bot)
	data = Read_Future_Games_CSV(Bot)
	print(data["Over"][1])
	End_Test(Bot)


Bovada = Bot()
Test_Run(Bovada)






