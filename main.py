import pandas as pd
from preprocessing import preprocess_text
from data_loader import load_dataset

if __name__ == "__main__":
    path = "data/IMDB Dataset.csv"
    df = load_dataset(path)

    # Apply text preprocessing
    df["cleaned_review"] = df["review"].apply(preprocess_text)

    print(df[["review", "cleaned_review"]].head())
