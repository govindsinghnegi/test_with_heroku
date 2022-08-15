import pandas as pd

def create_df_from_dict():
    data = {'col_1': [3, 2, 1, 0], 'col_2': ['a', 'b', 'c', 'd']}
    return pd.DataFrame.from_dict(data)

if __name__ == "__main__":
    df = create_df_from_dict()
    print(df.shape)