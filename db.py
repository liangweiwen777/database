#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#Discription:
#====#====#====#====
import pymysql
#链接数据库
def con_db(hostname='qzx',username='root',password='123456',databse='atm'):
    db = pymysql.connect(hostname,username,password,databse)
    return db
#查询
def search(sql):
    db = con_db()
    cu = db.cursor()
    cu.execute(sql)
    datas = cu.fetchall()
    db.commit()
    db.close()
    return datas
#增删改
def fix(sql):
    db = con_db()
    cu = db.cursor()
    cu.execute(sql)
    db.commit()
    db.close()

if __name__ == '__main__':
    fix("update userinfo set password = '654321' where id=1")
    sql = 'select * from userinfo where id=1'
    result = search(sql)
    print(result)