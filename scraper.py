# Import library
import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime

# Inisialisasi variabel untuk kebutuhan penyimpanan data
news_data = []
data_json = {
    'title':'',
    'content':'',
    'author':'',
    'url':'',
    'published_at':'',
    'scraped_at':'',
}
filename = 'scraping_result.json'

# Inisialisasi variabel sumber berita
url = 'https://www.pikiran-rakyat.com/'

# Mendefinisikan user-agent untuk dapat mengakses sumber berita
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
}

# Mengambil halaman sumber berita
page_response = requests.get(url, headers=headers)
soup = BeautifulSoup(page_response.text, 'html.parser')

if page_response.status_code == 200:
    # Menemukan bagian berita "Terpopuler"
    populer = soup.find('h3', class_='title6', string='Terpopuler')
    populer = populer.find_next('div', class_='most__wrap')        
    populer = populer.find_all('a')
        
    for item in populer:
        # Menyimpan URL dan judul berita
        data_json['url'] = item.get('href')
        data_json['title'] = item.find('h2').text.strip()
        
        # Mengambil konten dari halaman berita
        article_url = item.get('href')
        url_response = requests.get(article_url, headers=headers)
        soup2 = BeautifulSoup(url_response.text, 'html.parser')
        
        if url_response.status_code == 200:
            # Menemukan konten artikel
            obj = soup2.find('div', class_='col-bs12-8')
            article = obj.find_next('article', class_='read__content')
                        
            # Menyimpan informasi penulis dan tanggal publikasi
            data_json['author'] = obj.find('div', class_='read__info__author').text.strip()
            data_json['published_at'] = obj.find('div', class_='read__info__date').text.replace('-', '').strip()
            
            text = ''
            
            # Menghapus tag 'strong' dan 'a' dari konten
            for strong_tag in article.find_all('strong'):
                strong_tag.decompose()

            for a_tag in article.find_all('a'):
                a_tag.decompose()

            # Mengambil teks dari paragraf dan menggabungkannya ke dalam variabel
            for paragraph in article.find_all('p'):
                text += paragraph.text.replace('-', '').strip()
            
            data_json['content'] = text

        else:
            print(f'Request url {article_url} gagal (Status code: {url_response.status_code}) !!!')
        
        # Menyimpan informasi waktu saat proses scraping dilakukan
        data_json['scraped_at'] = str(datetime.now().strftime("%d %B %Y, %H:%M WIB"))
        
        # Menambahkan data berita ke dalam list
        news_data.append(dict(data_json))
    
else:
    print(f'Request gagal (Status code: {page_response.status_code}) !!!')

# Menyimpan data berita ke dalam file JSON
if news_data:
    with open (filename, "w") as write_file:
        json.dump(news_data, write_file, indent=3)
    print(f'Data berhasil disimpan ke dalam file {filename}!')

else:
    print(f'Data tidak berhasil disimpan!')