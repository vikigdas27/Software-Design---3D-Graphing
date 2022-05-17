#Neil i swear to god if you delete this again
#Neil ongod I'll commit a warcrime if you delete something you don't understand
import sqlite3
from time import time

def setupDatabase(db_file):
	con = sqlite3.connect(db_file)
	db = con.cursor()
	#None of this is in any way secure
	createUsersTable = """
	CREATE TABLE users( 
	username text UNIQUE NOT NULL,
	password text NOT NULL
	)"""
	createEquationsTable = """
	CREATE TABLE equations( 
	username text NOT NULL,
	equation text UNIQUE NOT NULL,
	date text NOT NULL
	)"""
	createHistoryTable = """
	CREATE TABLE history(
	username text NOT NULL,
	equation text NOT NULL,
	date text NOT NULL
	)"""
	db.execute(createUsersTable)
	print("Table Created: users")
	db.execute(createEquationsTable)
	print("Table Created: equations")
	db.execute(createHistoryTable)
	print("Table Created: history")
	con.commit()
	con.close()
	
def execute(query, params):
	con = sqlite3.connect("database.db")
	db = con.cursor()
	try:
		db.execute(query, params)
		rows = db.fetchall()
		con.commit()
		return rows
	except sqlite3.Error as err:
		print('SQLite error: %s' % (' '.join(err.args)))
		return err
	finally:
		con.close()
	
def getSaved(username):
	query = "SELECT * FROM equations WHERE username = ?"
	res = execute(query, [username])
	print(res)
	return res
	
def addSaved(username, equation):
	query = "INSERT INTO equations VALUES(?, ?, ?)"
	res = execute(query, [username, equation, int(time()*1000)])
	print(res)

def removeSaved(username, equation):
	query = "DELETE FROM equations WHERE username = ? AND equation = ?"
	res = execute(query, [username, equation])
	print(res)
	
def test(equation):
	print("Adding equation:")
	addSaved("billybob", equation)
	print("Retrieving equations:")
	getSaved("billybob")
	print("Deleting saves: ")
	removeSaved("billybob", equation)
	print("Retrieving equations:")
	getSaved("billybob")
if __name__ == '__main__':
	setupDatabase("database.db")