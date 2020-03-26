import pyodbc, mysql.connector, psycopg2
import getpass


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

class MySQL:


    def __init__(self, host = None, database = None, user = None, password = None, **kwargs):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection_sting = None
        self.connection = None

    def get_data_for_connection(self):
        self.host = input('HOST: ')
        self.database = input('DATABASE: ')
        self.table = input('TABLE: ')
        self.user = input('USER: ')
        self.password = getpass.getpass()

        self.connection_sting = f'''host={self.host}, database={self.database}, user={self.user}, table={self.table}, password=****************'''

        return self.connection_sting

    def make_connection(self):
        if self.connection:
            return self.connection
        self.connection = mysql.connector.connect(
            host=self.host,
            database=self.database,
            user=self.user,
            password=self.password
        )
        self.cursor = self.connection.cursor()
        return self.connection

    def insert(self, columns, values):
        insert_string = f"""INSERT INTO {self.table} ({','.join(columns)}) VALUES ({','.join(values)});"""
        self.cursor.execute(insert_string)

class PostgreSQL:
    def __init__(self, host = None, database = None, user = None, password = None, **kwargs):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection_sting = None
        self.connection = None

    def get_data_for_connection(self):
        self.host = input('HOST: ')
        self.database = input('DATABASE: ')
        self.table = input('TABLE: ')
        self.user = input('USER: ')
        self.password = getpass.getpass()

        self.connection_sting = f'''host={self.host}, database={self.database}, user={self.user}, table={self.table}, password=****************'''

        return self.connection_sting

    def make_connection(self):
        if self.connection:
            return self.connection
        self.connection = psycopg2.connect(
            host=self.host,
            database=self.database,
            user=self.user,
            password=self.password
        )
        self.cursor = self.connection.cursor()
        return self.connection

    def insert(self, columns, values):
        insert_string = f"""INSERT INTO {self.table} ({','.join(columns)}) VALUES ({','.join(values)});"""
        self.cursor.execute(insert_string)
