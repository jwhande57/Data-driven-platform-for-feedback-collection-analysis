import pandas as pd
import os

def save_data(data, filename="data\student_feedback_data.csv"):
    if os.path.exists(filename):
        df_existing = pd.read_csv(filename)
        df_new = pd.DataFrame([data])
        df = pd.concat([df_existing, df_new], ignore_index=True)
    else:
        df = pd.DataFrame([data])
    df.to_csv(filename, index=False)
