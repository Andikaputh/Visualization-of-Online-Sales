import pandas as pd

def explore_data(file_path):
    data = pd.read_csv(file_path)
    print(data.head())
    print(data.info())
    print(data.describe())

if __name__ == "__main__":
    explore_data('data_cleaned.csv')