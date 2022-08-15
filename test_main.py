import pandas as pd
import pytest
from main import create_df_from_dict

def test_create_df_from_dict():
    df = create_df_from_dict()
    assert len(df.columns) == 2

