import requests
from bs4 import BeautifulSoup

# Function to scrape product information
def scrape_products(web_url, product_ids:list):
    try:
        # defining user-Agent header in the request to make it look more like a legitimate browser request
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }

        # Fetch the HTML content of the webpage
        response = requests.get(web_url, headers=headers)

        if response.status_code == 200:
            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.content, 'lxml')

            # List to store all the data of main products
            product_data = []

            product_links = []
            # Find the product elements
            for prod_id in product_ids:
                product = soup.find('div', id=prod_id)
                if product:
                    product_name = product.text.strip()
                    # Get the <a> tag within the product div to navigate to that link for extracting the product desc and image url
                    a_tag = product.find('a')
                    if a_tag:
                        # extract the href value of the product "a" tag
                        product_url = a_tag['href'] # type: ignore
                        product_link = web_url+product_url
                        product_response = requests.get(product_link, headers=headers)
                        if product_response.status_code == 200:
                            product_soup = BeautifulSoup(product_response.content, 'lxml')
                            product_details = product_soup.find('div', id='contentDiv')
                            if product_details:
                                # Find all <p> tags within product_details
                                product_paragraphs = product_details.find_all('p')
                                # Extract text from each <p> tag and join them into a single string
                                product_desc = ' '.join([p.text.strip() for p in product_paragraphs])
                                image_urls = [web_url+img['src'] for img in product_details.find_all('img')]
                                product_info = {
                                    'product_name': product_name,
                                    'product_description': product_desc,
                                    'product_image_urls': image_urls
                                    }
                                product_data.append(product_info)
                            else:
                                print(f"Product {product_name} does not have description.")
                        else:
                            print(f"Failed to scrape webpage for {product_name}. Status code:", response.status_code)
                    else:
                        print(f"Product {product_name} does not have any 'a' tag.")
                else:
                    print(f"Product with product Id {prod_id} not found.")
            return product_data
        else:
            print("Failed to scrape webpage. Status code:", response.status_code)
            return None
        
    except Exception as e:
        print("Error occurred during web scraping:", e)
        return None