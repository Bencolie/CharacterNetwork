# dealing with regex,string and file paths
import os,math
# if line 4 and 5 have been executed, please comment it out
#import nltk
#nltk.download("popular")
from nltk.tokenize import PunktSentenceTokenizer
# use spaCy for name entity recognization
import spacy
from spacy.matcher import Matcher
from spacy.tokens import Doc
# use scikit-learn for name freqency filter
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
from functools import reduce

# file input
def readText(file_name):
    # adapt different directory structure
    file_path = os.path.abspath(f"TextData/{file_name}.txt")
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text
# setence tokenization
def sentTokenizer(text):
    tokenizer = PunktSentenceTokenizer()
    sentences_list = tokenizer.tokenize(text)
    return sentences_list
# Rule-based Matcher
def defPattern():
    matcher = Matcher(nlp.vocab)
    noun_name_pattern = [[{'ENT_TYPE':'PERSON'}],
                     [{'DEP':'nsubj','IS_LOWER':False,'IS_STOP':False}]]
    # Add rules to Matcher
    matcher.add('noun_name',noun_name_pattern)
    return matcher
def nameEntityRecognition(sentences_list):
    
    candidate = list()
    for sent in sentences_list:
        doc = nlp(sent)
        matcher = defPattern()
        matches = matcher(doc)
        for match_id,start,end in matches:
            span = doc[start:end]
            '''Comments below are for debugging'''
            #match_group = nlp.vocab.strings[match_id]
            #print(f"{match_group}:{span.text}")
            candidate.append(span.text)
    # reduce to non repetitive elements set
    candidate = set(candidate)
    return candidate
# filter out candidates that have low freqency
def freqFilter(candidate,text):
    vect = CountVectorizer(vocabulary=list(candidate),lowercase=False)#tokenizer=customTokenizer2
    candidate_freq = vect.fit_transform([text[:]])
    candidate_freq = pd.DataFrame(candidate_freq.toarray(),columns=vect.get_feature_names_out())
    candidate_freq = candidate_freq.T
    candidate_freq = candidate_freq.sort_values(by=0, ascending=False)
    '''Comments for debugging'''
    #pd.set_option('display.max_rows', None)
    #print(candidate_freq)
    
    # average frequency to increase acuracy
    freq_list = list(candidate_freq[0])
    avg_freq = reduce(lambda a,b : a+b,freq_list)/len(freq_list)
    candidate_index = list(candidate_freq.index)
    characters = [candidate_index[i] for i in range(len(freq_list)) if freq_list[i] >= math.floor(avg_freq)]
    return characters
# load the English language model
nlp = spacy.load('en_core_web_sm') #if error is raised, please do "Python3.11 -m spacy dowload en_core_web_sm"