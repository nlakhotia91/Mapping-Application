import psycopg2
import sys
import pandas as pd
import sqlalchemy as sq
import os.path
path = 'C:\\Users\\malaniaayushi\\Desktop\\dec\\'
engine = sq.create_engine("postgresql+psycopg2://postgres:resra@!$3@139.162.17.147/appdev_backup")

	#Define our connection string
conn_string = "host='139.162.17.147' dbname='appdev_backup' user='postgres' password='resra@!$3'"
 
	# print the connection string we will use to connect
print "Connecting to database\n	->%s" % (conn_string)
 
	# get a connection, if a connect cannot be made an exception will be raised here
conn = psycopg2.connect(conn_string)
    # conn.cursor will return a cursor object, you can use this cursor to perform queries
cursor = conn.cursor()
print "Connected!\n"
cursor.execute("""SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'""")    
rows = cursor.fetchall()

for row in rows:
    print row
    if os.path.exists(path+row[0]+'.csv'):
        print 'exists'
        continue
    else:    
        table = pd.read_sql_table(row[0],engine) ##reads table from postgres and stores it in dataframe
        table.to_csv(path+row[0]+'.csv')## dataframe to csv file on local computer
        
        


        