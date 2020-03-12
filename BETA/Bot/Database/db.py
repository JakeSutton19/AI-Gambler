#Bovada DB Imports 
import sqlite3
from sqlite3 import Error


#DB
def Init_DB(DB_PATH):
	conn = None
	try:
		conn = sqlite3.connect(DB_PATH)
		return conn
	except Error as e:
		print(e)

	return conn

# def create_games_table(conn):
# 	try:
# 		sql_create_table = """ CREATE TABLE IF NOT EXISTS future_games (
# 										id integer PRIMARY KEY,
# 										Game_Date text NOT NULL,
# 										Today_Date text NOT NULL,
# 										Game_start_time text NOT NULL,
# 										Game_current_time text NOT NULL,
# 										Game_Quarter text NOT NULL,
# 										Team_1 text NOT NULL, 
# 										Team_2 text NOT NULL,
# 										Over_Value_Game_Start real NOT NULL,
# 										Over_Value_Current real NOT NULL,
# 										Over_Value_Target real NOT NULL, 
# 										Over_Value_Q1 real NOT NULL, 
# 										Over_Value_Q2 real NOT NULL,
# 										Over_Value_Q3 real NOT NULL,
# 										Over_Value_Q4 real NOT NULL,
# 										Over_Value_Bet_Status real NOT NULL, 
# 										Over_Value real NOT NULL, 
# 										Under_Value real NOT NULL
# 										); """
# 		c = conn.cursor()
# 		c.execute(sql_create_table)
# 		conn.commit()
# 	except Error as e:
# 		print(e)


# def create_live_games_table(conn):
# 	try:
# 		sql_create_table = """ CREATE TABLE IF NOT EXISTS live_games (
# 										id integer PRIMARY KEY,
# 										game_id integer NOT NULL,
# 										League text NOT NULL,
# 										Start_Time numeric NOT NULL,
# 										Overall_time numeric NOT NULL,
# 										Quarter integer NOT NULL,
# 										Team_1 text NOT NULL, 
# 										Team_2 text NOT NULL,
# 										Over_Start_Value real NOT NULL, 
# 										Over_Bet_Target real NOT NULL, 
# 										Over_Current_Value real NOT NULL, 
# 										Under_Start_Value real NOT NULL, 
# 										Under_Bet_Target real NOT NULL, 
# 										Under_Current_Value real NOT NULL,
# 										game_status text NOT NULL
# 										); """
# 		c = conn.cursor()
# 		c.execute(sql_create_table)
# 	except Error as e:
# 		print(e)



# def create_future_game(conn, game):
# 	sql = ''' INSERT INTO future_games(Game_Date,Team_1,Team_2,Over_Value,Under_Value) VALUES(?,?,?,?,?) '''
# 	cur = conn.cursor()
# 	cur.execute(sql, game)
# 	conn.commit()



# def select_all_future_games(conn, Name):
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM {}".format(Name))
 
#     rows = cur.fetchall()
 
#     for row in rows:
#         print(row)

# def delete_future_game(conn, id):
#     sql = 'DELETE FROM future_games WHERE id=?'
#     cur = conn.cursor()
#     cur.execute(sql, (id,))
#     conn.commit()
 
 
# def delete_all_future_games(conn):
    
#     sql = 'DELETE FROM future_games'
#     cur = conn.cursor()
#     cur.execute(sql)
#     conn.commit()