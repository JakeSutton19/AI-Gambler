#Imports (General)


#Imports (Files)
from .bovada_login import *



class Bovada_Bot(Bovada_Login):
	def __init__(self):
		#Initilaization
		super().__init__()


	def Poker_Cash_Game_Setup(self):
		#Access Site
		self.Go_to_Site(self.Config_Options['BOVADA_URLS']['CASH_GAME'])
	
		#Setup Texas Holdem
		try:
			#Find Elements
			input("Press [Enter] to continue.")
			next_button = self.Driver.find_elements_by_xpath("/html/body/bx-site-preloader/div/bx-headless-site/main/pkr-app/div/div/pkr-cash-game/pkr-cash-zone-filter/div/div/bx-panel/div/div[2]/div/div[2]/pkr-single-game-filter/form/div[3]/div[3]/div/div/button")
			# next_button = self.Driver_Wait.until(EC.presence_of_element_located((By.XPATH, '//button[@type="submit"]')))
			# practice_mode_toggle = self.Driver_Wait.until(EC.presence_of_element_located((By.ID, "vr2owa")))
			
			#Activate Elements
			input("Press [Enter] to continue.")
			next_button.click()
		except (TimeoutException, NoSuchElementException):
			print("[ERROR]: Unable to find elements")
			return False
			

		
	def Run(self):
		# self.Bovada_Quick_Login()
		
		self.End_Test()