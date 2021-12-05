from selenium import webdriver
from selenium.webdriver.chrome.options import Options

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
 
 print('get the list div')
 name_list_table_class='cmc-table'
 name_divs = driver.find_elements_by_class_name(name_list_table_class)
 print(f'found {len(name_divs)}table')
