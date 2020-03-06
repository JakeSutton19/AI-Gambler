#Bovada DB Imports 
import sqlite3
from sqlite3 import Error



#DB
def DB_Connect(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn







 
def main(db):
    database = db

    # sql_create_future_game_table = """ CREATE TABLE IF NOT EXISTS future_game (
    #                                     id integer PRIMARY KEY,
    #                                     Start_Time text NOT NULL,
    #                                     Team_1 text NOT NULL, 
    #                                     Team_2 text NOT NULL,
    #                                     Over_Value integer NOT NULL, 
    #                                     Under_Value integer NOT NULL
    #                                 ); """
 
    # sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS tasks (
    #                                 id integer PRIMARY KEY,
    #                                 name text NOT NULL,
    #                                 priority integer,
    #                                 status_id integer NOT NULL,
    #                                 project_id integer NOT NULL,
    #                                 begin_date text NOT NULL,
    #                                 end_date text NOT NULL,
    #                                 FOREIGN KEY (project_id) REFERENCES projects (id)
    #                             );"""
                                
 
    # create a database connection
    conn = create_connection(database)
    with conn:
        print("Creating Game")
        game = ('11:00', 'Test Team 1', 'Test Team 2', 30, 20)
        create_future_game(conn, game)
        print("Future Games: ")
        select_all_future_games(conn)
        


if __name__ == '__main__':
    main("/home/human/AI-Gambler/CONFIG/Data/Databases/test.db")



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
 
 
def delete_all_tasks(conn):
    
    sql = 'DELETE FROM tasks'
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()


# def update_future_game(conn, task):
# 	"""
# 	update priority, begin_date, and end date of a task
# 	:param conn:
# 	:param task:
# 	:return: project id
# 	"""
# 	sql = ''' UPDATE tasks
# 	          SET priority = ? ,
# 	              begin_date = ? ,
# 	              end_date = ?
# 	          WHERE id = ?'''
# 	cur = conn.cursor()
# 	cur.execute(sql, task)
# 	conn.commit()

 

 
 
# def select_task_by_priority(conn, priority):
#     """
#     Query tasks by priority
#     :param conn: the Connection object
#     :param priority:
#     :return:
#     """
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM tasks WHERE priority=?", (priority,))
 
#     rows = cur.fetchall()
 
#     for row in rows:
#         print(row)
 



