import pandas as pd
import os
import sys

def load_dataset(file_path: str) -> pd.DataFrame:
    """
    Function Loads a CSV dataset from the specified path.

    Args:
        file_path (str): Relative or absolute path to the CSV file.

    Returns:
        pd.DataFrame: Loaded data as a pandas DataFrame.

    """
    if not os.path.exists(file_path):
        print(f"Error: File not found at {file_path}")
        sys.exit(1)

    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        print(f"Error reading CSV: {e}")
        sys.exit(1)

    return df