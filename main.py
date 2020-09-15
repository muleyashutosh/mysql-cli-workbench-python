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

def dropTable(conn, tablename):
    query = 'DROP TABLE ' + tablename
    curr = conn.cursor()
    curr.execute(query)

# SELECT atribute1,atribute2,... FROM tablename WHERE ... = ... ;
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
    
    where = [k + ' = "' + v + '"'for k,v in whereClause.items()]
    where = key.join(where)
    query = 'DELETE FROM ' + tablename + ' WHERE ' + where
    #print(query)
    curr = conn.cursor()
    curr.execute(query);
    conn.commit()

# UPDATE tablename SET ... = ... WHERE ... = ... ;
def UpdateTable(conn, tablename, updates, whereClause = {}, key = 'AND'):
    key = ' ' + key + ' '
    updates = [k + ' = "' + v + '"' for k, v in updates.items()]
    updates = ', '.join(updates)

    if whereClause :
        where  = [k + ' = "' + v + '"' for k, v in whereClause.items()]
        where = key.join(where)
        query = 'UPDATE ' + tablename + ' SET ' + updates + ' WHERE ' + where
    else :
        query = 'UPDATE ' + tablename + ' SET ' + updates
        
    #print(query)
    curr = conn.cursor()
    curr.execute(query)
    conn.commit()

# def createTable(conn,tablename,columns, pkey = ''):
#     columns = [ k + ' ' + v for k, v in columns.items()]
#     columns = ', '.join(columns)
#     if pkey:
#         columns += ', PRIMARY KEY('+ pkey + ')'
        
#     query = 'CREATE TABLE ' + tablename + ' ( ' + columns + ' );'
#     curr = conn.cursor()
#     curr.execute(query)



conn = connectDB('Sample')
tablename = 'employee'

# display tables
result = showTables(conn)
for x in result:
    print(x)
print('_______________________________')

# deleteFrom('employee', conn, where,'AND')
# print('_______________________________')

# updates = { 'firstname': 'Ashutosh', 'lastname' : 'Muley'}
# where= { 'firstname': 'Lynn', 'lastname' : 'Dennis'}
# UpdateTable(conn, tablename, updates, where)

# print('_______________________________')

# result = selectFrom(tablename, conn, attibutes, {}, 'AND')

# for x in result:
#     print(x)
 # create tables



result = showTables(conn)
for x in result:
    print(x)
print('_______________________________')





