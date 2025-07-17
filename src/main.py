import os
import pandas as pd

from preprocessing import preprocess_text
from data_loader import load_dataset


if __name__ == "__main__":
    ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
    DATA_PATH = os.path.join(ROOT_DIR, "data", "IMDB Dataset.csv")
    df = load_dataset(DATA_PATH)

    # appling text preprocessing
    df["cleaned_review"] = df["review"].apply(preprocess_text)

    print(df[["review", "cleaned_review"]].head())

    