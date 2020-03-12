#Bovada DB Imports 
import sqlite3
from sqlite3 import Error


#DB
def Connect_to_DB(DB_PATH):
	conn = None
	try:
		conn = sqlite3.connect(DB_PATH)
		return conn
	except Error as e:
		print(e)

	return conn

def create_games_table(conn):
	try:
		sql_create_table = """ CREATE TABLE IF NOT EXISTS future_games (
										id integer PRIMARY KEY,
										Game_Date text NOT NULL,
										Today_Date text NOT NULL,
										Game_start_time text NOT NULL,
										Game_current_time text NOT NULL,
										Game_Quarter text NOT NULL,
										Team_1 text NOT NULL, 
										Team_2 text NOT NULL,
										Over_Value_Game_Start real NOT NULL,
										Over_Value_Current real NOT NULL,
										Over_Value_Target real NOT NULL, 
										Over_Value_Q1 real NOT NULL, 
										Over_Value_Q2 real NOT NULL,
										Over_Value_Q3 real NOT NULL,
										Over_Value_Q4 real NOT NULL,
										Over_Value_Bet_Status real NOT NULL, 
										Over_Value real NOT NULL, 
										Under_Value real NOT NULL
										); """
		c = conn.cursor()
		c.execute(sql_create_table)
		conn.commit()
	except Error as e:
		print(e)



def create_future_game(conn, game):
	sql = ''' INSERT INTO future_games(Game_Date,Team_1,Team_2,Over_Value,Under_Value) VALUES(?,?,?,?,?) '''
	cur = conn.cursor()
	cur.execute(sql, game)
	conn.commit()


def update_task(conn, task):
    """
    update priority, begin_date, and end date of a task
    :param conn:
    :param task:
    :return: project id
    """
    sql = ''' UPDATE tasks
              SET priority = ? ,
                  begin_date = ? ,
                  end_date = ?
              WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()



def select_all_future_games(conn, Name):
    cur = conn.cursor()
    cur.execute("SELECT * FROM {}".format(Name))
 
    rows = cur.fetchall()
 
    for row in rows:
        print(row)

def delete_future_game(conn, id):
    sql = 'DELETE FROM future_games WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()
 
 
def delete_all_future_games(conn):
    
    sql = 'DELETE FROM future_games'
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()