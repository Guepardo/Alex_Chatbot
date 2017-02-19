import MySQLdb

class Database:
	def __init__(cls):
		cls.db = MySQLdb.connect(host='127.0.0.1', 
			user='root', 
			passwd='phprs',
			db='bot')

	def get_cursor(cls): 
		return cls.db.cursor()	

	def execute(cls, query): 
		cur = cls.db.cursor()
		cur.execute(query)
		return cur.fetchall()

	def close(cls):
		cls.db.close() 