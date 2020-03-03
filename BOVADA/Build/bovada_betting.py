#Imports Bot
from .bot import *



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

