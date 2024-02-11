#! /usr/bin/env python3

# import the modules to support the scraping process
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup

# Function to scrape data from Tokopedia
def scrape_tokopedia(search_query):
    # Define the URL based on search query
    url = f"https://www.tokopedia.com/search?st=&q={search_query}"

    # Configure WebDriver to use Firefox
    driver = webdriver.Firefox()

    # Open the URL
    try:
        driver.get(url)
    except:
        print("Can't access the URL")

    # Wait for the page to load the website
    driver.implicitly_wait(10)

    # Prepare the variable for JSON data
    products = []

    # Selenium will wait for a maximum of 3 seconds for an element matching the given criteria to be found. 
    # If no element is found in that time, Selenium will print to the console.
    try: 
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'zeus-root')))
    except:
        print("There is no element specified")

    # BeautifulSoup will parse the URL
    content = driver.page_source
    soup = BeautifulSoup(content, 'html.parser')

    # BeautifulSoup will find the CSS class that contain product container
    for product in soup.find_all('div', class_='css-uwyh54'):

        # First, let's find the CSS class for product name and get the text
        product_name = product.find('div', class_='prd_link-product-name css-3um8ox').text
        
        # Not all product has rating, so we should manage it. 
        # If it has rating, get the text. If none, set it to empty string.
        try:
            product_rating = product.find('span', class_='prd_rating-average-text css-t70v7i').text
        except:
            product_rating = ''

        # Not all product in the list has store name, so we should manage it. 
        # If it has store name, get the text. If none, set it to empty string.
        try:
            store_name = product.find('span', class_='prd_link-shop-name css-1kdc32b flip').text
        except:
            store_name = ''

        # Not all product in the list has store location, so we should manage it. 
        # If it has store location, get the text. If none, set it to empty string.
        try:
            store_location = product.find('span', class_='prd_link-shop-loc css-1kdc32b flip').text
        except:
            store_location = ''
        
        # Not all product in the list has product sold, so we should manage it. 
        # If it has product sold, get the text. If none, set it to empty string.
        try:
            product_sold = product.find('span', class_='prd_label-integrity css-1sgek4h').text
        except:
            product_sold = ''

        # Not all product in the list has product discount, so we should manage it. 
        # If it has product discount, get the text. If none, set it to empty string.
        try:
            product_discount = product.find('div', class_='prd_badge-product-discount css-1xelcdh').text
        except:
            product_discount = ''

        # Retrieve the src attribute in the img tag
        product_image = product.find('img', class_='css-1q90pod').get('src')

        products.append(
            {
                'Product Name': product_name,
                'Rating': product_rating,
                'Store Name': store_name,
                'Store Location': store_location,
                'Sold': product_sold,
                'Discount': product_discount,
                'Image': product_image
            }
        )

    # Close the WebDriver
    driver.quit()

    return products
