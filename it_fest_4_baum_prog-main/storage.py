import sqlite3 # structered query language
# реляционная база данных (relation)

class Storage:
	def __init__(self): #конструктор, вызывается при создании
		self.cnct = sqlite3.connect('data.db') # connect
		self.crs = self.cnct.cursor() # crs - cursor
		self.create_table()

	def create_table(self):
		self.crs = self.cnct.execute('''CREATE TABLE IF NOT EXISTS score_table (
											name text, score int		)''')

	def insert_into(self, name_usr, score):
		self.crs.execute(f'''INSERT INTO score_table (name, score) # f чтобы в строку можно было внести переменную
								VALUES('{name_usr}', '{score}')''')
		self.cnct.commit()

	def select_all(self):
		self.crs.execute('''SELECT * FROM score_table ''')
		return self.crs.fetchall()

	def __del__(self):# деструктор, вызывается при уничтожении
		self.cnct.close()
