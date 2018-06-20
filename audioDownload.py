# -*- coding: utf-8 -*-
# @Time    : 2018/6/8 0:25
# @Author  : Torre
# @Email   : klyweiwei@163.com
# 此程序可以获取xmly音频文件，尝试破解付费内容： 获取类别 》 albumId 》 mp3,可以尝试保存到数据库
# 可以大概分为三部分：获取音频类目, 爬取某一类目下的albumId,再爬取某一albumId下的MP3,保存文件，存到数据库MongoDB
import requests
import os
from bs4 import BeautifulSoup
import re
import getSoup

# 获取歌单的playlistId
def getplaylistids(url):
    url = url
    soup = getSoup.getSoup(url)
    # print(soup)
    playlistids = []
    playlists = soup.select('a')
    print(playlists)
    for playlist in playlists:
        playlist = playlist.get('href')
        playlistids.append(playlist)
    return playlistids

# Testing case

url = 'https://music.163.com/discover/playlist'
for play in getplaylistids(url):
    print(play)

# 获取歌单的 所有songId

# def getAudioUrl():