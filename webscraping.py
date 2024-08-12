import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL halaman yang ingin di-scrape
url = 'http://books.toscrape.com/'

# Mengambil konten halaman web
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Menentukan elemen HTML yang berisi data
data = []
books = soup.find_all('article', class_='product_pod')

# Mengambil data buku
for book in books:
    title = book.h3.a['title']
    price = book.select_one('p.price_color').text
    rating = book.p['class'][1]
    data.append([title, price, rating])

# Menyimpan data ke CSV dengan nama file yang baru
df = pd.DataFrame(data, columns=['Title', 'Price', 'Rating'])
df.to_csv('data_penjualan.csv', index=False)

print("Data telah disimpan ke data_penjualan.csv")