import requests
from bs4 import BeautifulSoup as bs

HEADERS = {"User-Agent": "Mozilla/5.0"}

# Green Rock Comics
SHOP_URLS = {"green_rock": "https://www.greenrockcomics.shop",}

LINK_URLS = {
    "green_rock_dc": "https://www.greenrockcomics.shop/collections/dc-multiverse",
    "green_rock_marvel": "https://www.greenrockcomics.shop/collections/marvel-toys",
    "green_rock_transformers": "https://www.greenrockcomics.shop/collections/transformers"
}

SHOP = {
    "green_rock": "Green Rock Comics",
    "culture_shock": "Culture Shock Collectables",
    "popcultcha": "Popcultcha",
    "zing": "ZING Pop Culture",
    "angel_grove": "Angel Grove Collectibles"
}

def scrape(link_url, shop_url, shop_name):
    figures = []
    
    if shop_name is SHOP["green_rock"]:
        response = requests.get(link_url, headers=HEADERS)
        soup = bs(response.text, "html.parser")
        products = soup.find_all("div", class_="product-details")
    
        for product in products:
            name = product.find("div", class_="product-title").text.strip()
            price = product.find("div", class_='product-price').text.strip()
            link = shop_url + product.find("a")["href"]

            if link_url is LINK_URLS["green_rock_dc"]:
                figures.append({'store': shop_name,
                                'line': 'McFarlane DC',
                                'name': name,
                                'price': price,
                                'link': link})
                
            elif link_url is LINK_URLS["green_rock_marvel"]:
                figures.append({'store': shop_name,
                                'line': 'Marvel Legends',
                                'name': name,
                                'price': price,
                                'link': link})
                
            elif link_url is LINK_URLS["green_rock_transformers"]:
                figures.append({'store': shop_name,
                                'line': 'Transformers',
                                'name': name,
                                'price': price,
                                'link': link})
    
    elif shop_name is SHOP["culture_shock"]:
        print("CULTURE SHOCK")
    
    elif shop_name is SHOP["popcultcha"]:
        print("POPCULTCHA")
    
    elif shop_name is SHOP["zing"]:
        print("ZING")
    
    elif shop_name is SHOP["angel_grove"]:
        print("ANGEL GROVE")

    return figures

def get_all_figures():
    figures = []
    
    figures.extend(scrape(LINK_URLS["green_rock_dc"], SHOP_URLS["green_rock"], SHOP["green_rock"]))
    figures.extend(scrape(LINK_URLS["green_rock_marvel"], SHOP_URLS["green_rock"], SHOP["green_rock"]))
    figures.extend(scrape(LINK_URLS["green_rock_transformers"], SHOP_URLS["green_rock"], SHOP["green_rock"]))
    
    return figures