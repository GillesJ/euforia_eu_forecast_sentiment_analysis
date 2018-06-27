#!/usr/bin/env python3
'''
settings.py
euforia_eu_forecast_sentiment_analysis 
6/6/18
Copyright (c) Gilles Jacobs. All rights reserved.  
'''
DATASET_FP = "../dataset/forecasts_eu.tsv"
LEXICODER_DIRP = "/home/gilles/software/Lexicoder 3.0/dat/"
LEXICODER_COUNT_FP = "../dataset/lexicoder_counts.tsv"
OPT_FP = "../dataset/sentiment_forecast_eu.tsv"
VALID_STATE_FP = "../dataset/countrylist.txt"

FROM_SCRATCH = True # redo sentiment analysis from scratch, false load from OPT_FP