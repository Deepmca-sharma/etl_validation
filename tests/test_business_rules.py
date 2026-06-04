def test_salary_must_be_positive(transformed_df):
    """No employee can have zero or negative salary."""
    invalid = transformed_df[transformed_df['salary'] <= 0]
    assert len(invalid) == 0, (
        f"{len(invalid)} rows have invalid salary:\n{invalid[['id', 'name', 'salary']]}"
    )

def test_age_within_valid_range(transformed_df):
    """Ages should be between 18 and 100 — anything else is data corruption."""
    invalid = transformed_df[
        (transformed_df['age'] < 18) | (transformed_df['age'] > 100)
    ]
    assert len(invalid) == 0, (
        f"Invalid ages found:\n{invalid[['id', 'name', 'age']]}"
    )

def test_department_values_are_valid(transformed_df):
    """Department must be one of the known values after uppercasing."""
    VALID_DEPARTMENTS = {'HR', 'IT', 'FINANCE', 'SALES', 'OPERATIONS'}
    invalid_depts = set(transformed_df['department'].unique()) - VALID_DEPARTMENTS
    assert len(invalid_depts) == 0, f"Unknown departments: {invalid_depts}"

def test_annual_bonus_is_10_percent_of_salary(transformed_df):
    """Derived column: bonus must exactly equal 10% of salary."""
    expected = (transformed_df['salary'] * 0.10).round(2)
    actual = transformed_df['annual_bonus'].round(2)
    mismatches = transformed_df[expected != actual]
    assert len(mismatches) == 0, (
        f"{len(mismatches)} rows have wrong bonus calculation"
    )
