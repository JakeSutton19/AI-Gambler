#Imports (General)
import re as re
import numpy as np
import time
from bs4 import BeautifulSoup
import pickle
import os

#Imports (Selenium)
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException

#Imports (Files)
from .toolkit import Configure_From_File


class Driver:
	def __init__(self):
		#Attributes
		self.CLASS_ID = 'Bot_Driver'

		#Setup
		self.Config_Options = None
		self.CONFIG_PATH = '/home/human/AI-Gambler/CONFIG/config.ini'
		self.Driver_Options = None

		#Driver
		self.Driver = None
		self.Driver_Wait = None

		#Setup
		self.Initialize_Setup()
		self.Initialize_Driver()
		self.Initialize_Webpage()
	
	#Setup from confige file
	def Initialize_Setup(self):
		#Config File
		self.Config_Options = Configure_From_File(self.CONFIG_PATH)

		#Web Driver Options
		self.Driver_Options = webdriver.ChromeOptions()
		self.Driver_Options.add_argument(self.Config_Options['OPTIONS']['OPTION_2'])
		self.Driver_Options.add_argument(self.Config_Options['OPTIONS']['OPTION_3'])
		self.Driver_Options.add_extension(self.Config_Options['EXTENSIONS']['DUCK_CRX_PATH'])

		#Extras
		# self.Driver_Options.add_argument(self.Config_Options['OPTIONS']['OPTION_1']) # Headless
		# self.Driver_Options.add_argument(self.Config_Options['OPTIONS']['OPTION_4']) # Incognito

	#initialize web driver
	def Initialize_Driver(self): # driver = 'Chrome'
		self.Driver = webdriver.Chrome(chrome_options=self.Driver_Options, 
			executable_path=self.Config_Options['ENVIRONMENT']['CHROMEDRIVER_PATH'])

		#Set up Waits
		self.Driver.implicitly_wait(10)
		self.Driver_Wait = WebDriverWait(self.Driver, 10)

	#initialize web page
	def Initialize_Webpage(self):
		self.Driver.get(self.Config_Options['BASE_URLS']['BASE'])


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

	#Go to site
	def Go_to_Site(self, site):
		self.Driver.get(site)


	def Switch_Frame(self):
		iframe = self.Driver.find_element_by_tag_name('iframe')
		self.Driver.switch_to.frame(iframe)


	def Switch_Default_Frame(self):
		self.Driver.switch_to.default_content()

	def GetSoup(self):
		soup = BeautifulSoup(self.Driver.page_source, 'html.parser')
		print(soup.prettify())


	def End_Test(self):
		input("Press [ENTER] to end session.")

		#Countdown
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