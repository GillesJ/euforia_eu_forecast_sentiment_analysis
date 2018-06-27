#!/usr/bin/env python3
'''
datahandler.py
euforia_eu_forecast_sentiment_analysis 
6/6/18
Copyright (c) Gilles Jacobs. All rights reserved.  
'''
import pandas as pd
import numpy as np
from sentiment_analysis import settings, preprocessor

def clean_dataset(df):
    '''
    Ensure "text" column is all str.
    Ensure "state" are member state.
    If conditions are not met, set value to empty or nan.
    Nan values are removed.
    Convert date field to datetime.
    Clean text field from pdf text artifacts.
    :param df: Dataframe loaded from eu_forecast dataset.
    :return: Cleaned dataframe
    '''
    # check if state field is valid
    with open(settings.VALID_STATE_FP, "rt") as valid_in:
        valid_states = [c.lower() for c in valid_in.read().splitlines()]
    mask = df["state"].str.lower().isin(valid_states)
    df = df.where(mask, other=np.nan)
    # ensure text are strings, no text = remove
    df["text"].astype(str)
    # convert empty values and "None" strings to NaN
    df = df.replace('None', np.nan)
    # drop rows containing nan
    df = df.dropna(axis=0, subset=["date", "state", "text"]).reset_index(drop=True)
    # convert date field to datetime
    df["date"] = pd.to_datetime(df["date"])
    # clean text
    df["text"] = df["text"].apply(preprocessor.clean_text)
    return df

def write_data(df, fp):
    try:
        df.to_csv(fp, sep="\t")
        print(f"Wrote dataframe to {fp}.")
    except Exception as e:
        print(e, f"Failed to write dataframe to {fp}.")


def read_data(fp):
    return pd.read_csv(fp, sep="\t")