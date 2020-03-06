#Imports Bot
from .bot import *

def Poker_Cash_Game_Setup_PracticeMode(Bot):
	#Access Site
	Bot.Go_to_Site(Bot.Config_Options['BOVADA_URLS']['CASH_GAME'])

	#Switch to Frame
	Bot.Switch_Frame()

	#Setup Texas Holdem
	try:
		#Click Practice Mode
		practice = Bot.Driver_Wait.until(EC.presence_of_element_located((By.XPATH, 
			'/html/body/bx-site-preloader/div/bx-headless-site/main/pkr-app/div/div/pkr-cash-game/pkr-cash-zone-filter/div/div/bx-panel/div/div[2]/div/div[2]/pkr-single-game-filter/form/div[3]/div[4]/bx-toggle')))
		time.sleep(.5)
		practice.click()

		#Click Next Button
		next_button = Bot.Driver_Wait.until(EC.presence_of_element_located((By.XPATH, '//button[@type="submit"]')))
		time.sleep(.5)
		next_button.click()

		#Click Stake Selection
		stake = Bot.Driver_Wait.until(EC.presence_of_element_located((By.XPATH, 
			'/html/body/bx-site-preloader/div/bx-headless-site/main/pkr-app/div/div/pkr-cash-game/pkr-cash-zone-filter/div/div/bx-panel/div/div[2]/div/div[2]/pkr-single-game-filter/pkr-overlay/div/div/section/pkr-buy-in/div/div/form/bx-dropdown')))
		time.sleep(.5)
		stake.click()

		# $2.00/$4.00
		first_op = Bot.Driver_Wait.until(EC.presence_of_element_located((By.XPATH, 
			'/html/body/bx-site-preloader/div/bx-headless-site/main/pkr-app/div/div/pkr-cash-game/pkr-cash-zone-filter/div/div/bx-panel/div/div[2]/div/div[2]/pkr-single-game-filter/pkr-overlay/div/div/section/pkr-buy-in/div/div/form/bx-dropdown/figure/ul/li')))
		time.sleep(.5)
		first_op.click()

		#Click Take My Seat
		take_seat = Bot.Driver_Wait.until(EC.presence_of_element_located((By.XPATH, 
			'/html/body/bx-site-preloader/div/bx-headless-site/main/pkr-app/div/div/pkr-cash-game/pkr-cash-zone-filter/div/div/bx-panel/div/div[2]/div/div[2]/pkr-single-game-filter/pkr-overlay/div/div/section/pkr-buy-in/div/div/form/div/div[3]/div/div[1]/button')))
		time.sleep(.5)
		take_seat.click()
		return True
		
	except:
		print("[ERROR]: Unable to find elements")
		return False


def Poker_Cash_Game_Setup_Live(Bot):
	#Access Site
	Bot.Go_to_Site(Bot.Config_Options['BOVADA_URLS']['CASH_GAME'])

	#Refresh 
	Bot.Driver.refresh()

	#Setup Texas Holdem
	try:
		#Click Next Button
		next_button = Bot.Driver_Wait.until(EC.presence_of_element_located((By.XPATH, '//button[@type="submit"]')))
		time.sleep(.5)
		next_button.click()

		#Click Stake Selection
		stake = Bot.Driver_Wait.until(EC.presence_of_element_located((By.XPATH, 
			'/html/body/bx-site-preloader/div/bx-headless-site/main/pkr-app/div/div/pkr-cash-game/pkr-cash-zone-filter/div/div/bx-panel/div/div[2]/div/div[2]/pkr-single-game-filter/pkr-overlay/div/div/section/pkr-buy-in/div/div/form/bx-dropdown')))
		time.sleep(.5)
		stake.click()

		# $0.02/$0.05
		first_op = Bot.Driver_Wait.until(EC.presence_of_element_located((By.XPATH, 
			'/html/body/bx-site-preloader/div/bx-headless-site/main/pkr-app/div/div/pkr-cash-game/pkr-cash-zone-filter/div/div/bx-panel/div/div[2]/div/div[2]/pkr-single-game-filter/pkr-overlay/div/div/section/pkr-buy-in/div/div/form/bx-dropdown/figure/ul/li[1]')))
		time.sleep(.5)
		first_op.click()

		#Click Take My Seat
		Bot.Driver_Wait.until(EC.presence_of_element_located((By.XPATH, 
			'/html/body/bx-site-preloader/div/bx-headless-site/main/pkr-app/div/div/pkr-cash-game/pkr-cash-zone-filter/div/div/bx-panel/div/div[2]/div/div[2]/pkr-single-game-filter/pkr-overlay/div/div/section/pkr-buy-in/div/div/form/div/div[3]/div/div[1]/button'))).click()
	except:
		print("[ERROR]: Unable to find elements")
		return False


# def Poker_Play_TexasHoldem(self):
# 	input("Press [Enter] to Play.")

# 	buy_chips_selection = self.Driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[4]/div[2]/div/div[2]/div[1]/label[1]')
# 	time.sleep(.5)
# 	print(buy_chips_selection)
# 	buy_chips_selection.click()

	# try:
	# 	input("Press [Enter] to Play.")

	# 	# Switch to Frame
	# 	# self.Switch_Frame()

	# 	buttons = self.Driver_Wait.until(EC.presence_of_element_located((By.TAG_NAME, 'button'))).click()
	# 	# print(buttons)
	# 	# buttons.click()

	# 	# input("Press [Enter] to Fold.")

	# 	# #Click Fold
	# 	# fold = self.Driver_Wait.until(EC.presence_of_element_located((By.XPATH, 
	# 	# 	'/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[4]/div[2]/div/div[2]/div[1]/div[1]/button')))
	# 	# time.sleep(.5)
	# 	# fold.click()

	# 	# #Click Check
	# 	# check = self.Driver_Wait.until(EC.presence_of_element_located((By.XPATH, 
	# 	# 	'/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[4]/div[2]/div/div[2]/div[1]/div[2]/button')))
	# 	# time.sleep(.5)
	# 	# check.click()

	# 	#Click to Raise
	# 	# //*[@id="root"]/div/div[2]/div[2]/div[2]/div[2]/div[4]/div[2]/div/div[2]/div[1]/div[3]/button

	# 	#Click Wait for BB
	# 	# /html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[4]/div[2]/div/div[2]/div[1]/label[1]

	# 	#CLick Join Next Hand
	# 	# /html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[4]/div[2]/div/div[2]/div[1]/label[2]

	# 	#Click Buy Chips
	# 	# buy_chips_selection = self.Driver_Wait.until(EC.presence_of_element_located((By.XPATH, 
	# 	# 	'//*[@id="root"]/div/div[2]/div[2]/div[2]/div[2]/div[4]/div[1]/div/div[2]/button')))
		# buy_chips_selection = self.Driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div[2]/div[2]/div[4]/div[1]/div/div[2]/button')
		# time.sleep(.5)
		# print(buy_chips_selection)
		# buy_chips_selection.click()
		

	# 	# #Click Buy
	# 	# buy_chips = self.Driver_Wait.until(EC.presence_of_element_located((By.XPATH, 
	# 	# 	'/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[4]/div[1]/div/div[2]/div/button')))
	# 	# time.sleep(.5)
	# 	# buy_chips.click()
	# except:
	# 	print("[ERROR]: Unable to find elements")
	# 	return False