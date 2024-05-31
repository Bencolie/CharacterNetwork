# Use venv1
# lexicon for crowdsourcing sentiment analysis
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd

def sentimentScore(sentences_list:list):
    analyser =  SentimentIntensityAnalyzer()
    score_list = [analyser.polarity_scores(sent) for sent in sentences_list]
    for idx,sent in enumerate(sentences_list):
        print(f"{sent} : {score_list[idx]}")
    return score_list
    
