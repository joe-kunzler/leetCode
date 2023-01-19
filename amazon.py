import requests
from bs4 import BeautifulSoup

url = 'https://www.ebay.com'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

product_title = soup.find('h3').get_text()
product_price = soup.find(class_='x-price-primary').get_text()

print(f'Title: {product_title}\nPrice: {product_price}')
