import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path, on_bad_lines='skip')

def clean_data(data):
    # Menghapus baris dengan nilai yang hilang
    return data.dropna()

if __name__ == "__main__":
    data = load_data('data_penjualan.csv')
    data_cleaned = clean_data(data)
    data_cleaned.to_csv('data_cleaned.csv', index=False)