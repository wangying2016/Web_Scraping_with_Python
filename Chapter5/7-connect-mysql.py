# Use PyMySQL
# import pymysql
#
# conn = pymysql.connect(host='127.0.0.1',
#                        user='root',
#                        passwd='123456',
#                        db='mysql')
# cur = conn.cursor()
# cur.execute('USE scraping')
# cur.execute('SELECT * FROM pages')
# print(cur.fetchone())
# cur.close()
# conn.close()

# Use mysql.connector
import mysql.connector

conn = mysql.connector.connect(host='127.0.0.1',
                               user='root',
                               passwd='123456',
                               db='mysql')
cur = conn.cursor()
cur.execute('USE scraping')
cur.execute('SELECT * FROM pages')
print(cur.fetchone())
cur.close()
conn.close()
