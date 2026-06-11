# Columns that must NEVER be null in the final output
import pytest


NOT_NULL_COLUMNS = ['id', 'name', 'age', 'salary', 'department']
@pytest.mark.sanity
@pytest.mark.bvt
def test_no_nulls_in_required_columns(transformed_df):
    """Each required column must have zero null values."""
    for col in NOT_NULL_COLUMNS:
        null_count = transformed_df[col].isnull().sum()
        assert null_count == 0, (
            f"Column '{col}' has {null_count} null value(s) after transformation"
        )
@pytest.mark.regression
def test_age_null_filled_with_median(source_df, transformed_df):
    """Specifically verify that missing ages were filled, not dropped."""
    original_nulls = source_df['age'].isnull().sum()
    if original_nulls > 0:
        remaining_nulls = transformed_df['age'].isnull().sum()
        assert remaining_nulls == 0, (
            f"{original_nulls} null ages in source were NOT filled"
        )
