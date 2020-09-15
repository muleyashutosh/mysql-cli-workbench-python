import mysql.connector


class Workbench:
    def __init__(self, database, host = 'localhost', user = 'root', password = ''):
        self.user = user
        self.host = host
        self.database= database
        self.password = password
        self.connectDB()
    
    def connectDB(self):
        self.conn = mysql.connector.connect(host = self.host,
                                        user = self.user,
                                        password = self.password,
                                        database = self.database)

    def showTables(self):
        curr = self.conn.cursor() 
        query = 'SHOW TABLES;'
        curr.execute(query)
        return curr.fetchall()
    
    def dropTable(self, tablename):
        query = 'DROP TABLE ' + tablename
        curr = self.conn.cursor()
        curr.execute(query)
    
    def selectFrom(self, tablename, attributes = [], whereClause = {}, key = 'AND'):
        key = " " + key + " "

        if len(attributes) == 0:
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
        curr = self.conn.cursor()
        curr.execute(search)
        return curr.fetchall()

    def deleteFrom(self, tablename, whereClause = {}, key = 'AND'):
        key = ' ' + key + ' '
        
        where = [k + ' = "' + v + '"'for k,v in whereClause.items()]
        where = key.join(where)
        query = 'DELETE FROM ' + tablename + ' WHERE ' + where
        #print(query)
        curr = self.conn.cursor()
        curr.execute(query);
        self.conn.commit()

    def UpdateTable(self, tablename, updates, whereClause = {}, key = 'AND'):
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
        curr = self.conn.cursor()
        curr.execute(query)
        self.conn.commit()