from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
nft_trending_url = 'https://coinmarketcap.com/nft/collecttions'

def get_driver():
 chrome_options = Options()
 chrome_options.add_argument('--no-sandbox')
 chrome_options.add_argument('--headless')
 chrome_options.add_argument('--disable-dev-shm-usage')
 driver = webdriver.Chrome(options=chrome_options)
 return driver

if __name__ == "__main__" :
 print('Creating driver')
 driver = get_driver()
 print('fetching the page')
 driver.get(nft_trending_url)
 print('Page title:', driver.title)
 print('get the content div')
 table_class='H7VNX2-2.EPPvUK.cmc-table'
 table_divs = driver.find_elements(By.CLASS_NAME,table_class)
 print(f' Found {len(table_divs)} table')
