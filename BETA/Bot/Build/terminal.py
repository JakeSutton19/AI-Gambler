class Terminal_Base:
	def __init__(self, cur, std, **kwargs):
		#Import Variables
		self.curses = cur
		self.stdscr = std

		# Start colors in curses
		self.curses.curs_set(0) # turn off cursor blinking
		self.curses.start_color()
		self.curses.init_pair(1, self.curses.COLOR_WHITE, self.curses.COLOR_BLACK)
		self.curses.init_pair(2, self.curses.COLOR_CYAN, self.curses.COLOR_BLACK)
		self.curses.init_pair(3, self.curses.COLOR_GREEN, self.curses.COLOR_BLACK)
		self.curses.init_pair(4, self.curses.COLOR_RED, self.curses.COLOR_BLACK)
		self.curses.init_pair(5, self.curses.COLOR_CYAN, self.curses.COLOR_WHITE)
		self.curses.init_pair(6, self.curses.COLOR_BLACK, self.curses.COLOR_WHITE)
		self.curses.init_pair(7, self.curses.COLOR_BLACK, self.curses.COLOR_CYAN)
		self.curses.init_pair(8, self.curses.COLOR_BLACK, self.curses.COLOR_GREEN)


	def Home(self):
		self.stdscr.clear()
		self.stdscr.refresh()
		# color scheme for selected row
		self.curses.init_pair(1, self.curses.COLOR_WHITE, self.curses.COLOR_BLACK)    
		current_row = 0 # specify the current selected row
		# print the menu
		self.Home_Menu(current_row)
		# handle pages
		while 1:
			key = self.stdscr.getch() #get user input
			# handle menu option selection
			if key == self.curses.KEY_UP and current_row > 0:
				current_row -= 1
			elif key == self.curses.KEY_DOWN and current_row < len(self.home_menu)-1:
				current_row += 1
			elif key == self.curses.KEY_ENTER or key in [10, 13]:
				page = self.home_menu[current_row]
				if (page == 'Bot'): # Exit Procedure
					try:
						self.Actions()
					except:
						break
				elif (page == 'Games'): # Exit Procedure
					try:
						self.print_center("Live {}".format(self.home_menu[current_row]))
						self.stdscr.getch()
					except:
						break
				elif (page == 'Stats'): # Exit Procedure
					try:
						self.print_center("'{}'".format(self.home_menu[current_row]))
						self.stdscr.getch()
					except:
						break
				elif (page == 'History'): # Exit Procedure
					try:
						self.print_center("'{}'".format(self.home_menu[current_row]))
						self.stdscr.getch()
					except:
						break
			elif (key == ord('q')):
				self.Exit_Procedure()
			# Bring up the main menu
			self.Home_Menu(current_row)


	def Home_Menu(self, selected_row_idx):
		k = 0
		cursor_x = 0
		cursor_y = 0
		# Initialization
		self.stdscr.clear()
		height, width = self.stdscr.getmaxyx()
		cursor_x = max(0, cursor_x)
		cursor_x = min(width-1, cursor_x)
		cursor_y = max(0, cursor_y)
		cursor_y = min(height-1, cursor_y)
		# Declaration of strings
		title = "#                  AI Gambler                  #"
		bar =   "#----------------------------------------------#"
		# Centering calculations
		start_x_title = int((width // 2) - (len(title) // 2) - len(title) % 2)
		start_y = int((height // 4) - 2)
		# Turning on attributes for title
		self.stdscr.attron(self.curses.color_pair(2))
		self.stdscr.attron(self.curses.A_BOLD)
		# Rendering title
		self.stdscr.addstr(start_y, start_x_title, title)
		self.stdscr.addstr(start_y + 1, start_x_title, bar)
		self.stdscr.addstr(start_y - 1, start_x_title, bar)
		# Turning off attributes for title
		self.stdscr.attroff(self.curses.color_pair(2))
		# Nav through menu options
		for idx, row in enumerate(self.home_menu):
			x = width//2 - (len(row) // 2) - len(row) % 2
			y = height//2 - len(self.home_menu)//2 + idx
			if idx == selected_row_idx:
				self.stdscr.attron(self.curses.color_pair(3))
				self.stdscr.addstr(y, x, row)
				self.stdscr.attroff(self.curses.color_pair(3))
			else:
				self.stdscr.addstr(y, x, row)
			self.stdscr.refresh()


	def Actions_Menu(self, selected_row_idx):
		k = 0
		cursor_x = 0
		cursor_y = 0
		# Initialization
		self.stdscr.clear()
		height, width = self.stdscr.getmaxyx()
		cursor_x = max(0, cursor_x)
		cursor_x = min(width-1, cursor_x)
		cursor_y = max(0, cursor_y)
		cursor_y = min(height-1, cursor_y)
		# Declaration of strings
		title = "#             AI Gambler - Actions             #"
		bar =   "#----------------------------------------------#"
		# Centering calculations
		start_x_title = int((width // 2) - (len(title) // 2) - len(title) % 2)
		start_y = int((height // 4) - 2)
		# Turning on attributes for title
		self.stdscr.attron(self.curses.color_pair(2))
		self.stdscr.attron(self.curses.A_BOLD)
		# Rendering title
		self.stdscr.addstr(start_y, start_x_title, title)
		self.stdscr.addstr(start_y + 1, start_x_title, bar)
		self.stdscr.addstr(start_y - 1, start_x_title, bar)
		# Turning off attributes for title
		self.stdscr.attroff(self.curses.color_pair(2))
		# Nav through menu options
		for idx, row in enumerate(self.actions_menu):
			x = width//2 - (len(row) // 2) - len(row) % 2
			y = height//2 - len(self.actions_menu)//2 + idx
			if idx == selected_row_idx:
				self.stdscr.attron(self.curses.color_pair(3))
				self.stdscr.addstr(y, x, row)
				self.stdscr.attroff(self.curses.color_pair(3))
			else:
				self.stdscr.addstr(y, x, row)
			self.stdscr.refresh()
