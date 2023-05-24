import numpy as np
import pandas as pd
import tensorflow as tf
from bs4 import BeautifulSoup
import requests

# Function to scrape clothing item details from a website
def scrape_clothing_details(url, class_name):
    response = requests.get(url)
    html_content = response.content
    soup = BeautifulSoup(html_content, "html.parser")
    items = soup.find_all("div", class_=class_name)
    
    clothing_details = []
    for item in items:
        link = item.find("a")["href"] if item.find("a") else ""
        image = item.find("img")
        image_url = image["src"] if image else ""
        image_title = image["title"] if image and "title" in image.attrs else ""
        text = item.find("p").get_text(strip=True) if item.find("p") else ""
        text_with_title = f"{image_title} {text}"
        clothing_details.append({"link": link, "image_url": image_url, "text": text_with_title})
    
    return clothing_details


url = "https://www.bewakoof.com/men-clothing"

item_desc = scrape_clothing_details(url, "plp-product-card")
print(len(item_desc))

# Specify the base URL of the website to scrape (men)
base_url_m = "https://www.bewakoof.com/men-clothing"

# (women)
base_url_w = "https://www.bewakoof.com/women-clothing" 

# Specify the class name of the elements containing clothing details
class_name = "plp-product-card"

# Scrape clothing details from multiple pages
all_details_men = []
all_details_women = []

for page_num in range(1, 5):  # Scraping 5 pages
    # men
    url_men = f"{base_url_m}?page={page_num}"
    page_details = scrape_clothing_details(url_men, class_name)
    all_details_men.extend(page_details)

    # women
    url_women = f"{base_url_w}?page={page_num}"
    page_details = scrape_clothing_details(url_women, class_name)
    all_details_women.extend(page_details)

final_df = all_details_men + all_details_women
for map in final_df:
    map["link"] = "https://www.bewakoof.com" + map["link"]

final_df = pd.DataFrame(final_df)
final_df.to_csv("fashion_data_test.csv", index=None)