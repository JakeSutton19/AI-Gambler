#Imports Bot
from .bot import *



# Click Over
def Select_Over_Under(Bot, game, over_or_under): # Starts at 1
	#Identify O/U
	if (over_or_under == 'over'):
		pick = 1
	elif (over_or_under == 'under'):
		pick = 2
	else:
		print("No selection, picking over.")
		pick = 1

	#Select Button
	try:
		Bet_Button = Bot.Driver_Wait.until(EC.presence_of_element_located((By.XPATH,
		 "/html/body/bx-site/ng-component/div/sp-sports-ui/div/main/div/section/main/sp-path-event/div/sp-next-events/div/div/div[1]/sp-coupon[{}] \
		 /sp-multi-markets/section/section/sp-outcomes/sp-two-way-vertical[3]/ul/li[{}]/sp-outcome/button".format(game, pick))))
		time.sleep(.5)
		Bet_Button.click()

		#Return
		return True
	except:
		print("[ERROR]: Unable to Click_Bet_Button")
		return False


# Click Bet
def Click_Bet_Button(Bot):
	try:
		Bet_Button = Bot.Driver_Wait.until(EC.presence_of_element_located((By.CLASS_NAME, "bet-btn")))
		time.sleep(.5)
		Bet_Button.click()

		#Return
		return True
	except:
		print("[ERROR]: Unable to Click_Bet_Button")
		return False


def Input_Bet(Bot, bet_amount):
	try:
		#Find Elements
		risk = Bot.Driver_Wait.until(EC.presence_of_element_located((By.ID, "default-input--risk")))

		#Input Risk Amount
		risk.clear()
		risk.send_keys(int(bet_amount))

		#Return
		return True
	except:
		print("[ERROR]: Unable to Input_Bet")
		return False


def Click_Submit_Button(Bot):
	try:
		Bet_Button = Bot.Driver_Wait.until(EC.presence_of_element_located((By.CLASS_NAME, "place-bets custom-cta primary cta-large")))
		time.sleep(.5)
		Bet_Button.click()

		#Return
		return True
	except:
		print("[ERROR]: Unable to Click_Submit_Button")
		return False


def Clear_Selection_Button(Bot):
	try:
		Bet_Button = Bot.Driver_Wait.until(EC.presence_of_element_located((By.CLASS_NAME, "clear-all-selections-wrapper")))
		time.sleep(.5)
		Bet_Button.click()

		#Return
		return True
	except:
		print("[ERROR]: Unable to Clear_Selection_Button")
		return False

def Make_Bet(Bot):
	try:
		#Bet
		Click_Bet_Button(Bot)
		Input_Bet(Bot, 1)
		Click_Submit_Button(Bot)

		#Return
		return True
	except:
		print("[ERROR]: Unable to Make_Bet")
		return False



