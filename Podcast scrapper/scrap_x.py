'''
This script scrapes multiple webpages by calling scrapper.py
'''

from scrapper import scrape_podcast

# List of podcast URLs
podcast_urls = [
    "https://poddtoppen.se/podcast/1680705190/i-hjarnan-pa-louise-epstein",
    "https://poddtoppen.se/podcast/1436136212/dumma-manniskor",
    "https://poddtoppen.se/podcast/1497443372/det-morka-psyket",
    "https://poddtoppen.se/podcast/1500788973/fasciaguiden",
    "https://poddtoppen.se/podcast/1373262000/barnpsykologerna",
    "https://poddtoppen.se/podcast/1053691380/psykiatrikerna",
    "https://poddtoppen.se/podcast/1592497926/psykologisk-forskning",
    "https://poddtoppen.se/podcast/1125776471/psykologipodden",
    "https://poddtoppen.se/podcast/1263660795/lakarna-podcast",
    "https://poddtoppen.se/podcast/1031843296/hjarnpodden-kristina-bahr",
    # "https://podtail.se/podcast/psykopatpodden-del-1/",
    # "https://modernpsykologi.se/podd/"
]

# Call the scrape_podcast function for each URL
for url in podcast_urls:
    try:
        scrape_podcast(url)
    except ValueError as e:
        print(f"Error scraping {url}: {e}")




        