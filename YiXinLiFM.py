#!/usr/bin/env python
# encoding: utf-8
"""
@author: yangwei.1024
@file: YiXinLiFM.py
@time: 2019-09-13 21:55
@desc: 下载心里FM音频文件
"""
import requests
import re
import os
import json
import urllib.request


# 获取音频Mp3信息
def getMp3Response(id):

    url = "http://fm.xinli001.com/broadcast"
    querystring = {"pk": id}
    headers = {
        'accept': "application/json, text/javascript, */*; q=0.01",
        'x-requested-with': "XMLHttpRequest",
        'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
        'cache-control': "no-cache",
        'postman-token': "3a95a7d6-5834-f6ae-5678-82b496bf9c71"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    print(response.text)
    try:
        res = json.loads(response.text)
    except:
        res = ''
    return res


# 判断是否是json
def isJson(myjson):
    try:
        res = json.loads(myjson)
    except ValueError:
        return False
    return res


# 非法字符替换为空格''
def validateTitle(title):
    rstr = r"[\/\\\:\*\?\"\<\>\|]"  # '/ \ : * ? " < > |'
    new_title = re.sub(rstr, " ", title)  # 替换为空格
    return new_title


def cbk(a,b,c):
    per = 100.0*a*b/c
    if per > 100:
        per = 100
    print('%.2f%%' % per)


# # 保存为MP3, 保存到特定文件夹下面：文件夹以专辑名字命名
def saveAudio(url, album, filename):
    filepath = os.getcwd()+'/mp3/'+album
    if os.path.exists(filepath):
        mp3 = os.path.join(filepath + '/', '' + filename + '.mp3')
        if url == '':
            print('the url is NUll, pass')
        else:
            urllib.request.urlretrieve(url, mp3, cbk)
            print(filename+'下载完毕')
    else:
        os.makedirs(filepath)
        mp3 = os.path.join(filepath + '/', '' + filename + '.mp3')
        if url == '':
            print('the url is NUll, pass')
        else:
            urllib.request.urlretrieve(url, mp3, cbk)
            print(filename+' 下载完毕')


if __name__ == '__main__':

    album = '壹心理'
    for id in range(38, 99395999):
        res = getMp3Response(id)
        if res:
            try:
                title = str(id) + '-' + res.get('data').get('title')
                url = res.get('data').get('url')
                saveAudio(url, album, title)
            except:
                print(str(res) + '为空')



