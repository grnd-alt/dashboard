from bs4 import BeautifulSoup
from urllib.request import urlopen
import datetime
def get_next_hours():

    url = "https://www.wetter.de/deutschland/wetter-leipzig-18232916.html"
    content = urlopen(url).read()
    #print(content)
    soup = BeautifulSoup(content,features = "html.parser")

    time = int(str(datetime.datetime.now().time())[:2])
    arounds = []
    for i in range(time,time+3):
        arounds.append(str(soup.find("div",{"data-id":str(i)}).get_text())[-3:]+";"+str(soup.find("div",{"data-id":str(i)}).find("img").get("title")))
    return arounds
def get_max_min_temp():
    url = "https://www.wetter.de/deutschland/wetter-leipzig-18232916.html"
    content = urlopen(url).read()
    # print(content)
    soup = BeautifulSoup(content, features="html.parser")
    max = soup.find("div", {"class": "weather-daybox__minMax__max"}).get_text()
    min = soup.find("div", {"class": "weather-daybox__minMax__min"}).get_text()
    return max,min
print(get_next_hours())