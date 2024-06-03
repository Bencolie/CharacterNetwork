# Use venv1
from FileManagement import *
from SentTokenizer import *
from NameEntityRecognition import *
from Coocurence_Sentiment import * 
from nltk.tokenize import sent_tokenize

def main():
    """
    PartI : NameEntityRecognition
    """
    
    #for i in range(1,13):
    datafile_name = 'AliceInWonderland-ch' + str(12)
    # load the text 
    text = readTextData(datafile_name)
    # Sentence Tokenization
    sentences_list = sentTokenizer(text)
    # Select possible character names
    candidate = nameEntityRecognition(sentences_list)
    # Use frequency to increase accuracy
    characters= freqFilter(candidate,text)
    print(characters)
    
    
    """
    PartII : Cooccurence + SentimentAnalysis
    """
    #for j in range(1,13):
    coreffile_name = 'AliceInWonderland-coref-ch'+str(12)
    text = readTextCoref(coreffile_name)
    sentences_list = sent_tokenize(text)
    """
    for sent in sentences_list:
        print(sent)
        print('-------------')
    """
    """
    sentiment_matrix,occurence_matrix = sentimentANDoccurenceMatrix(sentences_list,characters)
    print(sentiment_matrix)
    print('----------------')
    print(occurence_matrix)
    """
    
if __name__ == "__main__":
    main()