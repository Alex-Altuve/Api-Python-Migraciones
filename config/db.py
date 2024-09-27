from sqlalchemy import create_engine, MetaData

#Te permite conectarte a postgresql
# engine = create_engine('postgresql+psycopg2://user:password@hostname:puerto/database_name')

#Otra opcion de conexcion mas facil
#import psycopg2
# conn_string = "host='localhost' dbname='my_database' user='postgres' password='secret'"
# conn = psycopg2.connect(conn_string)

engine = create_engine("postgresql://postgres:adminadmin@localhost:5432/Practica_Python")

meta = MetaData()
conn = engine.connect()
