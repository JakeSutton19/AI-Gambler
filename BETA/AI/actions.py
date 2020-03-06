# Bovada Bot 
# - written by Jacob Sutton

#--------------------------------------------------------------------- IMPORTS ---------------------------------------------------------------------#
#Imports (General)
import time

#Bovada Imports
from .Build.__init__ import *
from .Bovada.__init__ import *
from .Database.__init__ import *


#Euroleague Schedule
def Create_Euroleague_Schedule(Bot, DB):
	try:
		#Navigate to Basketball Home
		Nav_to_Euroleague_Page(Bot)
		time.sleep(1)

		#Scrape the Page
		future_games = Create_Future_Games_List(Bot)

		#Create DF
		future_games_df = Create_Future_Games_DF(future_games)

		#Save CSV
		Create_Future_Games_CSV(Bot, future_games_df, 'EUROLEAGUE_PATH')

		#Add df to DB
		future_games_df.to_sql('future_euro_games', DB, if_exists='replace', index = True)
	except:
		Error_Message("Unable to Future Create_Euroleague_Schedule")

	try:
		#Scrape the Page
		live_games = Create_Live_Games_List(Bot)

		#Create DF
		live_games_df = Create_Live_Games_DF(live_games)

		#Save CSV
		Create_Live_Games_CSV(Bot, live_games_df, 'EUROLEAGUE_PATH')

		#Add df to DB
		live_games_df.to_sql('live_euro_games', DB, if_exists='replace', index = True)
	except:
		Error_Message("Unable to Live Create_Euroleague_Schedule")
		
	

#Argentina Schedule
def Create_Argentina_Schedule(Bot, DB):
	try:
		#Navigate to Basketball Home
		Nav_to_Argentina_Page(Bot)
		time.sleep(1)

		#Scrape the Page
		future_games = Create_Future_Games_List(Bot)

		#Create DF
		future_games_df = Create_Future_Games_DF(future_games)

		#Save CSV
		Create_Future_Games_CSV(Bot, future_games_df, 'ARGENTINA_PATH')

		#Add df to DB
		future_games_df.to_sql('future_argentina_games', DB, if_exists='replace', index = True)
	except:
		Error_Message("Unable to Future Create_Argentina_Schedule")

	try:
		#Scrape the Page
		live_games = Create_Live_Games_List(Bot)

		#Create DF
		live_games_df = Create_Live_Games_DF(live_games)

		#Save CSV
		Create_Live_Games_CSV(Bot, live_games_df, 'ARGENTINA_PATH')

		#Add df to DB
		live_games_df.to_sql('live_argentina_games', DB, if_exists='replace', index = True)

	except:
		Error_Message("Unable to Live Create_Argentina_Schedule")
	


#South Korea Schedule
def Create_SK_Schedule(Bot, DB):
	try:
		#Navigate to Basketball Home
		Nav_to_SK_Page(Bot)
		time.sleep(1)

		#Scrape the Page
		future_games = Create_Future_Games_List(Bot)

		#Create DF
		future_games_df = Create_Future_Games_DF(future_games)

		#Save CSV
		Create_Future_Games_CSV(Bot, future_games_df, 'SK_PATH')

		#Add df to DB
		future_games_df.to_sql('future_sk_games', DB, if_exists='replace', index = True)
	except:
		Error_Message("Unable to Future Create_SK_Schedule")

	try:
		#Scrape the Page
		live_games = Create_Live_Games_List(Bot)

		#Create DF
		live_games_df = Create_Live_Games_DF(live_games)

		#Save CSV
		Create_Live_Games_CSV(Bot, live_games_df, 'SK_PATH')

		#Add df to DB
		live_games_df.to_sql('live_sk_games', DB, if_exists='replace', index = True)
	except:
		Error_Message("Unable to Live Create_SK_Schedule")

		


#NBA Schedule
def Create_NBA_Schedule(Bot, DB):
	try:
		#Navigate to Basketball Home
		Nav_to_NBA_Page(Bot)
		time.sleep(1)

		#Scrape the Page
		future_games = Create_Future_Games_List(Bot)

		#Create DF
		future_games_df = Create_Future_Games_DF(future_games)

		#Save CSV
		Create_Future_Games_CSV(Bot, future_games_df, 'NBA_PATH')

		#Add df to DB
		future_games_df.to_sql('future_nba_games', DB, if_exists='replace', index = True)
	except:
		Error_Message("Unable to Future Create_NBA_Schedule")

	try:
		#Scrape the Page
		live_games = Create_Live_Games_List(Bot)

		#Create DF
		live_games_df = Create_Live_Games_DF(live_games)

		#Save CSV
		Create_Live_Games_CSV(Bot, live_games_df, 'NBA_PATH')

		#Add df to DB
		live_games_df.to_sql('live_nba_games', DB, if_exists='replace', index = True)
	except:
		Error_Message("Unable to Live Create_NBA_Schedule")
