#Imports (Files)
from bot_driver import *



class Bot(Bot_Driver):
	def __init__(self):
		#Initilaization
		super().__init__()

		#Bovada 
		self.email_auth = None
		self.password_auth = None

	def Initialize_Webdriver(self):
		self.Initialize_Setup()
		self.Initialize_Driver()
		self.Initialize_Webpage()

	def Initialize_Bovada(self):
		#Authorization
		self.email_auth = self.Config_Options['BOVADA_AUTH']['EMAIL']
		self.password_auth = self.Config_Options['BOVADA_AUTH']['PASSWORD']

		#Access Site
		self.Go_to_Site(self.Config_Options['BOVADA_URLS']['LOGIN'])
		time.sleep(2)

	def Bovada_Login(self):
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
			time.sleep(45)
			return True
		except (TimeoutException, NoSuchElementException):
			return False

	def Bovada_Poker_Setup(self):
		#Access Site
		self.Go_to_Site(self.Config_Options['BOVADA_URLS']['S_A_G'])
		time.sleep(30)

	def Run(self):
		self.Initialize_Webdriver()
		self.Initialize_Bovada()
		self.Bovada_Login()
		self.Bovada_Poker_Setup()
		time.sleep(5)
		self.Close_Connection()



