import sqlite3
from sqlite3 import Error
 
 
def create_connection(db_file):
	""" create a database connection to the SQLite database specified by db_file
	#:param db_file: database file
	#:return: Connection object or None
	"""
	conn = None
	try:
		conn = sqlite3.connect(db_file)
		return conn
	except Error as e:
		print(e)

	return conn
 
 
def create_table(conn, create_table_sql):
	""" create a table from the create_table_sql statement
	:param conn: Connection object
	:param create_table_sql: a CREATE TABLE statement
	:return:
	"""
	try:
		c = conn.cursor()
		c.execute(create_table_sql)
	except Error as e:
		print(e)

 
def create_project(conn, project):
	"""
	Create a new project into the projects table
	:param conn:
	:param project:
	:return: project id
	"""
	sql = ''' INSERT INTO projects(name,begin_date,end_date) VALUES(?,?,?) '''
	cur = conn.cursor()
	cur.execute(sql, project)
	return cur.lastrowid


def create_task(conn, task):
	"""
	Create a new task
	:param conn:
	:param task:
	:return:
	"""

	sql = ''' INSERT INTO tasks(name,priority,status_id,project_id,begin_date,end_date) VALUES(?,?,?,?,?,?) '''
	cur = conn.cursor()
	cur.execute(sql, task)
	return cur.lastrowid


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

 
def select_all_tasks(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks")
 
    rows = cur.fetchall()
 
    for row in rows:
        print(row)
 
 
def select_task_by_priority(conn, priority):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks WHERE priority=?", (priority,))
 
    rows = cur.fetchall()
 
    for row in rows:
        print(row)
 

def delete_task(conn, id):
    """
    Delete a task by task id
    :param conn:  Connection to the SQLite database
    :param id: id of the task
    :return:
    """
    sql = 'DELETE FROM tasks WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()
 
 
def delete_all_tasks(conn):
    """
    Delete all rows in the tasks table
    :param conn: Connection to the SQLite database
    :return:
    """
    sql = 'DELETE FROM tasks'
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()


 
def main(db):
    database = db

    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS projects (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        begin_date text,
                                        end_date text
                                    ); """
 
    sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS tasks (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    priority integer,
                                    status_id integer NOT NULL,
                                    project_id integer NOT NULL,
                                    begin_date text NOT NULL,
                                    end_date text NOT NULL,
                                    FOREIGN KEY (project_id) REFERENCES projects (id)
                                );"""
                                
 
    # create a database connection
    conn = create_connection(database)
    with conn:
        print("1. Query task by priority:")
        # select_task_by_priority(conn, 1)
 		
        # delete_task(conn, 1)

        print("2. Query all tasks")
        select_all_tasks(conn)


# if __name__ == '__main__':
# 	main("/home/human/AI-Gambler/CONFIG/Database/test.db")