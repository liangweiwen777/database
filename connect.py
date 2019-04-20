#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:liangweiwen
#CreatDate:
#Version: 
#Discription:
#====#====#====#====
import sqlite3,os
class Connect:
    #连接数据
    def con(self):
        # db = sqlite3.connect('dcb.db')
        db = sqlite3.connect('./db/dcb.db')#跨文件调用
        # current_path = os.path.dirname(__file__)
        # db = sqlite3.connect(current_path + '/dcb.db')#建议使用相对路径,通用
        return db
    #查询数据库
    def search(self,sql):
        db = self.con()
        cu = db.cursor()
        cu.execute(sql)
        datas = cu.fetchall()
        db.commit()
        db.close()
        return datas
    #数据库：增、删、改
    def fix(self,sql):
        db = self.con()
        cu = db.cursor()
        cu.execute(sql)
        db.commit()
        db.close()
if __name__ == '__main__':
    c = Connect()
    # sql = 'select * from results'
    sql = 'select red_number,blue_number from numbers'
    datas = c.search(sql)
    print(datas)
    # for i in datas:
    #     print(i)
    # sql = "insert into numbers(red_number,blue_number) values('01,02,03,04,05,06','16')"
    # c.fix(sql)
