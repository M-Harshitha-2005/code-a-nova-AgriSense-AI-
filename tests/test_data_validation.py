import pandas as pd

df = pd.read_csv("data/cleaned_crop_data.csv")

def test_missing_values():
    assert df.isnull().sum().sum() == 0

def test_duplicate_records():
    assert df.duplicated().sum() == 0

def test_dataset_not_empty():
    assert len(df) > 0

def test_target_column_exists():
    assert "label" in df.columns