#Imports Webscraping
from urllib.request import urlopen
from bs4 import BeautifulSoup


# Functions
#
def GetSoup(Bot):
	soup = BeautifulSoup(Bot.Driver.page_source, 'html.parser')
	print(soup.prettify())


def Scrape_Page(Bot):
	input("Press [Enter] to run scrape.")
	#Get Soup
	try:
		soup = BeautifulSoup(Bot.Driver.page_source, 'html.parser')
		grouped_events = []
		data_table = soup.findAll('section', class_="coupon-content more-info")
		# for rows in data_table:
		# 	grouped_events.append(rows)

		print(len(data_table))
		return True
	except:
		print("[ERROR]: Unable to Scrape Page")
		return False


def Grab_Scores(Scores, data_dict):
	#Find Scores
	all_scores = []
	for items1 in Scores.findAll('span', class_="score-nr"): # S1 = H, S2 = A
		all_scores.append(items1.get_text())

	#Find Time
	all_times = []
	for items2 in Scores.findAll('span', class_="gs"): # T1 = Quarter, T2 = Time
		all_times.append(items2.get_text())

	#Update
	data_dict['Top'] = all_scores[0]
	data_dict['Bottom'] = all_scores[1]
	data_dict['Quarter'] = all_times[0]
	data_dict['Time'] = all_times[1]

	#Ship Data
	return data_dict


def Grab_Teams(Teams, data_dict):
	#Find Teams
	all_teams = []
	for items1 in Teams.findAll('span', class_="name"): # S1 = H, S2 = A
		all_teams.append(items1.get_text())

	#Update
	data_dict['Top Team'] = all_teams[0]
	data_dict['Bottom Team'] = all_teams[1]

	#Ship Data
	return data_dict


def Grab_Outcomes(Outcomes, data_dict):
	#Find Outcomes
	all_outs = []
	for items1 in Outcomes.findAll('span', class_="market-line bet-handicap both-handicaps"): # S2 = O, S4 = U
		all_outs.append(items1.get_text())

	#Update
	data_dict['Over'] = all_outs[1]
	data_dict['Under'] = all_outs[3]

	#Ship Data
	return data_dict


def Create_Game(game):
	#Create data dict
	data_dict = {}

	#Find Scores in Game
	for score in game.findAll('sp-score-coupon', class_="scores"):
		data_dict = Grab_Scores(score, data_dict)
		
	#Find Teams in Game
	for teams in game.findAll('header', class_="event-title"):
		data_dict = Grab_Teams(teams, data_dict)

	#Find Outcomes in Game
	for outs in game.findAll('sp-outcomes', class_="markets-container"):
		data_dict = Grab_Outcomes(outs, data_dict)

	#Return Data
	return data_dict


def Scrape_Live_Games(Bot):
	#Initialize
	input("Press [Enter] to run scrape.")

	#Params
	Live_Games = []
	soup = BeautifulSoup(Bot.Driver.page_source, 'html.parser')
		
	#Isolate Live Games
	hn_bucket = soup.find('div', class_="happening-now-bucket") 

	#Identify individual Games
	for game in hn_bucket.findAll('section', class_="coupon-content more-info"):
		d = Create_Game(game)
		Live_Games.append(d)
		
	#Return Games Info
	return Live_Games
	
	