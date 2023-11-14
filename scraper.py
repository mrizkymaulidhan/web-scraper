import time
import json
import requests
from bs4 import BeautifulSoup

def scrape_news(url, headers):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

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
                
            return news_data

        else:
            print("Elemen 'Terpopuler' tidak ditemukan.")
            return None

    else:
        print(f'Request gagal (Status code: {response.status_code}) !!!')
        return None

def save_to_json(data, filename):
    if data:
        with open(filename, "w") as write_file:
            json.dump(data, write_file, indent=1)
        print(f"Data berhasil disimpan ke {filename}")
    else:
        print("Tidak ada data yang disimpan.")

if __name__ == "__main__":
    news_data = []
    data_json = {
        'link': '',
        'title': '',
        'scraping_time': ''
    }
    url = 'https://www.pikiran-rakyat.com/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
    }
    
    scraped_data = scrape_news(url, headers)
    save_to_json(scraped_data, "scraping_result.json")