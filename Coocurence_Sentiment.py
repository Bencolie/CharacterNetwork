# Use venv1
# lexicon for crowdsourcing sentiment analysis
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize 
import pandas as pd

def interactionsSent(sentences_list:list,characters:set) -> list:
    interactions_sent = list()
    for sent in sentences_list:
        sent_set = set(word_tokenize(sent))
        multi_characters = sent_set.intersection(characters)
        if len(multi_characters) >=2:
            interactions_sent.append(sent)
    return interactions_sent

def sentimentScore(interactions_sent:list):
    analyser =  SentimentIntensityAnalyzer()
    score_list = [analyser.polarity_scores(sent) for sent in interactions_sent]
    """ Comments for debugging """
    #for idx,sent in enumerate(interactions_sent):
        #print(f"{sent} : {score_list[idx]}")
    return score_list
   
