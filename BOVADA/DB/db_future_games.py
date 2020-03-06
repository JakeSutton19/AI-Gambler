import sqlite3
from sqlite3 import Error
 
 
def create_future_games_table(conn):
	try:
		sql_create_table = """ CREATE TABLE IF NOT EXISTS future_games (
										id integer PRIMARY KEY,
										Start_Time text NOT NULL,
										Team_1 text NOT NULL, 
										Team_2 text NOT NULL,
										Over_Value integer NOT NULL, 
										Under_Value integer NOT NULL
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


def select_all_future_games(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM future_games")
 
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