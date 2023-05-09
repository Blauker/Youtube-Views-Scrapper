#¯¯¯¯\____/¯¯¯¯\____/¯¯¯¯\____/¯¯¯¯\____/¯¯¯¯\____/¯¯¯¯\____/¯¯¯¯#
#                                                                #
#  This program will scrap all the views from youtube videos     #
#  (of a channel) which contains a specific keyword(s) on the    #
#  title.                                                        #
#    [ keywords.csv ]                                            #
#                                                                #
#  This programs works with a list of channel-ids                #
#    [ channel_ids.csv ]                                         #
#                                                                #
#  This program will generate 1 text file:                      #
#    [ Youtube-Views-Detailed_<date>.txt ]                       #
#                                                                #
#  @author: Blauker                                              #
#                                                                #
#____/¯¯¯¯\____/¯¯¯¯\____/¯¯¯¯\____/¯¯¯¯\____/¯¯¯¯\____/¯¯¯¯\____#

from bs4 import BeautifulSoup
import requests
import scrapetube
from datetime import datetime
import os

# CLEARING THE SCREEN BEFORE EXECUTING
os.system('cls')

# TIME.NOW (DD_MMM_YYYY)
dateTimeNow = datetime.now()
currentMonth = dateTimeNow.strftime("%d_%m_%Y")

# KEYWORDS THE VIDEO MUST HAVE
with open('Info/keywords.csv', 'r', encoding='utf-8') as f:
    content = f.read()
    keywords = content.split('\n')
    print(str(keywords))

# YOUTUBE CHANNEL IDs
with open('Info/channel_ids.csv', 'r', encoding='utf-8') as f:
    content = f.read()
    channel_ids = content.split('\n')
    channel_ids.pop(0)
    channel_ids.pop(0)

# CREATING NEW FILES TO WRITE
with open('Data/YouTube-Views-Detailed_' + str(currentMonth) + '.txt', 'w', encoding='utf-8') as fd:
    for id in channel_ids:
        id = id[:24]

        # LIST WITH ALL THE VIDEO URLS
        urls = scrapetube.get_channel(id)

        # SCRAPING YOUTUBE XML-VIDEO PAGE
        url = "https://www.youtube.com/feeds/videos.xml?channel_id=" + id
        html = requests.get(url)
        soup = BeautifulSoup(html.text, "lxml-xml")

        # INITIALIZE VARIABLES
        videos = []
        totalViews = 0
        totalVideos = 0
        maxVideosToSearch = 100  #Youtube video limit.

        # ALL YOUTUBE CHANNEL VIDEO LINKS
        for video in urls:
            link = "https://www.youtube.com/watch?v=" + video['videoId']
            videos.append(link)
        
        # YOUTUBE CHANNEL NAME
        channelName = soup.find("author").find("name").text.replace(" ", "")

        print   ("CHANNEL: " + channelName + " | KEYWORDS: " + str(keywords))
        fd.write("CHANNEL: " + channelName + " | KEYWORDS: " + str(keywords))

        for v, video in enumerate(videos):
            # GETTING THE VIDEO NAME
            soup = BeautifulSoup(requests.get(video).text, 'lxml')
            videoName = soup.select_one('meta[itemprop="name"][content]')['content']

            # IF THE YOUTUBE VIDEO NAME CONTAINS ANY KEYWORD...
            if ([keyword for keyword in keywords if(keyword.upper() in videoName.upper())]):
                # GETTING THE VIDEO VIEWS
                videoViews = soup.select_one('meta[itemprop="interactionCount"][content]')['content']
                totalViews += int(videoViews)
                totalVideos += 1
                
                print   (videoName + ": " + videoViews)
                fd.write(videoName + ": " + videoViews + "\n")
            
            if (v >= maxVideosToSearch):
                break
        if (totalVideos > 0):
            print   ("    Total views: " + str(totalViews) + "\n" + "    Total videos: " + str(totalVideos) + "\n\n")
            fd.write("    Total views: " + str(totalViews) + "\n" + "    Total videos: " + str(totalVideos) + "\n\n")
        else:
            print   ("    This channel dont have any video with that keyword" + "\n\n")
            fd.write("    This channel dont have any video with that keyword" + "\n\n")
        
fd.close() # CLOSING THE FILES
print ("Created -> " + 'Data/YouTube-Views-Detailed_' + str(currentMonth) + '.txt')