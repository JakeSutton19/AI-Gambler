#Imports (General)
import time

#Imports (Build)
from Build.__init__ import *


#Functions
#
def End_Test(Bot):
	#Countdown
	input("Press [ENTER] to end session.")
	time.sleep(.5)
	Bot.Driver.quit()
	time.sleep(.5)
	print("\nSession ended.")
	quit()



def Make_Test(Bot):
	try:
		#Bet
		input("Press [ENTER] to start test.")
		Select_Over_Under(Bot, 1, 'over')
		time.sleep(5)
		Clear_Selection_Button(Bot)

		#Return
		return True
	except:
		print("[ERROR]: Unable to Make_Test")
		return False



def Test_Run(Bot):
	Bovada_Quick_Login(Bot)
	Nav_to_Basketball_Page(Bot)
	Create_Future_Games_List(Bot)
	End_Test(Bot)


Bovada = Bot()
Test_Run(Bovada)






# class Bet_Controller:
# 	def __init__(self, Bot):
# 		#Initialize
# 		self.Bot = Bot

# 		#Bets
# 		self.bet = None
# 		self.bet_placed = None
# 		self.bet_amount = None
# 		self.bet_info = None
# 		self.future_bet = None
# 		self.bet_status = None
# 		self.bet_result = None