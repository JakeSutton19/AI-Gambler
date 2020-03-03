#Imports (General)


#Imports (Files)
from .Base.__init__ import *



class Bovada_Login(Bot):
	def __init__(self):
		#Initilaization
		super().__init__()

		#Bovada 
		self.email_auth = None
		self.password_auth = None

		#Cookies
		self.cookie_check = None
		self.set_cookies = None

		#Bovada Authorization
		self.email_auth = self.Config_Options['BOVADA_AUTH']['EMAIL']
		self.password_auth = self.Config_Options['BOVADA_AUTH']['PASSWORD']

	
	def Bovada_Setup_Login(self):
		#Go to Login Page
		self.Go_to_Site(self.Config_Options['BOVADA_URLS']['LOGIN'])

		#Login
		try:
			#Find Elements
			email = self.Driver_Wait.until(EC.presence_of_element_located((By.ID, "email")))
			password = self.Driver_Wait.until(EC.presence_of_element_located((By.ID, "login-password")))
			remember_me_label = self.Driver_Wait.until(EC.presence_of_element_located((By.ID, "remember-me-label")))
			submit = self.Driver_Wait.until(EC.presence_of_element_located((By.ID, "login-submit")))

			#Input Login Info and Submit
			email.clear()
			password.clear()
			time.sleep(1)
			email.send_keys(self.email_auth)
			time.sleep(1)
			password.send_keys(self.password_auth)
			time.sleep(1)
			remember_me_label.click()
			time.sleep(1)
			submit.click()

			#Save Cookies and Return
			input("Press [Enter] to save cookies.")
			self.save_cookies(self.Config_Options['COOKIES']['POKER_COOKIE_PATH'])
			return True
		except (TimeoutException, NoSuchElementException):
			print("[ERROR]: Unable to Login and Save.")
			return False


	def Bovada_Quick_Login(self):
		try:
			#load cookies
			self.load_cookies(self.Config_Options['COOKIES']['POKER_COOKIE_PATH'])

			#Go to Home
			self.Go_to_Site(self.Config_Options['BOVADA_URLS']['HOME'])
		except TimeoutException:
			print("[ERROR]: Unable to preform Quick Login.")
			return False



	

	
	


