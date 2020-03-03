#Imports
import pandas as pd
from pandas import DataFrame
import csv

#Imports Bot
from .bot import *

#Games
Games = []


def Create_DF(Dict):
	try:
		df = DataFrame(Dict,columns = ['Start_Time', 'Team1', 'Team2', 'Over', 'Over_Bet', 'Under', 'Under_Bet']) 

		#Return
		return df
	except:
		print("[ERROR]: Unable to Create_Future_Games_CSV")
		return False


def Create_Future_Games_CSV(Bot, Dict):
	try:
		df = DataFrame(Dict,columns = ['Start_Time', 'Team1', 'Team2', 'Over', 'Over_Bet', 'Under', 'Under_Bet']) 
		
		#Save to CSV
		df.to_csv (Bot.Config_Options['SAVE_DATA']['FUTURE_DATA_PATH'], index=False, header=True)

		#Return
		return True
	except:
		print("[ERROR]: Unable to Create_Future_Games_CSV")
		return False


def Read_Future_Games_CSV(Bot):
	try:
		df = pd.read_csv(Bot.Config_Options['SAVE_DATA']['FUTURE_DATA_PATH'])

		#Return
		return df
	except:
		print("[ERROR]: Unable to Read_Future_Games_CSV")
		return False



def Create_Live_Games_CSV(Bot, Dict):
	try:
		df = DataFrame(Dict,columns = ['Team1', 'Team2', 'Over', 'Over_Bet', 'Under', 'Under_Bet', 'Score1', 'Score2', 'Quarter', 'Time']) 
		
		#Save to CSV
		df.to_csv (Bot.Config_Options['SAVE_DATA']['LIVE_DATA_PATH'], index=False, header=True)

		#Return
		return True
	except:
		print("[ERROR]: Unable to Create_Live_Games_CSV")
		return False


def Read_Live_Games_CSV(Bot):
	try:
		df = pd.read_csv(Bot.Config_Options['SAVE_DATA']['LIVE_DATA_PATH'])

		#Return
		return df
	except:
		print("[ERROR]: Unable to Read_Live_Games_CSV")
		return False