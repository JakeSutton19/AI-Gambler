#Imports (General)


#Imports (Files)
from .Driver.__init__ import *



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

	def Bovada_Login(self):
		#load cookies
		self.load_cookies(self.Config_Options['COOKIES']['COOKIE_PATH'])

		#Go to Home
		self.Go_to_Site(self.Config_Options['BOVADA_URLS']['HOME'])
		time.sleep(2)

	
	def Bovada_Save_Login(self):
		#Authorization
		self.email_auth = self.Config_Options['BOVADA_AUTH']['EMAIL']
		self.password_auth = self.Config_Options['BOVADA_AUTH']['PASSWORD']

		#Go to Login
		self.Go_to_Site(self.Config_Options['BOVADA_URLS']['LOGIN'])
		time.sleep(2)

		#Login
		try:
			#Find Elements
			email = self.Driver_Wait.until(EC.presence_of_element_located((By.ID, "email")))
			password = self.Driver_Wait.until(EC.presence_of_element_located((By.ID, "login-password")))
			submit = self.Driver_Wait.until(EC.presence_of_element_located((By.ID, "login-submit")))

			#Clear 
			email.clear()
			password.clear()
			time.sleep(1)

			#Input
			email.send_keys(self.email_auth)
			time.sleep(1)
			password.send_keys(self.password_auth)
			time.sleep(1)

			#Submit
			submit.click()
			time.sleep(1)

			#Save Cookies and Return
			input("Press [Enter] to continue.")
			self.save_cookies(self.Config_Options['COOKIES']['COOKIE_PATH'])
			return True
		except (TimeoutException, NoSuchElementException):
			return False

	def Bovada_Poker_Setup(self):
		#Access Site
		self.Go_to_Site(self.Config_Options['BOVADA_URLS']['S_A_G'])
		time.sleep(10)

	def Run(self):
		self.Bovada_Login()
		self.Bovada_Poker_Setup()
		self.Close_Connection()



