from bs4 import BeautifulSoup
import requests
nft_trending_url = 'https://coinmarketcap.com/nft/collections'

response = requests.get(nft_trending_url)
print('status', response.status_code)
print('Output',response.text[:1000])
with open('trending.html', 'w') as f:
  f.write(response.text)

doc = BeautifulSoup(response.text,'html.parser')

#find the division containing table
table_row_div = doc.find_all('table',class_='cmc-table')
kj= len(table_row_div)
print(kj)

