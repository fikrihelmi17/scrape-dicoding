#! /usr/bin/env python3

# import the modules to support the scraping process
import json
from scrape import scraper

if __name__ == '__main__':
    # Define the URL
    url = 'https://www.dicoding.com/academies/list'

    data = scraper(url)

    # Save data to JSON file
    with open('dicoding_data.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)