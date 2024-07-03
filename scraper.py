import requests
from bs4 import BeautifulSoup

def scrape_website(url):

    """Scrapes a website and downloads dictionaries of data
    
    Args will be as follows:
    url: The URL of the website to scrape
    
    A list of dictionaries, where each dictionary represent an RnB vinyl record with details
    like title, artist, price, and condition (if available)"""

    # Download for webpage content, both grouped and individual
    response = requests.get(url)
    response.raise_for_status() # Raises an exception for requests that are not successful

    # Bringing in the BeautifulSoup library to parse HTML content 
    soup = BeautifulSoup(response.content, 'html.parser')

    # Finding all product listings, especially for 90s RnB
    listings = soup.find_all('div', class_='link_1ctor')

    #Initialize an empty list to store product data
    records = []

    for listing in listings:
        # data extraction from each listing
        title_element = listing.find()
