#! /usr/bin/env python3

# import the modules to support the scraping process
import json
from scrape import scrape_tokopedia

if __name__ == "__main__":
    search_query = "iphone"
    data = scrape_tokopedia(search_query)
    
    # Save data to JSON file
    with open('tokopedia_data.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)