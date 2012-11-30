# -*- coding: utf-8 -*-
__author__ = 'red'
import sys
import  MySQLdb
reload(sys)
sys.setdefaultencoding('utf-8')


db = MySQLdb.connect(host = "localhost",
            port = 3306,
            user = "root",
            db = 'tema_diploma',
            use_unicode = True)

db.set_character_set('utf8')
cursor = db.cursor()
cursor.execute('SET NAMES utf8;')
cursor.execute('SET CHARACTER SET utf8;')
cursor.execute('SET character_set_connection=utf8;')


cursor.execute('SET NAMES utf8;')
cursor.execute('SET CHARACTER SET utf8;')
cursor.execute('SET character_set_connection=utf8;')
req = "SELECT * FROM tema;"
command = cursor.execute(req)
rezult = cursor.fetchall()

for i in rezult:
    print str(i[1]+' '+i[2]+' '+i[3]+' '+i[4])

cursor.close()
db.close()