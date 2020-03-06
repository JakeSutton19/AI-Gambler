#Bovada DB Imports 
import sqlite3
from sqlite3 import Error


#DB
def Bovada_DB(DB):
	conn = None
	try:
		conn = sqlite3.connect(DB)
		return conn
	except Error as e:
		print(e)

	return conn

def create_upcoming_games_table(conn):
	try:
		sql_create_table = """ CREATE TABLE IF NOT EXISTS Upcoming_Games (
										id integer PRIMARY KEY,
										League text NOT NULL,
										Start_Time numeric NOT NULL,
										Team_1 text NOT NULL, 
										Team_2 text NOT NULL,
										Over_Value real NOT NULL, 
										Under_Value real NOT NULL
										); """
		c = conn.cursor()
		c.execute(sql_create_table)
	except Error as e:
		print(e)


def create_live_games_table(conn):
	try:
		sql_create_table = """ CREATE TABLE IF NOT EXISTS live_games (
										id integer PRIMARY KEY,
										game_id integer NOT NULL,
										League text NOT NULL,
										Start_Time numeric NOT NULL,
										Overall_time numeric NOT NULL,
										Quarter integer NOT NULL,
										Team_1 text NOT NULL, 
										Team_2 text NOT NULL,
										Over_Start_Value real NOT NULL, 
										Over_Bet_Target real NOT NULL, 
										Over_Current_Value real NOT NULL, 
										Under_Start_Value real NOT NULL, 
										Under_Bet_Target real NOT NULL, 
										Under_Current_Value real NOT NULL,
										game_status text NOT NULL
										); """
		c = conn.cursor()
		c.execute(sql_create_table)
	except Error as e:
		print(e)



def create_future_game(conn, game):
	sql = ''' INSERT INTO future_games(Start_Time,Team_1,Team_2,Over_Value,Under_Value) VALUES(?,?,?,?,?) '''
	cur = conn.cursor()
	cur.execute(sql, game)
	return cur.lastrowid