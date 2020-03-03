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





def Run(Bot):
	#Status
	bet_count = 0

	#Setup
	Bovada_Quick_Login(Bot) #Login 
	Nav_to_Basketball_Page(Bot) #Go to Basketball Page

	#Data Collecting
	schedule = Create_Future_Games_List(Bot) 

	#Create Future Game List
	Create_Future_Games_CSV(Bot, schedule)

	#Store Initial Values and create what to Compare
	Init_Games_DF = Read_Future_Games_CSV(Bot)

	#Monitor Games
	while 1:
		#Index
		index = 0

		#Pull latest data
		update = Create_Future_Games_List(Bot)
		update_df = Create_DF(update)

		#Look at each game O/U
		for games in len(update_df):

			#Make bet if better than "rule of 7"
			if ((float(Init_Games_DF["Over_Bet"][index]) - float(update_df["Over"][index])) < -1):
				Select_Over_Under(Bot, (index + 1), 'over')
				Input_Bet(Bot, 1)
				Click_Submit_Button(Bot)
				bet_count += 0
				break

				#Make bet if better than reverse "rule of 7"
			elif ((float(Init_Games_DF["Under_Bet"][index]) - float(update_df["Under"][index])) > -1):
				Select_Over_Under(Bot, (index + 1), 'under')
				Input_Bet(Bot, 1)
				Click_Submit_Button(Bot)
				bet_count += 0
				break

			#Increase Index
			index += 1

		#Store Results?
		


	#End
	End_Test(Bot)


Bovada = Bot()
Run(Bovada)






