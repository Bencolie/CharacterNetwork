# Use venv1
# lexicon for crowdsourcing sentiment analysis
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer 
import pandas as pd
import numpy as np

# Use vaderSentiment to calculate the sentiment score (compound)
def sentimentScore(sentence:str) -> float:
    score_dict = analyser.polarity_scores(sentence)
    """ Comments for debugging """
    #print(f"{sentence} : {score_dict['compound']}")
    return score_dict['compound']
# Use CountVectorizer to calculate the occurence of each character in each sentence
def occrencePerSent(sentences_list:list,characters:set):
    name_sent_occurence = list()
    vect = CountVectorizer(vocabulary=characters,binary=True,lowercase=False)
    occurence_vect = vect.fit_transform(sentences_list).toarray()
    for value in occurence_vect:
        float_value = [float(value[i]) for i in range(len(value))]
        name_sent_occurence.append(float_value)
    return np.array(name_sent_occurence)
# Make a Sentiment Socre Matrix
def sentimentPerSent(sentences_list:list):
    sentiment_score_list = [sentimentScore(sent) for sent in sentences_list]
    return np.array(sentiment_score_list)
# Do the calculation
def sentimentANDoccurenceMatrix(sentences_list:list,characters:list):
    name_sent_occurence = occrencePerSent(sentences_list,characters)
    sentiment_score = sentimentPerSent(sentences_list)
    #
    align_rate = np.sum(sentiment_score)/len(np.nonzero(sentiment_score)[0]) * -2
    occurence_matrix = np.dot(name_sent_occurence.T,name_sent_occurence)
    sentiment_matrix = np.dot(name_sent_occurence.T, (name_sent_occurence.T * sentiment_score).T)
    # 
    sentiment_matrix += align_rate*occurence_matrix
    # Symmetric Matrix -> keep only the lower triangle
    occurence_matrix = np.tril(occurence_matrix)
    sentiment_matrix = np.tril(sentiment_matrix)
    # Reduce the diagonal value to 0
    shape = occurence_matrix.shape[0]
    occurence_matrix[[range(shape)], [range(shape)]] = 0
    sentiment_matrix[[range(shape)], [range(shape)]] = 0
    return sentiment_matrix, occurence_matrix

analyser =  SentimentIntensityAnalyzer()