#Imports Webscraping
from urllib.request import urlopen
import pandas as pd
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate


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

		print(len(data_table))

		#Return
		return True
	except:
		print("[ERROR]: Unable to Scrape_Page")
		return False


def Grab_Future_Time(Scores, data_dict):
	try:
		#Find Time
		all_times = []
		for items1 in Scores.findAll('span', class_="period hidden-xs"): # T1 = Quarter, T2 = Time
			all_times.append(items1.get_text())

		#Update
		data_dict['Date'] = all_times[0]

		#Ship Data
		return data_dict
	except:
		print("[ERROR]: Unable to Grab_Scores")
		return False


def Grab_Scores(Scores, data_dict):
	try:
		#Find Scores
		all_scores = []
		for items1 in Scores.findAll('span', class_="score-nr"): # S1 = H, S2 = A
			all_scores.append(items1.get_text())

		#Find Time
		all_times = []
		for items2 in Scores.findAll('span', class_="gs"): # T1 = Quarter, T2 = Time
			all_times.append(items2.get_text())

		#Update
		data_dict['Score1'] = all_scores[0]
		data_dict['Score2'] = all_scores[1]
		data_dict['Quarter'] = all_times[0]
		data_dict['Time'] = all_times[1]

		#Ship Data
		return data_dict
	except:
		print("[ERROR]: Unable to Grab_Scores")
		return False


def Grab_Teams(Teams, data_dict):
	try:
		#Find Teams
		all_teams = []
		for items1 in Teams.findAll('span', class_="name"): # S1 = H, S2 = A
			all_teams.append(items1.get_text())

		#Update
		data_dict['Team1'] = all_teams[0]
		data_dict['Team2'] = all_teams[1]

		#Ship Data
		return data_dict
	except:
		print("[ERROR]: Unable to Grab_Teams")
		return False


def Grab_Outcomes(Outcomes, data_dict):
	try:
		#Find Outcomes
		all_outs = []
		for items1 in Outcomes.findAll('span', class_="market-line bet-handicap both-handicaps"): # S2 = O, S4 = U
			all_outs.append(items1.get_text())

		#Update
		data_dict['Over'] = all_outs[1]
		data_dict['Under'] = all_outs[3]

		#Create Mock Values to Look for
		data_dict['Over_Bet'] = float(all_outs[1]) + 7
		data_dict['Under_Bet'] = float(all_outs[3]) - 7

		#Ship Data
		return data_dict
	except:
		#Update
		data_dict['Over'] = 0.0
		data_dict['Under'] = 0.0

		#Create Mock Values to Look for
		data_dict['Over_Bet'] = 0.0
		data_dict['Under_Bet'] = 0.0

		#Ship Data
		return data_dict


def Create_Live_Games_List(Bot):
	
	#Initialize
	# input("Press [Enter] to run scrape.")

	#Isolate Live Games
	Live_Games = []
	soup = BeautifulSoup(Bot.Driver.page_source, 'html.parser')
	Live_Container = soup.find('div', class_="happening-now-bucket") 

	#Identify individual Games
	for game in Live_Container.findAll('section', class_="coupon-content more-info"):
		#Create data dict
		data_dict = {}
		try:
			for score in game.findAll('sp-score-coupon', class_="scores"): #Find Scores in Game
				data_dict = Grab_Scores(score, data_dict)
			
			for teams in game.findAll('header', class_="event-title"): #Find Teams in Game
				data_dict = Grab_Teams(teams, data_dict)
		
			for outs in game.findAll('sp-outcomes', class_="markets-container"): #Find Outcomes in Game
				data_dict = Grab_Outcomes(outs, data_dict)
		
			#Save Data
			Live_Games.append(data_dict)
		except:
			print("[ERROR]: Unable to Create_Live_Game")
		
	#Return Games Info
	return Live_Games
	
	

def Create_Future_Games_List(Bot):
	try:
		#Initialize
		# input("Press [Enter] to run scrape.")

		#Isolate Future Games
		Future_Games = []
		soup = BeautifulSoup(Bot.Driver.page_source, 'html.parser')
		Future_Container = soup.find('div', class_="next-events-bucket") 

		#Identify individual Games
		for game in Future_Container.findAll('section', class_="coupon-content more-info"):
			#Create data dict
			data_dict = {}

			for score in game.findAll('sp-score-coupon', class_="scores"): #Find Start Time in Game
				data_dict = Grab_Future_Time(score, data_dict)
				
			for teams in game.findAll('header', class_="event-title"): #Find Teams in Game
				data_dict = Grab_Teams(teams, data_dict)
			
			for outs in game.findAll('sp-outcomes', class_="markets-container"): #Find Outcomes in Game
				data_dict = Grab_Outcomes(outs, data_dict)

			#Return Data
			Future_Games.append(data_dict)
				
		#Return Games Info
		return Future_Games, True
	except:
		print("[ERROR]: Unable to Create_Future_Games_List")
		return False
	