import os
import pandas as pd

def extract(filepath: str) -> pd.DataFrame:
    """Read raw data from a CSV file."""
    return pd.read_csv(filepath)

def transform(df: pd.DataFrame) -> pd.DataFrame:
    """Clean and transform the data."""
    # Remove duplicate rows
    df = df.drop_duplicates()

    # Fill missing ages with the median
    df['age'] = df['age'].fillna(df['age'].median())

    # Normalize text: strip whitespace, lowercase department
    df['name'] = df['name'].str.strip()
    df['department'] = df['department'].str.upper()

    # Add a derived column
    df['annual_bonus'] = df['salary'] * 0.10

    return df

#def load(df: pd.DataFrame, output_path: str) -> None:
    """Save transformed data."""
    df.to_csv(output_path, index=False)

def load(df, output_path: str):
    # Ensure parent folder exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
