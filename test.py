
from BETA.__init__ import *



def Run_Terminal():
	def run(stdscr):
		Controller(curses, stdscr)

	curses.wrapper(run)



Run_Terminal()
