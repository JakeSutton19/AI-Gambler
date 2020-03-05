#Bovada Build Imports 

# Bot
from .bot import Bot

# Tools
from .tools import Configure_From_File, End_Test, Info_Message, Error_Message

# Login
from .bovada_login import Bovada_Setup_Login, Bovada_Quick_Login

#--------------------------------------------------------------------- Functions ---------------------------------------------------------------------#
#Returns Bot
def Create_Bot():
	try:
		#Create the Bot
		bot = Bot()
		return bot
	except Error as e:
		print(e)
		Error_Message("Create_Bot failed.")
		return False

#Login
def Bovada_Login(Bot):
	#Login to Bovada
	try:
		login_status = Bovada_Quick_Login(Bot) #Login 
	except Error as e:
		print(e)
		Error_Message("Quick login failed.")

	#If Unsuccesfull
	if (login_status == False):
		Info_Message('Attempting manual login..')

		#Re attempt Login
		try:
			login_status = Bovada_Setup_Login(Bot) #Login 
		except Error as e:
			print(e)
			Error_Message("Manual login failed. Shutting Down.")
			Error_Quit(Bot)

		#Return Status
		return login_status
	#Successful
	else:
		return True