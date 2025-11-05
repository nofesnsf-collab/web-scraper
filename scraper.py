import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import logging
import os
# Setup logging
os.makedirs('logs', exist_ok=True)
logging.basicConfig(
level=logging.INFO,
format='%(asctime)s - %(levelname)s - %(message)s',
handlers=[
logging.FileHandler('logs/scraper.log'),
logging.StreamHandler()
]
)
class WebScraper:
"""Web scraper for extracting product data"""
def __init__(self, url, headers=None):
self.url = url
self.headers = headers or {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}
self.data = []
def fetch_page(self):
"""Fetch webpage content"""
try:
response = requests.get(self.url, headers=self.headers, timeout=10)
response.raise_for_status()
logging.info(f"Successfully fetched: {self.url}")
return response.text
except requests.RequestException as e:
logging.error(f"Error fetching {self.url}: {e}")
return None
def parse_products(self, html):
"""Parse HTML and extract product data"""
soup = BeautifulSoup(html, 'html.parser')
products = []
try:
# Customize selectors based on target website
product_items = soup.find_all('div', class_='product-item')
WEB SCRAPER - Python Files
FILE 1: scraper.py
for item in product_items:
try:
name_tag = item.find('h2', class_='product-name')
price_tag = item.find('span', class_='price')
link_tag = item.find('a', class_='product-link')
if name_tag and price_tag and link_tag:
products.append({
'Product Name': name_tag.get_text(strip=True),
'Price': price_tag.get_text(strip=True),
'URL': link_tag.get('href', ''),
'Timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
'Status': 'Active'
})
except Exception as e:
logging.warning(f"Error parsing product: {e}")
continue
logging.info(f"Parsed {len(products)} products")
except Exception as e:
logging.error(f"Error parsing HTML: {e}")
return products
def scrape(self):
"""Main scraping method"""
html = self.fetch_page()
if html:
self.data = self.parse_products(html)
return self.data
return []
def save_to_csv(self, filename='output/products.csv'):
"""Save data to CSV file"""
try:
os.makedirs('output', exist_ok=True)
df = pd.DataFrame(self.data)
df.to_csv(filename, index=False, encoding='utf-8')
logging.info(f"Data saved to {filename}")
return filename
except Exception as e:
logging.error(f"Error saving CSV: {e}")
return None
def get_summary(self):
"""Get scraping summary"""
return {
'Total Products': len(self.data),
'Timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
'Status': 'Success' if self.data else 'No data found'
