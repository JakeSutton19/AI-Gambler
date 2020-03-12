# Bovada Bot 
# - written by Jacob Sutton

#--------------------------------------------------------------------- IMPORTS ---------------------------------------------------------------------#
#Imports (General)
import time
import os
import curses

#Bovada Imports
from .Build.__init__ import *
from .Bovada.__init__ import *
from .Database.__init__ import *
from .ui_controller import UI_Controller
from .setup_bovada_controller import Setup_Bovada_Controller


class Controller:
	def __init__(self, curses, stdscr):
		#Bot
		self.Bot = None
		self.created_bot = None

		#DB
		self.conn = None
		self.db_path = '/home/human/AI-Gambler/CONFIG/Data/Databases/controller.db'
		self.connected_DB = None

		#Bovada
		self.Bovada_Controller = None
		self.bovada_setup_succeed = None

		#Tags
		self.euro_tag = None
		self.Argentina_tag = None
		self.sk_tag = None
		self.NBA_tag = None

		#Run
		self.setup_complete = None
		self.terminal_start()
		
	#Setup Bot
	def Setup_Bot(self):
		try:
			self.Bot = Bot()
			return True 
		except:
			Error_Message("Unable to Setup_Bot")
			return False

	#Setup DB
	def Setup_DB(self):
		try:
			self.conn = Init_DB(self.db_path)
			return True 
		except:
			Error_Message("Unable to Setup_DB")
			return False

	#Setup Controller
	def Setup_Controller(self):
		try:
			self.created_bot = self.Setup_Bot() #Bot
			self.connected_DB = self.Setup_DB() #DB
			return True 
		except:
			Error_Message("Unable to Setup_Controller")
			return False

	#Setup Bovada
	def Setup_Bovada(self):
		try:
			self.Bovada_Controller = Setup_Bovada_Controller(self.Bot, self.conn, self.setup_complete)
			return True 
		except:
			Error_Message("Unable to Setup_Bovada")
			return False

	#Initialize Games
	def Create_Games_List(self):
		try:
			self.euro_tag, self.Argentina_tag, self.sk_tag, self.NBA_tag = self.Bovada_Controller.Initialize_Basketball_Games()
			return True 
		except:
			Error_Message("Unable to Create_Games_List")
			return False
		
		
		
		