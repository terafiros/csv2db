import csv
import pyodbc
import mysql.connector
import psycopg2



'''configurações da conexão com o servidor SQL SERVER'''
'''
conn = pyodbc.connect('Driver={SQL Server};'
					  'Server=DESKTOP-476CGTK;'
					  'Database=test;'
                    'Trusted_Connection=yes;'
					  )



conn = mysql.connector.connect(host='localhost',
							   database='test',
							   user='root',
							   password='root')
'''

conn = psycopg2.connect(host='localhost',
						database='test',
						user='postgres',
						password='root'
						)

cursor = conn.cursor()
print('connected')

#colunas a serem inseridas
values_to_insert =  ['age','sex','trestbps','chol','fbs','thalach']

#heart.csv é o arquivo com os dados o encoding deve ser mudado caso haja erro nos nomes dos campos
#a primeira linha do csv deve ser os nome dos campos
#no line[XXXX] é devem ir os nomes das colunas na mesma ordaded de values_to_insert

sex = {'1':'M', '0':'F'}

with open('heart.csv', encoding='utf-8-sig') as csvfile:
	reader = csv.DictReader(csvfile)
	print(reader.fieldnames)
	for line in reader:
		insert_sql_server = f'''INSERT INTO test.dbo.Paciente({','.join(values_to_insert)})
		            VALUES
		                ({line['age']},{line['sex']},{line['trestbps']},{line['chol']},{line['fbs']},{line['thalach']})
		        '''

		insert_mysql = f'''INSERT INTO paciente({','.join(values_to_insert)})
		            VALUES
		                ({line['age']},{line['sex']},{line['trestbps']},{line['chol']},{line['fbs']},{line['thalach']})
		        '''

		insert_postgresql = f'''INSERT INTO Paciente({','.join(values_to_insert)})
		            VALUES
		                ({line['age']},'{sex[line['sex']]}',{line['trestbps']},{line['chol']},{line['fbs']},{line['thalach']})
		        '''
		cursor.execute(insert_postgresql)

print('finalizando conexão')
conn.commit()

print('finalizando')
conn.close()

