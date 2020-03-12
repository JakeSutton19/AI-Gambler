#Bovada Build Imports 

# Bot
from .bot import Bot

# Tools
from .tools import Configure_From_File, End_Test, Info_Message, Error_Message, Error_Quit

#Terminal
from .terminal import Terminal_Base



# #--------------------------------------------------------------------- Functions ---------------------------------------------------------------------#
# #Returns Bot
# def Create_Bot():
# 	try:
# 		#Create the Bot
# 		bot = Bot()
# 		return bot, True
# 	except Error as e:
# 		print(e)
# 		Error_Message("Create_Bot failed.")
# 		return False


