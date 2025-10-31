import pandas as pd


def clean_dates(df):
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    return df.dropna(subset=['Date'])


# ---------------- Additional Cleaning Utilities ---------------- #

def clean_text_columns(df, text_columns):
    """
    Standardize text columns: lowercase, strip spaces, and fix common typos.
    """
    for col in text_columns:
        df[col] = df[col].astype(str).str.strip().str.lower()
    return df


def handle_missing_values(df, strategy="drop", fill_values=None):
    """
    Handle missing values.
    strategy: 'drop' or 'fill'
    fill_values: dict (e.g., {'Quantity Sold': 0, 'Category': 'unknown'})
    """
    if strategy == "drop":
        df = df.dropna()
    elif strategy == "fill" and fill_values:
        df = df.fillna(fill_values)
    return df


def remove_duplicates(df):
    """
    Remove duplicate rows based on all columns.
    """
    before = df.shape[0]
    df = df.drop_duplicates()
    after = df.shape[0]
    print(f"Removed {before - after} duplicate rows.")
    return df
