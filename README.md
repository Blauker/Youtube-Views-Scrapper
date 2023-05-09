# Youtube-Views-Scrapper
Please note that YouTube Shorts videos will not be counted, and if a YouTube channel has many videos, the process may take some time.

## How to Add New Channels
If you want to add new channels to scrape, simply add the channel IDs to the [ids/channel_ids.csv](ids/channel_ids.csv) file. To check if the channel works correctly, run the [channel-id-test.py](channel-id-test.py) file.

## How to Get Channel IDs
To get the ID of a YouTube channel, simply visit any YouTube page. If the URL looks like this: `https://www.youtube.com/channel/UCiqmmeS3jg7BE-baFd92CAg`, the channel ID is `UCiqmmeS3jg7BE-baFd92CAg`. If the URL looks like this: `https://www.youtube.com/@SrTriline`, follow these steps:

1. Right-click on the page and select "View Page Source".
2. Press Ctrl+F to search for the string `?channel_id`.
3. You will see something like this: `videos.xml?channel_id=UCJxv80y78XTCUqfiplmDyRw`. The channel ID is `UCJxv80y78XTCUqfiplmDyRw`.

## How to Use the Scraper
To use the scraper, simply run the [count-views.py](count-views.py) file. The program will start scraping all the YouTube videos (with your custom keywords) from all the channel IDs listed in [ids/channel_ids.csv](ids/channel_ids.csv). After the process ends, a `.txt` file with the results will be generated. The results will be located in `YouTube-Views-Detailed.txt`.

## Limitations
Please note that abusing this tool may exceed the limits of the YouTube API. Use the tool with caution and respect the YouTube API usage policies.

And that's it! We hope this tutorial has been helpful for you. If you have any questions or suggestions, please don't hesitate to contact us. Enjoy the YouTube scraper!

