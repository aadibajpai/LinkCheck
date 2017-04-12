import urllib.request
import re
from bs4 import BeautifulSoup
import subprocess
from datetime import datetime
import time
import sys
import vlc


def findLink(links):
    while True:
        for link in links:
            if re.search(pattern,str(link.get('href'))):
                return True
            
        else:
            print("Not yet")
            time.sleep(60)
        
FileName = sys.argv[1]
url = input("Input the URL where you want to find the link: ")
pattern = input("Input the pattern which you want to find: ")


with urllib.request.urlopen(url) as cont:
    urler = cont.read()

soup = BeautifulSoup(urler, "html.parser")
links = soup.find_all('a')

if findLink(links):
        p = vlc.MediaPlayer(FileName)
        p.play()
        while True:
            key = sys.stdin.read(1)
            if key == 'q': 
                p.stop()
                break
      

      

        
                            
        
        
