import argparse, csv
import getpass
import pyodbc
from actions import SGBDAction

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('sgbd',choices=['sqlserver', 'mysql', 'postgresql'], action=SGBDAction)
	parser.add_argument('csv', type=argparse.FileType('r', encoding='utf-8-sig'))

	namespace = parser.parse_args()

	reader = csv.DictReader(namespace.csv)
	for line in reader:
		namespace.sgbd.insert(line.keys(), line.values())

	namespace.connection.commit()
	namespace.connection.close()
