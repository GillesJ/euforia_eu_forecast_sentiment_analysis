# EUforia: Sentiment analysis on EU forecasts

Sentiment analysis for journalistic reporting on EU Forecasts per member-state.
Lexicon-based approaches (for now) using the following lexicons:
- McDonald and Loughan financial sentiment lexicon
- Harvard Inquirer 4 general purpose sentiment lexicon
- Lexicoder political sentiment lexicon

## Installation
Requirements:
- Python 3.5+
- Pip

Run:

`pip install pandas sklearn matplotlib git+https://github.com/hanzhichao2000/pysentiment/`

## Usage
- `./sentiment_analysis/settings.py`: Set in/output paths, analyser settings. Set FROM_SCRATCH to True to run sentiment analysis from scratch.
- `./sentiment_analysis/sentimentanalyser.py`: Run analysis and plotting.
- `./sentiment_analysis/preprocessor.py`: Functions for text preprocessing.
- `./sentiment_analysis/datahandler.py`: Functions for dataset reading, cleaning, and writing.

TODO:
- Implement Lexicoder political sentiment lexicon scoring
- Research more sentiment lexicons (political discourse could be useful)
- Combine results: scale scores, take into account subjectivity score in linear combination + use a voting or linear combination at document.


by Gilles Jacobs and Ioannis Antypas