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



class UI_Controller(Terminal_Base):
	def __init__(self, curses, stdscr):
		#Initialize
		Terminal_Base.__init__(self, curses, stdscr)

		#Terminal Variables
		self.CLASS_ID = 'UI_Controller'
		self.home_menu = ['Bot', 'Games', 'Stats', 'History']
		self.actions_menu = ['Startup', 'Test', 'Run']


	def print_center(self, text):
		self.stdscr.clear()
		h, w = self.stdscr.getmaxyx()
		x = w//2 - len(text)//2
		y = h//2
		self.stdscr.addstr(y, x, text)
		self.stdscr.refresh()

	def Exit_Procedure(self):
		self.stdscr.clear()
		h, w = self.stdscr.getmaxyx()
		x = w//2
		y = h//2
		self.stdscr.addstr(y, x - 10, '[EXIT]: Closing program...')
		if (self.created_bot):
			self.Bot.Driver.quit()
		self.stdscr.refresh()
		time.sleep(1)
		self.curses.endwin()
		os.system("killall -9 python")


	def Actions(self):
		self.stdscr.clear()
		self.stdscr.refresh()
		# color scheme for selected row
		self.curses.init_pair(1, self.curses.COLOR_WHITE, self.curses.COLOR_BLACK)    
		current_row = 0 # specify the current selected row
		# print the menu
		self.Actions_Menu(current_row)
		# handle pages
		while 1:
			key = self.stdscr.getch() #get user input
			# handle menu option selection
			if key == self.curses.KEY_UP and current_row > 0:
				current_row -= 1
			elif key == self.curses.KEY_DOWN and current_row < len(self.actions_menu)-1:
				current_row += 1
			elif key == self.curses.KEY_ENTER or key in [10, 13]:
				page = self.actions_menu[current_row]
				if (page == 'Startup'): # Exit Procedure
					try:
						self.print_center("Running: Controller Setup")
						self.setup_complete = self.Setup_Controller()
						if (self.setup_complete):
							self.print_center("Success: Controller Setup")
						self.stdscr.getch()
					except:
						break
				elif (page == 'Test'): # Exit Procedure
					try:
						self.print_center("Running: Bovada Setup")
						self.bovada_setup_succeed = self.Setup_Bovada()
						if (self.bovada_setup_succeed):
							self.print_center("Success: Bovada Setup")
					except:
						break
				elif (page == 'Run'): # Exit Procedure
					try:
						self.print_center("'{}'".format(self.actions_menu[current_row]))
						self.stdscr.getch()
					except:
						break
			elif (key == ord('q')):
				self.Exit_Procedure()
			elif (key == ord('b')):
				self.Home()
			# Bring up the main menu
			self.Actions_Menu(current_row)

	def terminal_start(self):  #Terminal Start
		self.Home() 



