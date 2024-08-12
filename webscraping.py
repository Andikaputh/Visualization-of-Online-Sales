import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL halaman e-commerce yang ingin di-scrape
url = 'https://books.toscrape.com/'

# Mengambil konten halaman web
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Menentukan elemen HTML yang berisi data
data = []
table = soup.find('table', {'id': 'sales-data-table'})  # Ganti dengan elemen yang sesuai
rows = table.find_all('tr')

# Mengambil header
headers = [header.text for header in rows[0].find_all('th')]

# Mengambil baris data
for row in rows[1:]:
    cols = row.find_all('td')
    data.append([col.text for col in cols])

# Menyimpan data ke CSV
df = pd.DataFrame(data, columns=headers)
df.to_csv('data_penjualan.csv', index=False)

print("Data telah disimpan ke data_penjualan.csv")
