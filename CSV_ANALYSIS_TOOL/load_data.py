import pandas as pd

def load_csv(file_path):
    try:
        df = pd.read_csv(file_path)
        print("CSV Loaded Successfully!")
        return df

    except Exception as e:
        print("Error:", e)
        return None