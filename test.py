import argparse
import getpass
import pyodbc
import csv

class PasswordAction(argparse.Action):
	def __init__(self, option_strings, dest, nargs='?', **kwargs):
		super(PasswordAction, self).__init__(option_strings, dest, nargs, **kwargs)

	def  __call__(self, parser, namespace, values, option_string=None):
		password = getpass.getpass()
		setattr(namespace, self.dest, password)

class SQLServer:
	def __init__(self, server = None, database = None, **kwargs):
		self.server = server
		self.database = database
		self.driver = 'Driver={SQL Server};'
		self.trusted = 'Trusted_Connection=yes;'
		self.connection_sting = None
		self.connection = None

	def get_data_for_connection(self):
		self.server = input('SERVER: ')
		self.database = input('DATABASE: ')
		self.table = input('TABLE: ')
		self.connection_sting = self.driver + 'SERVER=' + self.server + ';' + 'DATABASE=' + self.database + ';' + self.trusted

		return self.connection_sting

	def make_connection(self):
		if self.connection:
			return self.connection
		self.connection = pyodbc.connect(self.connection_sting)
		self.cursor = self.connection.cursor()
		return self.connection

	def insert(self, columns, values):
		insert_string = f"""INSERT INTO {self.table} ({','.join(columns)}) VALUES ({','.join(values)});"""
		self.cursor.execute(insert_string)


class SGBDAcion(argparse.Action):
	def __init__(self, option_strings, dest, nargs='?', **kwargs):
		super(SGBDAcion, self).__init__(option_strings, dest, nargs, **kwargs)
		self.sgbds = {'sqlserver': SQLServer()}

	def __call__(self, parser, namespace, values, option_string=None):
		sgbd = self.sgbds[values]
		connection_string = sgbd.get_data_for_connection()
		connection = sgbd.make_connection()
		setattr(namespace, 'connection_string', connection_string)
		setattr(namespace, 'connection', connection)
		setattr(namespace, 'sgbd', sgbd)



if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('sgbd',choices=['sqlserver', 'mysql', 'postgresql'], action=SGBDAcion)
	parser.add_argument('csv', type=argparse.FileType('r', encoding='utf-8-sig'))

	namespace = parser.parse_args()

	reader = csv.DictReader(namespace.csv)
	for line in reader:
		namespace.sgbd.insert(line.keys(), line.values())

	namespace.connection.commit()
	namespace.connection.close()
