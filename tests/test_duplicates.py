import pytest

@pytest.mark.sanity
@pytest.mark.bvt
def test_no_duplicate_rows(transformed_df):
    """Output should have no fully duplicated rows."""
    duplicate_count = transformed_df.duplicated().sum()
    assert duplicate_count == 0, f"Found {duplicate_count} fully duplicate rows"
@pytest.mark.regression
def test_no_duplicate_ids(transformed_df):
    """Each ID should appear exactly once — this is the primary key check."""
    duplicate_ids = transformed_df[transformed_df.duplicated(subset=['id'])]['id'].tolist()
    assert len(duplicate_ids) == 0, f"Duplicate IDs found: {duplicate_ids}"
