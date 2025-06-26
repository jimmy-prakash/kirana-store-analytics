def clean_dates(df):
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    return df.dropna(subset=['Date'])
