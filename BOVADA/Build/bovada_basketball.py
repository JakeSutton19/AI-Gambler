#Imports Bot
from .bot import *


def Click_Dropdown_Box(Bot):
	try:
		dropdown_box = Bot.Driver_Wait.until(EC.presence_of_element_located((By.ID, "small-dropdown")))
		time.sleep(.5)
		dropdown_box.click()
		return True
	except:
		print("[ERROR]: Unable to Click_Dropdown_Box")
		return False


def Select_League_Dropbox(Bot):
	try:
		league = Bot.Driver_Wait.until(EC.presence_of_element_located((By.XPATH, 
				"/html/body/bx-site/ng-component/div/sp-sports-ui/div/main/div/section/main/sp-path-event/div/header/sp-filter/section/div[2]/sp-event-path-filter/figure/input")))
		time.sleep(.5)
		league.click()
		return True
	except:
		print("[ERROR]: Unable to Click_Quarter_Lines")
		return False

def Select_League(Bot):
	try:
		league = Bot.Driver_Wait.until(EC.presence_of_element_located((By.XPATH, 
				"/html/body/bx-site/ng-component/div/sp-sports-ui/div/main/div/section/main/sp-path-event/div/header/sp-filter/section/div[2]/sp-event-path-filter/figure/ul/li[{}]".format(4))))
		time.sleep(.5)
		league.click()
		return True
	except:
		print("[ERROR]: Unable to Click_Quarter_Lines")
		return False


def Click_Quarter_Lines(Bot):
	try:
		q_lines = Bot.Driver_Wait.until(EC.presence_of_element_located((By.XPATH, 
				"/html/body/bx-site/ng-component/div/sp-sports-ui/div/main/div/section/main/sp-path-event/div/header/sp-filter/section/div[2]/sp-market-type-filter/figure/ul/li[4]")))
		time.sleep(.5)
		q_lines.click()
		return True
	except:
		print("[ERROR]: Unable to Click_Quarter_Lines")
		return False


def Click_Show_All(Bot):
	try:
		show_button = Bot.Driver_Wait.until(EC.presence_of_element_located((By.XPATH, 
				"/html/body/bx-site/ng-component/div/sp-sports-ui/div/main/div/section/main/sp-path-event/div/sp-happening-now/div/div/div[3]/button")))
		time.sleep(.5)
		show_button.click()
		return True
	except:
		print("[ERROR]: Unable to Click_Show_All")
		return False



def Nav_to_Basketball_Page(Bot):
	try:
		#Access Site
		Bot.Go_to_Site(Bot.Config_Options['BOVADA_URLS']['BASKETBALL_URL'])

		#Click Dropdown
		Click_Dropdown_Box(Bot)

		#Click Quarter Lines
		Click_Quarter_Lines(Bot)

		#Select League Dropbown
		Select_League_Dropbox(Bot)

		#Select League 
		Select_League(Bot)
		time.sleep(2)

		#Return
		return True
	except:
		print("[ERROR]: Unable to Nav_to_Basketball_Page")
		return False




