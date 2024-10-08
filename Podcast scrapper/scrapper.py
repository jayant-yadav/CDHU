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
    mp3_count = 0

    # Download each mp3 file from the RSS feed
    for item in items:
        enclosure = item.find('enclosure')
        if enclosure and enclosure.get('type') == 'audio/mpeg':
            mp3_count += 1
            mp3_url = enclosure.get('url')
            mp3_filename = os.path.join(download_dir, os.path.basename(mp3_url))

            # Download the mp3 file
            with requests.get(mp3_url, stream=True) as r:
                r.raise_for_status()
                with open(mp3_filename, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=8192):  # 8192 bytes = 8 KB
                        f.write(chunk)
            print(f"Downloaded {mp3_count}: {mp3_filename}")

if __name__ == "__main__":
    podcast_url = "https://poddtoppen.se/podcast/1680705190/i-hjarnan-pa-louise-epstein"
    scrape_podcast(podcast_url)