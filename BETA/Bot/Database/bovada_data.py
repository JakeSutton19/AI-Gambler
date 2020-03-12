#Imports
import pandas as pd
from pandas import DataFrame
import csv

#Games
Games = []



def Create_Games_DF(Dict):
	try:
		df = DataFrame(Dict,columns = ['Date', 'Time', 'Quarter', 'Team1', 'Team2', 'Over', 'Over_Bet', 'Under', 'Under_Bet', 'Score1', 'Score2']) 

		#Return
		return df
	except:
		print("[ERROR]: Unable to Create_Future_Games_DF")
		return False

def Create_Games_CSV(Bot, df, File):
	try:
		#Save to CSV
		df.to_csv(Bot.Config_Options['FUTURE_DATA'][File], index=False, header=True)

		#Return
		return True
	except:
		print("[ERROR]: Unable to Create_Future_Games_CSV")
		return False


def Create_Future_Games_DF(Dict):
	try:
		df = DataFrame(Dict,columns = ['Date', 'Team1', 'Team2', 'Over', 'Over_Bet', 'Under', 'Under_Bet']) 

		#Return
		return df
	except:
		print("[ERROR]: Unable to Create_Future_Games_DF")
		return False


def Create_Future_Games_CSV(Bot, df, File):
	try:
		#Save to CSV
		df.to_csv(Bot.Config_Options['FUTURE_DATA'][File], index=False, header=True)

		#Return
		return True
	except:
		print("[ERROR]: Unable to Create_Future_Games_CSV")
		return False


def Read_Future_Games_CSV(Bot, File):
	try:
		df = pd.read_csv(Bot.Config_Options['FUTURE_DATA'][File])

		#Return
		return df
	except:
		print("[ERROR]: Unable to Read_Future_Games_CSV")
		return False



def Create_Live_Games_DF(Dict):
	try:
		df = DataFrame(Dict,columns = ['Time', 'Quarter', 'Team1', 'Team2', 'Over', 'Over_Bet', 'Under', 'Under_Bet', 'Score1', 'Score2']) 

		#Return
		return df
	except:
		print("[ERROR]: Unable to Create_Live_Games_CSV")
		return False


def Create_Live_Games_CSV(Bot, df, File):
	try:
		#Save to CSV
		df.to_csv (Bot.Config_Options['LIVE_DATA'][File], index=False, header=True)

		#Return
		return True
	except:
		print("[ERROR]: Unable to Create_Live_Games_CSV")
		return False


def Read_Live_Games_CSV(Bot, File):
	try:
		df = pd.read_csv(Bot.Config_Options['LIVE_DATA'][File])

		#Return
		return df
	except:
		print("[ERROR]: Unable to Read_Live_Games_CSV")
		return False


def Sql_to_DF(DB, game_table):
	try:
		df = pd.read_sql_query("SELECT * from {}".format(game_table), DB)

		#Return
		return df
	except:
		print("[ERROR]: Unable to Sql_to_DF")
		return False