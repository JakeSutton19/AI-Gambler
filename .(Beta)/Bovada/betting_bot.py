#Imports
import functools
import logging
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
import os

#Bots
from BotKit.__init__ import *


class Betting_Bot(Base_Bot):
	def __init__(self, webdriver_import, CONFIG=None):
		super().__init__(webdriver_import)

		#Details
		self.username = self.base_config['BOVADA_AUTH']['USERNAME']
		self.password = self.base_config['BOVADA_AUTH']['PASSWORD']

	def Login(self):
		usernameToLog = self.driver.find_element_by_id('email')
		time.sleep(.2)
		usernameToLog.send_keys(self.username)
		time.sleep(.2)
		passwordToLog = self.driver.find_element_by_id('login-password')
		time.sleep(.2)
		passwordToLog.send_keys(self.password)
		time.sleep(.5)
		self.driver.find_element_by_id('remember-me-label').click()
		time.sleep(1)
		self.driver.find_element_by_id('login-submit').click()
		

	def Navigate_Live_Betting(self):
		self.driver.find_element_by_id('small-dropdown').click()
		time.sleep(.5)
		ql = self.driver.find_elements_by_xpath('/html/body/bx-site/ng-component/div/sp-sports-ui/div/main/div/section/main/sp-path-event/div/header/sp-filter/section/div[2]/sp-market-type-filter/figure/ul/li[4]')
		# ql = self.driver.find_elements_by_name('Quarter Lines')

		ql.click()

	def Run(self):
		self.Driver_Setup('Chrome')
		self.Access_URL(self.base_config['BOVADA_URLS']['LOGIN'])
		time.sleep(2)

		self.Login()
		time.sleep(40)
		self.Access_URL(self.base_config['BOVADA_URLS']['BBALL'])
		time.sleep(2)
		self.Navigate_Live_Betting()
		time.sleep(10)
		self.Shutdown_Driver()
		# self.Login()


a = Betting_Bot(webdriver)
a.Run()