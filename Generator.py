# -*- coding: utf-8 -*-
__author__ = 'Red_Labs'

import sys
from PyQt4 import QtGui, QtCore
from esa_database import esa_db
from random import choice

reload(sys)
sys.setdefaultencoding('utf-8')

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Generator:
    def __init__(self):
        self.db = esa_db()

    def gen(self,fio, grupa, object):
        self.dr_type = self.db.generate_drive_type(object)
        self.dr_type_choice = choice(self.dr_type)

        self.cr = self.db.generate_criterion(object)
        self.cr_choice = choice(self.cr)

        self.man_system = self.db.generate_man_system()
        self.man_system_choice = choice(self.man_system)

        self.ref = self.db.generate_reference(object)
        self.ref_choice = choice(self.ref)


        #print dr_type_choice
        #print dr_type_choice, cr_choice, man_system_choice, ref_choice

        #Request for INSERT to table "rezults"
        req = "INSERT INTO rezults (FIO, groups, object_type, drive_type, criterio, managment_system, reference) " \
              "VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}');".format(fio, grupa, object, self.dr_type_choice,
                self.cr_choice, self.man_system_choice, self.ref_choice)

        self.send = self.db.send_rezult(req)

        #Text for output
        self.show_req = ' Ф.И.О.:   {0} \n гр. {1} \n\n Тема дипломного проекта: \n {2} \n\n Спецчасть: \n {3} \n {4} \n ' \
                        '{5} \n\n Ссылки: \n {6}'.format(fio, grupa, object, self.dr_type_choice, self.cr_choice,
                        self.man_system_choice, self.ref_choice)


        print ('|------------------------------|')
        print type(self.show_req), self.show_req

        return self.show_req



    def checking(self, fio, grupa, object):
        self.ch = self.db.chek_for_match(fio, grupa)


        if self.ch == 0:
            self.rez = self.gen(fio, grupa, object)
            self.ch_cont = self.db.chek_contect_for_match(self.dr_type_choice, self.cr_choice, self.man_system_choice, self.ref_choice)
            if self.ch_cont != 0:
                self.rez = self.gen(fio, grupa, object)
        else:
            self.rt = self.db.return_chek_for_match(fio)
            rt_choice = choice(self.rt)
            print ('|------------------------------|')
            print self.rt, type(self.rt)
            print rt_choice[0:8], type(rt_choice)

            #Text for output
            self.show_rt = '                                             ВНИМАНИЕ!!!' \
                           '\n\n ЗАДАНИЕ НА ДИПЛОМИРОВАНИЕ СТУДЕНТУ гр. {1} \n{0} УЖЕ БЫЛО ВЫДАНО!!!\n\nТема ' \
                           'дипломного проекта: \n {2}\n\nСпецчасть: \n{3}'.format(fio, rt_choice[0:8], object, rt_choice[9:])

            self.rez = self.show_rt

        return  self.rez



