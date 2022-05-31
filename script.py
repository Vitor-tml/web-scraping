from urllib.request import urlopen, urlretrieve, Request
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup
import pandas as pd
import urllib.parse
 
 
#Obtendo o HTML
name = "GLP Capivara#CWB"
url = "https://tracker.gg/valorant/profile/riot/" + urllib.parse.quote(name) + "/overview"
headers ={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"}
 
req = Request(url,headers=headers)
response = urlopen(req)
html = response.read()
soup = BeautifulSoup(html,'html.parser')

rank = soup.find("div", attrs={"class": "valorant-rank-bg"})
print("O rank de " + name +  " é " + rank.text.replace("\n","").replace(" ", ""))