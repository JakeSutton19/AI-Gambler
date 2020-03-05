# Bovada Bot 
# - written by Jacob Sutton


#--------------------------------------------------------------------- IMPORTS ---------------------------------------------------------------------#
#Imports (General)
import time

#Bovada Imports
from .Build.__init__ import *
from .Betting.__init__ import *
from .Database.__init__ import *
from .Poker.__init__ import *
from .Setup.__init__ import *








#Bovada Controller
class Controller:
	def __init__(self):
		#Status
		self.create_bot = None
		self.bovada_login = None

	#1. Setup
	def Setup(self):
		self.bovada_login = Bovada_Login(self.Bot)


#Bovada 
def Bovada:
	#Create bot




	
def Run_Test(Bot):
	#Access Site
	Bot.Go_to_Site(Bot.Config_Options['BOVADA_URLS']['BASKETBALL_URL'])

	#End
	End_Test(Bot)