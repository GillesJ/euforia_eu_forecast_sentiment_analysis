#!/usr/bin/env python3
'''
preprocessor.py
euforia_eu_forecast_sentiment_analysis 
6/6/18
Copyright (c) Gilles Jacobs. All rights reserved.  
'''
import re

def clean_text(txt):
    try:
        txt = " ".join(txt.split())  # remove double whitespace
        txt = re.sub(r"\b\-\s\b", "", txt)

    except Exception as e:
        print(str(e), "Failed to clean text.")
    return txt