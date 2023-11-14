# Web Scraper untuk Pikiran Rakyat

![Beautiful Soup](https://img.shields.io/badge/Made%20with-Beautiful%20Soup-orange)

Web scraper sederhana yang dibangun menggunakan bahasa pemrograman Python dan Beautiful Soup untuk mengambil daftar judul dan isi berita terpopuler dari halaman [Pikiran Rakyat](https://www.pikiran-rakyat.com/).

## Deskripsi
Projek ini bertujuan untuk mengumpulkan informasi mengenai berita-berita terpopuler yang terdapat pada halaman utama Pikiran Rakyat. Web scraper ini dibangun menggunakan library Beautiful Soup untuk melakukan ekstraksi data dari halaman web dan mengambil judul serta isi dari berita-berita yang populer.

## Penggunaan
1. Pastikan Anda memiliki Python diinstal.
2. Instal library Beautiful Soup dengan menjalankan perintah:
    ```bash
    pip install beautifulsoup4
    ```
3. Jalankan skrip Python untuk mengumpulkan data dari Pikiran Rakyat.

## Struktur File
- `scraper.py`: Skrip Python yang mengimplementasikan web scraper menggunakan Beautiful Soup.
- `scraping_result.json`: File JSON yang berisi data judul dan isi berita terpopuler.

## Cara Kerja
1. Mengakses halaman web Pikiran Rakyat.
2. Mencari daftar berita terpopuler.
3. Mengambil judul dan isi dari masing-masing berita terpopuler.

## Catatan Penting
Pastikan untuk menggunakan scraper ini sesuai dengan kebijakan dan batasan yang diberlakukan oleh Pikiran Rakyat. Penggunaan scraper ini sepenuhnya menjadi tanggung jawab pengguna.

## Lisensi
Proyek ini dilisensikan di bawah [MIT License](LICENSE).
