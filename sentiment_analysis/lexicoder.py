#!/usr/bin/env python3
'''
Preprocessing and writing to file for ease of use with Lexicoder SA programme.
lexicoder.py
euforia_eu_forecast_sentiment_analysis
6/6/18
Copyright (c) Gilles Jacobs. All rights reserved.
'''
from sentiment_analysis import datahandler, settings, sentimentanalyser
import os
import pandas as pd

def add_lexicoder(df):
    try:
        lexicoder_df = datahandler.read_data(settings.LEXICODER_COUNT_FP)
    except Exception as e:
        print(e, "Ensure you have run seperate Lexicoder 3.0 dictionary count cf. Usage.")

    lexicoder_df["index"] = lexicoder_df["case"].apply(lambda x: int(x.split("_")[0]))
    lexicoder_df = lexicoder_df.set_index("index").sort_index()
    if df.shape[0] != lexicoder_df.shape[0]:
        raise ValueError("The lexicoder count dataset and base dataset have different row counts.")

    df = pd.concat([df, lexicoder_df], axis=1,)

    df = df.rename(index=str, columns={"negative": "lexicoder_negative", "positive": "lexicoder_positive"})
    df["lexicoder_polarity"] = df.apply(
        lambda x: sentimentanalyser.compute_polarity_score(
            x["lexicoder_positive"],
            x["lexicoder_negative"],
        ),
        axis = 1,
    )

    df["lexicoder_subjectivity"] = df.apply(
        lambda x: sentimentanalyser.compute_subjectivity_score(
            x["lexicoder_positive"],
            x["lexicoder_negative"],
            len(x["alltext"].split())
        ),
        axis=1,
    )
    df = df.drop(["case"], axis=1)

    return df

def preprocess_lexicoder(lexicoder_dirp):
    os.makedirs(lexicoder_dirp, exist_ok=True)
    df = datahandler.read_data(settings.DATASET_FP)
    df = datahandler.clean_dataset(df)
    df["alltext"] = df.apply(lambda row: sentimentanalyser.combine_title_text(row), axis=1)
    for index, row in df.iterrows():
        fn = f"{index:04d}_{row['date']}_{row['state']}.txt"
        fp = os.path.join(settings.LEXICODER_DIRP, fn)
        with open(fp, "wt") as f_out:
            f_out.write(row["alltext"])

if __name__ == "__main__":
    preprocess_lexicoder(settings.LEXICODER_DIRP)
