#coding=utf-8

import hashlib
import sys
import os

import pymysql

def get_file_md5(f):
    return hashlib.md5(open(f,'rb').read()).hexdigest()
#
# create database filetools;
# create table files(id int not null auto_increment,file_name varchar(255) not null,fullpath varchar(512) not null,fileMD5 varchar(32)
#



if __name__ == '__main__':

    rootdir="/root"
    conn=pymysql.Connect(host='localhost',port=3306,user='python',passwd='python',db='filetools',charset='utf8')
    conn.autocommit(False)
    cursor=conn.cursor()
    try:
        for parent,dirnames,filenames in os.walk(rootdir):
            # for dirname in dirnames:
            #     print("parent folder is :"+parent)
            #     print("dirname is :"+dirname)


            for filename in filenames:
                fullpath=os.path.join(parent,filename)
                fileMD5=get_file_md5(fullpath)
                # print("parent folder is :"+parent)
                # print("filename with full path:{0} md5 is {1}".format(fullpath,fileMD5))
                sql='insert into files(file_name,fullpath,fileMD5) values("{0}","{1}","{2}")'.format(filename,fullpath,fileMD5)
                print(sql)
                cursor.execute(sql)
                print(cursor.rowcount)
        conn.commit()
    except Exception as e:
        print("Reason:",e)
        conn.rollback()

    cursor.close()
    conn.close()




