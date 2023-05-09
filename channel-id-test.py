from bs4 import BeautifulSoup
import requests
import os

# CLEARING THE SCREEN BEFORE EXECUTING
os.system('cls')

channel_ids = []

# YOUTUBE CHANNEL IDs
with open('Info/channel_ids.csv', 'r', encoding='utf-8') as f:
    content = f.read()
    channel_ids = content.split('\n')
    channel_ids.pop(0)
    channel_ids.pop(0)

print("Loading channel names...\n")

for i, id in enumerate(channel_ids):
    id = id[:24]

    # SCRAPING YOUTUBE XML-VIDEO PAGE
    url = "https://www.youtube.com/feeds/videos.xml?channel_id=" + id
    html = requests.get(url)
    soup = BeautifulSoup(html.text, "lxml-xml")

    # YOUTUBE CHANNEL NAME
    channelName = soup.find("author").find("name").text.replace(" ", "")

    print("Channel " + str(i) + ": " + channelName)
    
print("\n")
