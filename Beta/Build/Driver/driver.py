#Imports (General)
import re as re
import numpy as np
import time
from bs4 import BeautifulSoup
import pickle

#Imports (Selenium)
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
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
		self.CONFIG_PATH = '/home/human/AI-Gambler/Config/config.ini'
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

		#Wait for response
		self.Driver_Wait = WebDriverWait(self.Driver, 10)

	#initialize web page
	def Initialize_Webpage(self):
		self.Driver.get(self.Config_Options['BASE_URLS']['BASE'])


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


	# If captcha page is displayed, this function will run indefinitely until the captcha page is no longer displayed (checks for it every 30 seconds).
	# Purpose of the function is to "pause" execution of the scraper until the user has manually completed the captcha requirements.
	def _pause_for_captcha(self):
		while True:
			time.sleep(30)
			if not self._is_element_displayed("captcha-container", "class"):
				break


	# Check to see if the page is currently stuck on a captcha page. If so, pause 
	# the scraper until user has manually completed the captcha requirements.
	def check_for_captcha(self):
		if self._is_element_displayed("captcha-container", "class"):
			print("\nCAPTCHA!\nManually complete the captcha requirements.\nOnce that's done, if the program was in the middle of scraping "\
			"(and is still running), it should resume scraping after ~30 seconds.")
			self._pause_for_captcha()
		

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
		# Check to make sure a captcha page is not displayed.
		self.check_for_captcha()


	def Switch_Frame(self):
		iframe = self.Driver.find_element_by_tag_name('iframe')
		self.Driver.switch_to.frame(iframe)



	def Switch_Default_Frame(self):
		self.Driver.switch_to.default_content()
	


	# Teardown webdriver.
	def Close_Connection(self):
	    self.Driver.quit()
	    quit()