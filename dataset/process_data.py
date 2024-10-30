import os
import pandas as pd

RAW_DATA_DIR = "raw_data"

def main():
    df_l = []
    for filename in os.listdir(RAW_DATA_DIR):
        with open(os.path.join(RAW_DATA_DIR, filename)) as f:
            df_l.append(pd.read_csv(f))

    df = pd.concat(df_l)
    print(df.head())


if __name__=="__main__": main()