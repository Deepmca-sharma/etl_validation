import pytest
import pandas as pd
import sys, os

# Make sure Python can find the etl/ folder
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from etl.pipeline import extract, transform, load

BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # project root
SOURCE_PATH = os.path.join(BASE_DIR, "data", "source_data.csv")
#SOURCE_PATH = "data/source_data.csv"
OUTPUT_PATH = "data/transformed_data.csv"

@pytest.fixture(scope="session")
def source_df():
    """Load the raw source data once for the whole test session."""
    return extract(SOURCE_PATH)

@pytest.fixture(scope="session")
def transformed_df(source_df):
    """Run the ETL transformation and return the result."""
    df = transform(source_df.copy())
    load(df, OUTPUT_PATH)
    return df
#scope="session"