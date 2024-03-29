#Import 
import time

#Imports (Selenium)
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException


def Bovada_Quick_Login(Bot):
	#load cookies
	Bot.load_cookies(Bot.Config_Options['COOKIES']['BOVADA_LOGIN_COOKIE'])

	#Go to Home
	try:
		Bot.Go_to_Site(Bot.Config_Options['BOVADA_URLS']['HOME'])
		time.sleep(.5)
		return True
	except:
		print("[ERROR]: Unable to preform Quick Login.")
		return False

		

def Bovada_Login(Bot):
	#Bovada Authorization
	email_auth = Bot.Config_Options['BOVADA_AUTH']['EMAIL']
	password_auth = Bot.Config_Options['BOVADA_AUTH']['PASSWORD']

	#load cookies
	Bot.load_cookies(Bot.Config_Options['COOKIES']['BOVADA_LOGIN_COOKIE'])

	#Go to Home
	try:
		Bot.Go_to_Site(Bot.Config_Options['BOVADA_URLS']['HOME'])
		time.sleep(.5)
		Bot.Go_to_Site(Bot.Config_Options['BOVADA_URLS']['LOGIN'])
		time.sleep(1)

		#Check for Captch
		if (Bot.check_for_captcha()):
			#Login
			try:
				#Find Elements
				email = Bot.Driver_Wait.until(EC.presence_of_element_located((By.ID, "email")))
				password = Bot.Driver_Wait.until(EC.presence_of_element_located((By.ID, "login-password")))
				remember_me_label = Bot.Driver_Wait.until(EC.presence_of_element_located((By.ID, "remember-me-label")))
				submit = Bot.Driver_Wait.until(EC.presence_of_element_located((By.ID, "login-submit")))

				#Input Login Info and Submit
				email.clear()
				password.clear()
				time.sleep(1)
				email.send_keys(email_auth)
				time.sleep(1)
				password.send_keys(password_auth)
				time.sleep(1)
				remember_me_label.click()
				time.sleep(1)
				submit.click()

				#Save Cookies and Return
				input("Press [Enter] to save cookies.")
				Bot.save_cookies(Bot.Config_Options['COOKIES']['BOVADA_LOGIN_COOKIE'])
				return True

			except (TimeoutException, NoSuchElementException):
				print("[ERROR]: Unable to Login and Save.")
				return False				
	except:
		print("[ERROR]: Unable to preform Quick Login.")
		return False




def Bovada_Setup_Login(Bot):
	#Bovada Authorization
	email_auth = Bot.Config_Options['BOVADA_AUTH']['EMAIL']
	password_auth = Bot.Config_Options['BOVADA_AUTH']['PASSWORD']

	#Go to Login Page
	Bot.Go_to_Site(Bot.Config_Options['BOVADA_URLS']['LOGIN'])

	#Login
	try:
		#Find Elements
		email = Bot.Driver_Wait.until(EC.presence_of_element_located((By.ID, "email")))
		password = Bot.Driver_Wait.until(EC.presence_of_element_located((By.ID, "login-password")))
		remember_me_label = Bot.Driver_Wait.until(EC.presence_of_element_located((By.ID, "remember-me-label")))
		submit = Bot.Driver_Wait.until(EC.presence_of_element_located((By.ID, "login-submit")))

		#Input Login Info and Submit
		email.clear()
		password.clear()
		time.sleep(1)
		email.send_keys(email_auth)
		time.sleep(1)
		password.send_keys(password_auth)
		time.sleep(1)
		remember_me_label.click()
		time.sleep(1)
		submit.click()

		#Save Cookies and Return
		input("Press [Enter] to continue.")
		Bot.save_cookies(Bot.Config_Options['COOKIES']['BOVADA_LOGIN_COOKIE'])
		return True

	except (TimeoutException, NoSuchElementException):
		print("[ERROR]: Unable to Login and Save.")
		return False


