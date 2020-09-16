from workbench import Workbench
from dotenv import load_dotenv
import os

load_dotenv()

myobject = Workbench('Sample',user = 'muleyashutosh', password =  os.getenv('mySQL_muleyashutosh_password'))

print('MYSQL VERSION: ', myobject.conn.get_server_info())

attributes = []
tablename = 'student'
myobject.create_table(tablename)
