from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

class WebScraper:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.data = {
            'images': [],
            'links': [],
            'buttons': [],
            'products': []
        }

    def extract_images(self):
        """Extract all images with src and alt attributes"""
        images = self.driver.find_elements(By.TAG_NAME, 'img')
        for img in images:
            self.data['images'].append({
                'src': img.get_attribute('src'),
                'alt': img.get_attribute('alt') or ''
            })

    def extract_links(self):
        """Extract all links with href and text"""
        links = self.driver.find_elements(By.TAG_NAME, 'a')
        for link in links:
            self.data['links'].append({
                'href': link.get_attribute('href'),
                'text': link.text.strip()
            })

    def extract_buttons(self):
        """Extract all buttons with text"""
        buttons = self.driver.find_elements(By.TAG_NAME, 'button')
        for btn in buttons:
            self.data['buttons'].append({
                'text': btn.text.strip()
            })

    def extract_products(self):
        """Extract product titles"""
        products = self.driver.find_elements(By.CLASS_NAME, "ps-title")
        for product in products:
            self.data['products'].append({
                'title': product.get_attribute('innerHTML')
            })

    def save_to_excel(self):
        """Save all collected data to Excel"""
        with pd.ExcelWriter('scraped_data.xlsx') as writer:
            for data_type, items in self.data.items():
                if items:  # Only create sheet if there's data
                    pd.DataFrame(items).to_excel(writer, sheet_name=data_type, index=False)

    def scrape(self, url):
        """Main scraping function"""
        self.driver.get(url)
        time.sleep(2)  # Wait for page to load
        
        self.extract_images()
        self.extract_links()
        self.extract_buttons()
        self.extract_products()
        
        self.save_to_excel()
        self.driver.quit()

if __name__ == "__main__":
    scraper = WebScraper()
    scraper.scrape("https://www.dell.com/en-in/search/laptop")
