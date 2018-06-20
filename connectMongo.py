# -*- coding: utf-8 -*-
# @Time    : 2018/6/9 20:42
# @Author  : Torre
# @Email   : klyweiwei@163.com
import pymongo
from pymongo import MongoClient
import json
import os
def connectMongoDB():
    client = pymongo.MongoClient(host='localhost', port=27017)
    # client = MongoClient()
    return client

# client = connectMongoDB()
# print(client)
# db = client.mydb
# print(db)
# collection = db("students")

# student = {
#     'id': '20170101',
#     'name': 'Jordan',
#     'age': 20,
#     'gender': 'male'
# }
# result = collection.insert(student)

my_file = os.getcwd()
print(my_file+'\\')
if os.path.exists(my_file+'\\'):
    os.remove(my_file+'\\')
    #删除文件，可使用以下两种方法。
    os.remove(my_file)
    file = open('newjson.json', 'w', encoding='utf-8')
    data = {
        'no': 1,
        'name': 'Runoob财年哦',
        'url': 'http://www.runoob.com'
    }

    jsonp = json.dumps(data).decode('utf-8')
    j2o = json.loads(jsonp)
    file.write(jsonp)
    print(j2o)
else:
    print('no such file:%s' %my_file)

