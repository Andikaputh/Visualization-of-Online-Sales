import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_sales_trend(data):
    data['Tanggal'] = pd.to_datetime(data['Tanggal'])
    sales_per_day = data.groupby('Tanggal')['Penjualan'].sum()
    plt.figure(figsize=(10, 6))
    plt.plot(sales_per_day.index, sales_per_day.values)
    plt.title('Tren Penjualan Harian')
    plt.xlabel('Tanggal')
    plt.ylabel('Total Penjualan')
    plt.show()

def plot_top_products(data):
    top_products = data.groupby('Produk')['Penjualan'].sum().sort_values(ascending=False).head(10)
    plt.figure(figsize=(10, 6))
    top_products.plot(kind='bar')
    plt.title('10 Produk Terlaris')
    plt.xlabel('Produk')
    plt.ylabel('Total Penjualan')
    plt.show()

def plot_correlation(data):
    plt.figure(figsize=(10, 6))
    sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
    plt.title('Korelasi Antar Variabel')
    plt.show()

if __name__ == "__main__":
    data = pd.read_csv('data_cleaned.csv')
    plot_sales_trend(data)
    plot_top_products(data)
    plot_correlation(data)