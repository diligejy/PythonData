import sqlite3
import datetime

now = datetime.datetime.now()
print("now : ", now)

nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
print("nowDatetime : ", nowDatetime)

print('sqlite3.version : ', sqlite3.version)
print('sqlite3.sqlite_version : ', sqlite3.sqlite_version)

conn = sqlite3.connect('C:/Users/sjy04/OneDrive/바탕 화면/cosmetheus/database.db', isolation_level=None)

c = conn.cursor()
print('Cursor Type:', type(c))

