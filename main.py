import json
from script import scrape_products

# URL of the webpage to scrape
web_url = "https://www.norlandbiotech.com"

# Ids of the main products
product_ids = ["w_common_text-1570525614358", "w_common_text-1570525698742", "w_common_text-1570525818094", "w_common_text-1570525848492", "w_common_text-1570525729725", "w_common_text-1570525706381", "w_common_text-1570525782726"]


scraped_products = scrape_products(web_url, product_ids)

# Save product data to a JSON file
with open('product_data.json', 'w') as json_file:
    json.dump(scraped_products, json_file, indent=4)

print(scraped_products)
