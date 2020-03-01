#Imports (General)
from bs4 import BeautifulSoup

#Imports (Files)
from .bovada_login import *



class Bovada_Bot(Bovada_Login):
	def __init__(self):
		#Initilaization
		super().__init__()

		#Soup
		self.soup = None

		#Data
		self.data_table = None


	def Click_Dropdown_Box(self):
		try:
			dropdown_box = self.Driver_Wait.until(EC.presence_of_element_located((By.ID, "small-dropdown")))
			time.sleep(.5)
			dropdown_box.click()
		except:
			print("[ERROR]: Unable to Click_Dropdown_Box")
			return False


	def Click_Quarter_Lines(self):
		try:
			q_lines = self.Driver_Wait.until(EC.presence_of_element_located((By.XPATH, 
					"/html/body/bx-site/ng-component/div/sp-sports-ui/div/main/div/section/main/sp-path-event/div/header/sp-filter/section/div[2]/sp-market-type-filter/figure/ul/li[4]")))
			time.sleep(.5)
			q_lines.click()
		except:
			print("[ERROR]: Unable to Click_Quarter_Lines")
			return False


	def Click_Show_All(self):
		try:
			show_button = self.Driver_Wait.until(EC.presence_of_element_located((By.XPATH, 
					"/html/body/bx-site/ng-component/div/sp-sports-ui/div/main/div/section/main/sp-path-event/div/sp-happening-now/div/div/div[3]/button")))
			time.sleep(.5)
			show_button.click()
		except:
			print("[ERROR]: Unable to Click_Show_All")
			return False


	def Nav_to_Basketball_Page(self):
		try:
			#Access Site
			self.Go_to_Site(self.Config_Options['BOVADA_URLS']['BASKETBALL_URL'])

			#Click Dropdown
			self.Click_Dropdown_Box()

			#Click Quarter Lines
			self.Click_Quarter_Lines()

			#Click Show All
			# self.Click_Show_All()
		except:
			print("[ERROR]: Unable to Nav_to_Basketball_Page")
			return False


	def GetSoup(self):
		soup = BeautifulSoup(self.Driver.page_source, 'html.parser')
		print(soup.prettify())


	def Scrape_Page(self):
		input("Press [Enter] to scrape.")
		#Get Soup
		self.soup = BeautifulSoup(self.Driver.page_source, 'html.parser')

		#Find Table
		data_table = self.soup.findAll('span')
		print(data_table)


	
	def Run(self):
		self.Bovada_Quick_Login()
		self.Nav_to_Basketball_Page()
		self.Scrape_Page()
		
		self.End_Test()
