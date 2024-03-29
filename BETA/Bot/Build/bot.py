#Imports (General)
import re as re
import numpy as np
import time
import pickle
from splinter import Browser

#Imports (Selenium)
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException

#Imports (Files)
from .tools import Configure_From_File


class Bot:
	def __init__(self):
		#Setup
		self.Config_Options = None
		self.CONFIG_PATH = '/home/human/AI-Gambler/CONFIG/config.ini'

		#Cookies
		self.cookie_check = None
		self.set_cookies = None

		#Driver
		self.Driver = None
		self.Driver_Wait = None

		#Setup
		self.Initialize_Setup()
		
		

	#Setup from confige file
	def Initialize_Setup(self):
		#Config File
		self.Config_Options = Configure_From_File(self.CONFIG_PATH)

		#Web Driver Options
		Driver_Options = Options()
		Driver_Options.add_extension(self.Config_Options['EXTENSIONS']['DUCK_CRX_PATH'])
		Driver_Options.add_argument(self.Config_Options['OPTIONS']['OPTION_1']) # User-data
		Driver_Options.add_argument(self.Config_Options['OPTIONS']['OPTION_2']) # Maximize
		Driver_Options.add_argument(self.Config_Options['OPTIONS']['OPTION_3']) # No sandbox
		Driver_Options.add_argument(self.Config_Options['OPTIONS']['OPTION_6']) # No notifications
		Driver_Options.add_experimental_option("excludeSwitches",["ignore-certificate-errors"])
		Driver_Options.add_argument('--mute-audio')
		Driver_Options.add_argument('--dns-prefetch-disable')
		Driver_Options.add_argument('--lang=en-US')
		Driver_Options.add_argument('--disable-setuid-sandbox')
		# Driver_Options.add_argument(self.Config_Options['OPTIONS']['OPTION_4']) # Incognito
		# Driver_Options.add_argument(self.Config_Options['OPTIONS']['OPTION_5']) # Headless

		#Initialize Web Driver
		self.Driver = webdriver.Chrome(options=Driver_Options, 
			executable_path=self.Config_Options['ENVIRONMENT']['CHROMEDRIVER_PATH'])

		#Driver Waits
		self.Driver.implicitly_wait(10)
		self.Driver_Wait = WebDriverWait(self.Driver, 10)

		# Initialize Start Page
		self.Driver.get(self.Config_Options['BASE_URLS']['BASE'])

		# Wait and Load (Effect)
		time.sleep(.5)
	
	#Go to site
	def Go_to_Site(self, site):
		time.sleep(.5)
		self.Driver.get(site)
		time.sleep(.5)

		#Check for captcha
		# cap = self.check_for_captcha()
		# return cap


	# Helper function for checking for the presence of a web element.
	def _is_element_displayed(self, elem_text, elem_type):
		if elem_type == "class":
			try:
				out = self.Driver.find_element_by_class_name(elem_text).is_displayed()
			except (NoSuchElementException, TimeoutException):
				out = False
		elif elem_type == "css":
			try:
				out = self.Driver.find_element_by_css_selector(elem_text).is_displayed()
			except (NoSuchElementException, TimeoutException):
				out = False
		else:
			raise ValueError("arg 'elem_type' must be either 'class' or 'css'")
			return(out)


	def check_for_captcha(self):
		if self._is_element_displayed("captcha-container", "class"):
			return True
		else:
			return False


	def save_cookies(self, path):
		with open(path, 'wb') as filehandler:
			pickle.dump(self.Driver.get_cookies(), filehandler)


	def load_cookies(self, path):
		with open(path, 'rb') as cookiesfile:
			cookies = pickle.load(cookiesfile)
			for cookie in cookies:
				if isinstance(cookie.get('expiry'), float):
					cookie['expiry'] = int(cookie['expiry'])
				self.Driver.add_cookie(cookie)
		time.sleep(.5)


	def Switch_Frame(self):
		#Click Fold
		iframe = self.Driver_Wait.until(EC.presence_of_element_located((By.TAG_NAME, 'iframe')))
		self.Driver.switch_to.frame(iframe)


	def Switch_to_GameFrame(self):
		#Click Fold
		iframe = self.Driver_Wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'f944aqf')))
		self.Driver.switch_to.frame(iframe)
		


	def Switch_Default_Frame(self):
		self.Driver.switch_to.default_content()


	def End_Test(self):
		#Countdown
		input("Press [ENTER] to end session.")
		time.sleep(.5)
		self.Driver.quit()
		time.sleep(.5)
		print("\nSession ended.")
		quit()
		
		
	# Teardown webdriver.
	def Close_Connection(self):
		print("Closed session.")
		self.Driver.quit()
		quit()