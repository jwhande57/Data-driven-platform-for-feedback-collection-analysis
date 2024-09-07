import pandas as pd
from textblob import TextBlob

def load_data(file_path):
    df = pd.read_csv(file_path)
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df["areas needing improvement"].astype(str)
    df['greatest strength'] = df['greatest strength'].astype(str)
    df['Sentiment'] = df['greatest strength'].apply(lambda x: TextBlob(x).sentiment.polarity if isinstance(x, str) and x.strip() else None)
    return df

def apply_filters(df, department_filter, program_filter, year_filter, selected_year, selected_month):
    filtered_df = df.copy()

    if department_filter != "All":
        filtered_df = filtered_df[filtered_df["department"] == department_filter]
    if program_filter != "All":
        filtered_df = filtered_df[filtered_df["program of study"] == program_filter]
    if year_filter != "All":
        filtered_df = filtered_df[filtered_df["year of study"] == year_filter]
    if selected_year != "All":
        filtered_df = filtered_df[filtered_df['date'].dt.year == selected_year]
    if selected_month != "All":
        filtered_df = filtered_df[filtered_df['date'].dt.month == selected_month]

    return filtered_df
