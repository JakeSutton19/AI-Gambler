#Imports (General)
import time
from bs4 import BeautifulSoup

#Imports (Files)
from .driver import *



class Bot(Driver):
	def __init__(self):
		#Initilaization
		super().__init__()

		#Bovada 
		self.email_auth = None
		self.password_auth = None

		#Cookies
		self.cookie_check = None
		self.set_cookies = None


	def GetSoup(self):
		soup = BeautifulSoup(self.Driver.page_source, 'html.parser')
		print(soup.prettify())


	def End_Test(self):
		#Countdown
		input("Press [ENTER] to end session.")
		time.sleep(.5)
		self.Driver.quit()
		time.sleep(.5)
		print("\nSession ended.")
		quit()