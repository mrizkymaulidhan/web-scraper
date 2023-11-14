import datetime
import time
import json
import requests
from bs4 import BeautifulSoup

data_json={
    'link':'',
    'title':'',
    'scraping_time':''
}

news_data = []

url = 'https://www.pikiran-rakyat.com/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text,'html.parser')

if response.status_code == 200:
    pupuler = soup.find('h3', class_='title6', string='Terpopuler')
    if pupuler:
        obj = pupuler.find_next('div', class_='most__wrap')        
        obj = obj.find_all('a')
        
        for item in obj:
            data_json['link'] = item.get('href')
            data_json['title'] = item.find('h2').text
            data_json['scraping_time'] = time.asctime(time.localtime(time.time()))
            
            news_data.append(dict(data_json))
            
        print(news_data)

else:
    print(f'Request gagal (Status code: {response.status_code}) !!!')

with open ("scraping_result.json", "w") as write_file:
    json.dump(news_data, write_file, indent=1)
