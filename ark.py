import urllib.request
import re
from bs4 import BeautifulSoup
import subprocess
from datetime import datetime
import time

FileName="C://20syl - Ongoing Thing feat Oddisee.mp3"
pattern="https://the2ndeuler.wordpress.com/..../../../cpp-tutorial/"

url=urllib.request.urlopen("https://the2ndeuler.wordpress.com/blog/")
urler=url.read()
url.close()
soup=BeautifulSoup((urler), "html.parser")
arkham=soup.find_all('a')
for link in arkham:
    lulz=str(link.get('href'))
    fox=re.findall(pattern,lulz)
    if fox:
        subprocess.call(["start",'VLC media player',FileName],shell = True)
    else:
      print("Not yet")

      

        
                            
        
        
