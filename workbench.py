import mysql.connector
from dotenv import load_dotenv
import os 

load_dotenv()

def connectDB(database):
    user = 'muleyashutosh'
    password = os.getenv('mySQL_muleyashutosh_password')
    #print(password)
    host = 'localhost'
    database = database
    conn = mysql.connector.connect(host = host,
                                    user = user,
                                    password = password,
                                    database = database)
    return conn

def showTables(conn):
    curr = conn.cursor() 
    query = 'SHOW TABLES;'
    curr.execute(query)
    return curr.fetchall()



def selectFrom(tablename, conn, attributes, whereClause, key):
    key = " " + key + " "

    if len(attibutes) == 0:
        attr = '*'
    else:
        attr = ",".join(attributes)

    whereClause = [ k + ' = "' + v + '"' for k,v in whereClause.items() ]

    if len(whereClause) == 0:
        where = ";"
    else:
        where = " WHERE " + key.join(whereClause) + ';'
    search = 'SELECT ' + attr + ' FROM ' + tablename + where

    #print(search)
    curr = conn.cursor()
    curr.execute(search)
    return curr.fetchall()


#DELETE FROM tablename WHERE 
def deleteFrom(tablename, conn, whereClause, key):
    key = ' ' + key + ' '
    
    where = [k + '= "' + v + '"'for k,v in whereClause.items()]
    where = key.join(where)
    query = 'DELETE FROM ' + tablename + ' WHERE ' + where;
    #print(query)
    curr = conn.cursor()
    curr.execute(query);
    conn.commit()


conn = connectDB('Sample')
db = 'employee'

#display tables
# result = showTables(conn)
# for x in result:
#     print(x)
    
#select query 
attibutes = ['firstname', 'middlename', 'lastname']
where = {}
result = selectFrom(db, conn, attibutes, where, 'AND')

for x in result:
    print(x)

where = {'firstname': 'Leslie','lastname': 'Baker' }

deleteFrom('employee', conn, where,'AND')
print('_______________________________')
result = selectFrom(db, conn, attibutes, {}, 'AND')




for x in result:
    print(x)

