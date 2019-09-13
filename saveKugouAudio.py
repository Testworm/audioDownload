# -*- coding: utf-8 -*-
# @Time    : 2018/6/8
# @Author  : Torre
# @Email   : klyweiwei@163.com
# 音乐下载V1.1

import os
import urllib.request
import requests
import re
import json
import getSoup

headers = {
    'origin': "http://www.kugou.com",
    'x-devtools-emulate-network-conditions-client-id': "97C9BAA42BE5A8449EC4283F764B4D9E",
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36",
    'content-type': "application/x-www-form-urlencoded",
    'accept': "*/*",
    'referer': "http://www.kugou.com/singer/3520.html",
    'accept-encoding': "gzip, deflate",
    'accept-language': "zh-CN,zh;q=0.9",
    'cookie': "kg_mid=88665d81b7959ab3787c4976831a30f9; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1528705681; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1528707581",
    'cache-control': "no-cache",
    'postman-token': "c717ef07-2b91-06f1-1d22-abcb47b0bce2"
}

# 获取album信息
def getAlbumid(singerID):
    # 获取歌单albumid
    url = "http://www.kugou.com/yy/"
    querystring = {"r": "singer/album", "sid": singerID}
    # headers = {
    #     'origin': "http://www.kugou.com",
    #     'x-devtools-emulate-network-conditions-client-id': "97C9BAA42BE5A8449EC4283F764B4D9E",
    #     'user-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36",
    #     'content-type': "application/x-www-form-urlencoded",
    #     'accept': "*/*",
    #     'referer': "http://www.kugou.com/singer/3520.html",
    #     'accept-encoding': "gzip, deflate",
    #     'accept-language': "zh-CN,zh;q=0.9",
    #     'cookie': "kg_mid=88665d81b7959ab3787c4976831a30f9; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1528705681; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1528707581",
    #     'cache-control': "no-cache",
    #     'postman-token': "c717ef07-2b91-06f1-1d22-abcb47b0bce2"
    # }
    response = requests.request("POST", url, headers=headers, params=querystring)
    res = response.text
    # print(type(res))
    jsonRes = json.loads(res)
    loadAlbumids = []  # 保存albumids到list
    loadAlbumname = []
    albumids = jsonRes['data']

    for albumid in albumids:
        albumid = albumid['albumid']
        # print(albumid)
        loadAlbumids.append(albumid)
        # print(albumid)

    for albumname in albumids:
        albumname = albumname['albumname']
        loadAlbumname.append(albumname)
        # print(albumname)
    return loadAlbumname, loadAlbumids

# getAlbumid(2303)

def getMp3Info(albumid):
    url = 'http://www.kugou.com/yy/album/single/'+str(albumid)+'.html'
    soup = getSoup.getSoup(url)
    hashs = soup.select('.songList a')
    loadMp3Hash = []
    for hashss in hashs:
        hash = hashss.get('data')
        # 通过spilt('|')分割字符串,获取hash
        mp3Hash = hash.split('|')[0]
        # print(hash.split('|')[0])
        # hash = hash.spilt('|')
        loadMp3Hash.append(mp3Hash)
        # print(mp3Hash)
    return loadMp3Hash

# mp3 = getMp3Info(1645030)
# for i in range(len(mp3)):
#     print(mp3[i])

# 获取歌曲的PlayerUrl
def getPlayUrl(hash, albumId):
    url = "http://www.kugou.com/yy/index.php"
    querystring = {"r": "play/getdata", "hash": hash, "album_id": albumId}
    response = requests.request("GET", url, headers=headers, params=querystring)
    response.raise_for_status()
    res = response.text
    # print(type(res))
    jsonRes = json.loads(res)
    playUrl = jsonRes['data']

    audioName = playUrl['audio_name']
    playUrl = playUrl['play_url']
    music = (audioName, playUrl)
    # print('-'.join(music))
    return audioName, playUrl

# @test
# mp3 = getMp3Info(1645030)
# for i in range(len(mp3)):
#     print(mp3[i])
#     getPlayUrl(mp3[i], '1645030')


# 非法字符替换为空格''
def validateTitle(title):
    rstr = r"[\/\\\:\*\?\"\<\>\|]"  # '/ \ : * ? " < > |'
    new_title = re.sub(rstr, " ", title)  # 替换为空格
    return new_title


def cbk(a,b,c):
    per=100.0*a*b/c
    if per>100:
        per=100
    print('%.2f%%' % per)


# # 保存为MP3, 保存到特定文件夹下面：文件夹以专辑名字命名
def saveAudio(url, album, filename):
    # filepath = os.getcwd()+'\\mp3\\'+album
    filepath = os.getcwd()+'/mp3/'+album
    if os.path.exists(filepath):
        # os.removedirs(filepath)
        # mp3 = os.path.join(filepath + '\\', '' + filename + '.mp3')
        mp3 = os.path.join(filepath + '/', '' + filename + '.mp3')
        if url == '':
            print('the url is NUll, pass')
        else:
            urllib.request.urlretrieve(url, mp3, cbk)
            print(filename+'下载完毕')
    else:
        os.makedirs(filepath)
        # mp3 = os.path.join(filepath + '\\', '' + filename + '.mp3')
        mp3 = os.path.join(filepath + '/', '' + filename + '.mp3')
        if url == '':
            print('the url is NUll, pass')
        else:
            urllib.request.urlretrieve(url, mp3, cbk)
            print(filename+'下载完毕')


# 正则表达式提取器，提起歌曲名字和歌曲连接
# 运行主程序, 只需要填入 歌手ID即可(http://www.kugou.com/yy/html/singer.html,
# 点击任一歌手即可获得其ID), 可以自动下载其所有专辑 : 比如3043 代表 许巍; 61874代表Sophia zelmani 34450


# test
def mp3Creator(singerId):
    albumname, albumids = getAlbumid(singerId)
    # length = len(albumids)
    # print(albumids)
    for i in range(len(albumids)):
        hashs = getMp3Info(albumids[i])
        for ii in range(len(hashs)):
            audioName, playUrl = getPlayUrl(hashs[ii], albumids[i])
            saveAudio(playUrl, validateTitle(albumname[i]), validateTitle(audioName))


# mp3Creator(34450)


if __name__ == '__main__':
    mp3 = 'http://tyst.migu.cn/public/product5th/product28/2019/02/15/2015%E5%B9%B411%E6%9C%8826%E6%97%A514%E7%82%B943%E5%88%86%E7%B4%A7%E6%80%A5%E5%86%85%E5%AE%B9%E5%87%86%E5%85%A5%E5%8C%97%E4%BA%AC%E5%B0%91%E5%9F%8E2%E9%A6%96/%E6%A0%87%E6%B8%85%E9%AB%98%E6%B8%85/MP3_128_16_Stero/63681000367.mp3'
    saveAudio(mp3, '爬虫下载', '音乐2')

