import os
from dotenv import load_dotenv
from scraper import WebScraper
import logging
load_dotenv()
# Configuration
TARGET_URL = "https://example-ecommerce.com/products" # Change this to your target
# Email configuration
EMAIL_USER = os.getenv('EMAIL_USER')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
TARGET_EMAIL = os.getenv('TARGET_EMAIL')
logger = logging.getLogger(__name__)
def run_scraper():
"""Run the scraper"""
logger.info("Starting web scraper...")
scraper = WebScraper(TARGET_URL)
products = scraper.scrape()
if products:
# Save to CSV
scraper.save_to_csv()
# Print summary
summary = scraper.get_summary()
logger.info(f"Summary: {summary}")
return True
else:
logger.warning("No products found")
return False
if __name__ == "__main__":
# Run once
run_scraper()
# For scheduled execution, uncomment below:
# import schedule
# import time
#
# schedule.every(1).hours.do(run_scraper)
#
# while True:
# schedule.run_pending()
# time.sleep(60)