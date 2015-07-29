# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 12:40:36 2015

"""
"""
import requests
import datetime
from bs4 import BeautifulSoup
import certifi

url = 'https://www.rakuten-sec.co.jp/web/market/ranking/value.html?ind=1&market=0&information=0'


response = requests.get(url, verify = False)
soup = response.text.encode('shift-jis')    # a `bytes` object
#text = data.decode('shift-jis') # a `str`; this step can't be used if data is binary
#text = text[13:] #第13個是位

print (soup)
"""

import urllib.request
import re

url = 'https://www.rakuten-sec.co.jp/web/market/ranking/value.html'

req = urllib.request.Request(url)
resp = urllib.request.urlopen(req)
respData = resp.read()
respData = respData.decode('utf-8')

print (respData)
