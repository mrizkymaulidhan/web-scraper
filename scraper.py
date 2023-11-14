import time
import json
import requests
from bs4 import BeautifulSoup

news_data = []
data_json = {}
filename = 'scraping_result.json'

url = 'https://www.pikiran-rakyat.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text,'html.parser')

if response.status_code == 200:
    populer = soup.find('h3', class_='title6', string='Terpopuler')
    populer = populer.find_next('div', class_='most__wrap')        
    populer = populer.find_all('a')
        
    for item in populer:
        data_json['url'] = item.get('href')
        data_json['title'] = item.find('h2').text
        data_json['scraping_time'] = time.asctime(time.localtime(time.time()))  
        news_data.append(dict(data_json))
    
else:
    print(f'Request gagal (Status code: {response.status_code}) !!!')

if news_data:
    with open (filename, "w") as write_file:
        json.dump(news_data, write_file, indent=1)
    print(f'Data berhasil disimpan ke dalam file {filename}!')

else:
    print(f'Data tidak berhasil disimpan!')