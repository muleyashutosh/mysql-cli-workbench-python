"""
MySQL Workbench Module
"""

import mysql.connector


class Workbench:
    """
    MySQL Workbench Class
    """
    def __init__(self, database, host='localhost', user='root', password=''):
        """
        INPUT: database name, hostname(default = localhost),
                    username(default = 'root'), password
        This function will initialize the Workbench class with basic parameters
        for creating connection. Connection will be created and stored in 'conn'
        attribute.
        """
        self.user = user
        self.host = host
        self.database = database
        self.password = password
        self.connect_db()


    def connect_db(self):
        """
        This function creates the connection to the database using the mysql
        connector for python and initilizes the conn.
        RETURNS: None
        """
        self.conn = mysql.connector.connect(host=self.host,
                                            user=self.user,
                                            password=self.password,
                                            database=self.database)


    def show_tables(self):
        """
        This function will execute the SHOW TABLES query and return the
        result as a list of tuples.
        RETURNS: list of tuples.
        """
        curr = self.conn.cursor()
        query = 'SHOW TABLES;'
        curr.execute(query)
        return curr.fetchall()


    def drop_table(self, tablename):
        """
        Function to delete tables from our selected database
        INPUT: tablename to be deleted
        RETURNS: None
        """
        query = 'DROP TABLE ' + tablename
        curr = self.conn.cursor()
        curr.execute(query)


    def select_from(self, tablename, attributes=None, where_clause=None, key='AND'):
        """
        This function will execute the SELECT query to select particular
        attributes from the table along with checking the where clause
        conditions.
        INPUT: tablename(string), attributes (list of strings),
                where_clause(dictionary of key-Value pairs to be matched),
                key(default= AND) to be placed between where items.
        RETURNS: Result of the query as a list of tuples.
        """
        key = " " + key + " "
        if attributes is None:
            attr = '*'
        else:
            attr = ",".join(attributes)
        if where_clause is None:
            where = ";"
        else:
            where_clause = [k + ' = "' + v + '"' for k, v in where_clause.items()]
            where = " WHERE " + key.join(where_clause) + ';'
        search = 'SELECT ' + attr + ' FROM ' + tablename + where
        curr = self.conn.cursor()
        curr.execute(search)
        return curr.fetchall()


    def delete_from(self, tablename, where_clause=None, key='AND'):
        """
        Function to delete rows from the table matching the where clause
        conditions.
        INPUT: tablename, where_clause(dictionary of key-Value
                pairs to be matched), key(default = AND) to be placed between
                where_clause items.

        Returns: None
        """
        key = ' ' + key + ' '
        if where_clause is not None:
            where = [k + ' = "' + v + '"'for k, v in where_clause.items()]
            where = key.join(where)
            query = 'DELETE FROM ' + tablename + ' WHERE ' + where
        else:
            query = 'DELETE FROM ' + tablename
        #print(query)
        curr = self.conn.cursor()
        curr.execute(query)
        self.conn.commit()

    def update_table(self, tablename, updates, where_clause=None, key='AND'):
        """
        This functions executes the update query to update items in a given
        table by matching the where clause conditions.
        INPUT: tablename, updates(dictionary of columns: value) to be made,
               where_clause(dictionary of key-Value pairs to be matched),
               key(default = AND) to be placed in between the where_clause
               items
        RETURNS: None
        """
        key = ' ' + key + ' '
        updates = [k + ' = "' + v + '"' for k, v in updates.items()]
        updates = ', '.join(updates)
        if where_clause is not None:
            where = [k + ' = "' + v + '"' for k, v in where_clause.items()]
            where = key.join(where)
            query = 'UPDATE ' + tablename + ' SET ' + updates + ' WHERE ' + where
        else:
            query = 'UPDATE ' + tablename + ' SET ' + updates
        curr = self.conn.cursor()
        curr.execute(query)
        self.conn.commit()
