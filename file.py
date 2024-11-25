import os
import pandas as pd


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))

    file_path = os.path.join(script_dir, 'Cyanobacteria2024.csv')
    bloom_df = pd.read_csv(file_path)
    print(bloom_df.head())


if __name__ == '__main__':
    main()