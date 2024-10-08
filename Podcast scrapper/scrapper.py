'''
This script scrapes ONE podcast page for the RSS feed URL and downloads all mp3 files from the feed.
'''

import requests
import os
import re
from bs4 import BeautifulSoup

def scrape_podcast(podcast_url):
    # Directory to save the downloaded mp3 files
    download_dir = "./podcast_episodes"
    os.makedirs(download_dir, exist_ok=True)

    # Scrape the podcast page for the RSS feed URL
    response = requests.get(podcast_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    rss_link = soup.find_all('a', href=re.compile("https://api.sr.se/api/rss/pod/itunes"))

    if rss_link:
        rss_feed_url = rss_link[0].get('href')
    else:
        raise ValueError("RSS feed URL not found")

    # Fetch the RSS feed
    response = requests.get(rss_feed_url)
    rss_feed_content = response.content

    # Parse the RSS feed
    soup = BeautifulSoup(rss_feed_content, 'xml')
    items = soup.find_all('item')

    # Download each mp3 file from the RSS feed
    for item in items:
        # Your code to download mp3 files goes here
        pass

if __name__ == "__main__":
    podcast_url = "https://poddtoppen.se/podcast/1680705190/i-hjarnan-pa-louise-epstein"
    scrape_podcast(podcast_url)