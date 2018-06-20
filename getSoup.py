#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : Torre
# @Email  : klyweiwei@163.com
# @Time   : 2018/6/5
import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import time

def getSoup(url):
    # proxies = {'http': '121.193.143.249:80'}
    # requests.get('http://httpbin.org/ip', ).json()
    response = requests.get(url)
    response.raise_for_status()
    res = response.content
    soup = bs(res, 'html.parser')
    return soup


# # 下面函数不成功
# def getSoupBySe(url):
#     web = webdriver.Chrome()
#     web.get(url)
#     time.sleep(3)
#     dec = web.find_element_by_class_name("m-pl-container")
#     InnerElement = dec.get_attribute('innerHTML')
#     soup = bs(InnerElement, 'html.parser')
#     playlists = soup.find_all('a')
#     for playlist in playlists:
#         print(playlist.get('href'))






