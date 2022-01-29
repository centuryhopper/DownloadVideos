#!/usr/bin/env python
# coding: utf-8

# # Downloading videos using request and Bs4


import requests
from bs4 import BeautifulSoup
from secrets import Secrets

'''
URL of the archive web-page which provides link to
all video lectures. It would have been tiring to
download each video manually.
In this example, we first crawl the webpage to extract
all the links and then download videos.
'''

# specify the URL of the archive here
archive_url = Secrets.URL
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36", 'Accept-Language': 'en-US, en;q=0.5'}

def get_video_links():
    #create response object
    r = requests.get(archive_url, headers=HEADERS)
    #create beautiful-soup object
    soup = BeautifulSoup(r.content,'html5lib')
    #find all links on web-page
    links = soup.findAll('a')
    #filter the link ending with .mp4
    video_links = [archive_url + link['href'] for link in links if link['href'].endswith('mp4')]

    return video_links

# get_video_links()


def download_video_series(video_links):
    for link in video_links:
        '''
        iterate through all links in video_links
        and download them one by one
        '''

        #obtain filename by splitting url and getting last string
        file_name = link.split('/')[-1]

        print ("Downloading file:%s"%file_name)

        #create response object
        r = requests.get(link, stream = True)

        #download started
        with open(file_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size = 1024*1024):
                if chunk:
                    f.write(chunk)

        print ("%s downloaded!\n"%file_name)

    print ("All videos downloaded!")
    return

if __name__ == "__main__":
    #getting all video links
    video_links = get_video_links()
    print(video_links)

    #download all videos
    # download_video_series(video_links)

