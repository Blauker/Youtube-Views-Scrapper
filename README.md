# Youtube-Views-Scrapper
FIRST OF ALL:
    You need python 3 installed on your computer.
    To install all depencencies and libraries execute --> pip install -r requirements.txt
    Youtube shorts wont be counted
    If a youtube channel have a lot of videos, it will take a while
    The abuse of this app will exceed the request youtube API limit

HOW TO ADD NEW CHANNELS:
    Write channel_ids on [ ids/channel_ids.csv ] file
    To test if the channel works execute [ channel-id-test.py ]

HOW TO GET CHANNEL IDS:
    Go you any Youtube page
    If the list is like this: https://www.youtube.com/channel/UCiqmmeS3jg7BE-baFd92CAg, channel id = UCiqmmeS3jg7BE-baFd92CAg
    If the channel is like this: https://www.youtube.com/@SrTriline
        · Right click -> View page source
        · Ctrl+F to search -> [ ?channel_id ]
        · You will see something like this: videos.xml?channel_id=UCJxv80y78XTCUqfiplmDyRw, channel id = UCJxv80y78XTCUqfiplmDyRw

HOW TO USE THE SCRAPPER:
    execute [ count-views.py ]
    · The program will start scraping all the youtube videos (with your custom keywords) from all the channel_ids listed.
    · After the process end, will generate .txt file with the results.

RESULTS:
    Will generate YouTube-Views-Detailed.txt
