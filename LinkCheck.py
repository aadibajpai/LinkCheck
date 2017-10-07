import urllib.request
import re
from bs4 import BeautifulSoup
import subprocess
from datetime import datetime
import time
import sys
import vlc
import urllib.parse
import argparse
import glob
from urllib.error import URLError

def findLink(links):
    while True:
        for link in links:
            if re.search(pattern,str(link.get('href'))):
                return True
            
        else:
            print("Not yet")
            time.sleep(60)

parser = argparse.ArgumentParser()
parser.add_argument('-f',action='store',dest='filename',help='If specified, use the file instead of searching in current directory',default='none')
args = parser.parse_args();
FileName = ''
if args.filename == 'none':
    #No file specified, search directory
    print("Searching directory for music file.")
    files = glob.glob('./*.mp3')
    if len(files) == 0:
        print("No music file found, exiting")
        exit(1)
    FileName = files[0] #If more than one are found, take the first one
else:
    FileName = args.filename
print("Using "+FileName+" as music file")

raw_url = input("Input the URL where you want to find the link: ")
pattern = input("Input the pattern which you want to find: ")
parsed_url = urllib.parse.urlparse(raw_url)

url = raw_url if parsed_url.scheme else "http://"+raw_url

try:
    with urllib.request.urlopen(url) as cont:
        urler = cont.read()
except URLError:
    sys.exit("ERROR: Not a valid URL")
    
soup = BeautifulSoup(urler, "html.parser")
links = soup.find_all('a')

if findLink(links):
        p = vlc.MediaPlayer(FileName)
        p.play()
        print("--------------------------------- \n Input q to stop the music. \n---------------------------------")
        while True:
            key = sys.stdin.read(1)
            if key == 'q': 
                p.stop()
                break
      

      

        
                            
        
        
