# -*- coding: utf-8 -*-
__author__ = 'red'
import sys
import  MySQLdb
reload(sys)
sys.setdefaultencoding('utf-8')

class esa_db:
    def __init__(self):
        self.db = MySQLdb.connect(host = "localhost",
                        port = 3306,
                        user = "root",
                        db = 'tema_diploma',
                        use_unicode = True,
                        charset='utf8')

        self.cursor = self.db.cursor()
        self.cursor.execute('SET NAMES utf8;')
        self.cursor.execute('SET CHARACTER SET utf8;')
        self.cursor.execute('SET character_set_connection=utf8;')
    def get_groups_list(self):
        return [u'ЭСА-07-1', u'ЭСА-07-2', u'ЭСА-07т', u'ЭСА-07-1з', u'ЭСА-07-1зт',
                u'ЭСА-08-1', u'ЭСА-08-2', u'ЭСА-08т', u'ЭСА-08-1з', u'ЭСА-08-1зт',
                u'ЭСА-09-1', u'ЭСА-09-2', u'ЭСА-09т', u'ЭСА-09-1з', u'ЭСА-09-1зт',
                u'ЭСА-10-1', u'ЭСА-10-2', u'ЭСА-10т', u'ЭСА-10-1з', u'ЭСА-10-1зт',
                u'ЭСА-11-1', u'ЭСА-11-2', u'ЭСА-11т', u'ЭСА-11-1з', u'ЭСА-11-1зт',
                u'ЭСА-12-1', u'ЭСА-12-2', u'ЭСА-12т', u'ЭСА-12-1з', u'ЭСА-12-1зт',
                u'ЭСА-13-1', u'ЭСА-13-2', u'ЭСА-13т', u'ЭСА-13-1з', u'ЭСА-13-1зт',
                u'ЭСА-14-1', u'ЭСА-14-2', u'ЭСА-14т', u'ЭСА-14-1з', u'ЭСА-14-1зт',
                u'ЭСА-15-1', u'ЭСА-15-2', u'ЭСА-15т', u'ЭСА-15-1з', u'ЭСА-15-1зт',
                u'ЭСА-16-1', u'ЭСА-16-2', u'ЭСА-16т', u'ЭСА-16-1з', u'ЭСА-16-1зт',
                u'ЭСА-17-1', u'ЭСА-17-2', u'ЭСА-17т', u'ЭСА-17-1з', u'ЭСА-17-1зт',
                u'ЭСА-18-1', u'ЭСА-18-2', u'ЭСА-18т', u'ЭСА-18-1з', u'ЭСА-18-1зт',
                u'ЭСА-19-1', u'ЭСА-19-2', u'ЭСА-19т', u'ЭСА-19-1з', u'ЭСА-19-1зт',
                u'ЭСА-20-1', u'ЭСА-20-2', u'ЭСА-20т', u'ЭСА-20-1з', u'ЭСА-20-1зт']


    def get_tech_objects_list(self):
        sql = '''
            select object_type from tema;
        '''
        data = self.cursor.execute(sql)
        rez = self.cursor.fetchall()

        data = []
        for i in rez:
            data.append(i[0])

        return data

    def generate_drive_type(self,object):
        list = []
        req = "SELECT DISTINCT drive_type FROM tema WHERE object_type = '{0}'; ".format(object)
        data = self.cursor.execute(req)
        rez = self.cursor.fetchall()


        for i in rez:
            list.append(u' '.join(i))

        #print list
        return list

    def generate_criterion(self, object):
        list = []
        req = "SELECT DISTINCT criterion FROM tema WHERE object_type = '{0}'; ".format(object)
        data = self.cursor.execute(req)
        rez = self.cursor.fetchall()

        for i in rez:
            list.append(u' '.join(i))

        #print list
        return list

    def generate_man_system(self):
        list = []
        req = "SELECT DISTINCT managment_system FROM tema;"
        data = self.cursor.execute(req)
        rez = self.cursor.fetchall()
        for i in rez:
            list.append(u' '.join(i))

        #print list
        return list

    def generate_reference(self, object):
        list = []
        req = "SELECT DISTINCT reference FROM tema WHERE object_type = '{0}';".format(object)
        data = self.cursor.execute(req)
        rez = self.cursor.fetchall()

        for i in rez:
            list.append(u' '.join(i))

        #print type(list)
        return list

    #Send data to table "rezults"
    def send_rezult(self,req):
        data = self.cursor.execute(req)
        self.db.commit()

        #print req

    #Checking for match FIO and groups
    def chek_for_match(self, fio, grupa):
        self.list = []
        req = "SELECT object_type FROM rezults WHERE FIO = '{0}' AND groups = '{1}';".format(fio, grupa)
        data = self.cursor.execute(req)
        rez = self.cursor.fetchall()

        for i in rez:
            self.list.append(i)

        #print  len(self.list)
        return len(self.list)

    #Checking for match content
    def chek_contect_for_match(self, drive_type, criterio, man_system, ref):
        self.list = []
        req = "SELECT * FROM rezults WHERE drive_type = '{0}' AND criterio = '{1}' AND managment_system = '{2}' AND reference = '{3}';".format(drive_type, criterio, man_system, ref)
        data = self.cursor.execute(req)
        rez = self.cursor.fetchall()

        for i in rez:
            self.list.append(i)

        print self.list
        print len(self.list)
        return len(self.list)


    #Return rezults after checking for match FIO
    def return_chek_for_match(self, fio):
        list = []
        req = "SELECT groups, drive_type, criterio, managment_system, reference  FROM rezults WHERE LOWER(FIO) = '{0}';".format(fio)
        data = self.cursor.execute(req)
        rez = self.cursor.fetchall()

        for i in rez:
            list.append(u', '.join(i))

        #print list, type(list)
        return list