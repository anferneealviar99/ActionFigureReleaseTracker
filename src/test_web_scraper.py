import requests
from bs4 import BeautifulSoup as bs
import json
import os 


# Collection Page URL

URL = "https://www.greenrockcomics.shop/collections/dc-multiverse"
HEADERS = {"User-Agent": "Mozilla/5.0"}

DATA_FILE = "../json/greenrock_dc_multiverse.json"

def fetch_figures():
    """Scrape Green Rock Comics' DC Multiverse Collection Page"""
    
    response = requests.get(URL, headers=HEADERS)
    soup = bs(response.text, "html.parser")
    
    figures = []
    
    products = soup.find_all("div", class_="product-details")
    
    for product in products:
        name = product.find("div", class_="product-title").text.strip()
        price = product.find("div", class_='product-price').text.strip()
        link = "https://www.greenrockcomics.shop" + product.find("a")["href"]
        print(f'{name}: {price} - {link}')
    
        figures.append({'name': name,
                        'price': price,
                        'link': link})
    
    return figures 

def save_and_compare(new_data):
    
    """Compare with previous data, save new listings"""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            old_data = json.load(file)
            
    else:
        old_data = []
        
    old_names = {item['name'] for item in old_data}
    new_entries = [item for item in new_data if item['name'] not in old_names]
    
    if new_entries:
        print("NEW FIGURES FOUND")
        for figure in new_entries:
            print(f"- {figure['name']} ({figure['price']})")
            print(f" Link: {figure['link']}\n")
            
    else:
        print("No new figures added.")
        
    # SAVE LATEST DATA
    with open(DATA_FILE, 'w+') as file:
        json.dump(new_data, file, indent=4)
    
figures = fetch_figures()
save_and_compare(figures)