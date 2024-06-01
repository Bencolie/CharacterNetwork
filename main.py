# Use venv1
from FileManagement import *
from SentTokenizer import *
from NameEntityRecognition import *
from Coocurence_Sentiment import * 

def main():
    """
    PartI : NameEntityRecognition
    """
    # load the text
    text = readTextData('AliceInWonderland-ch1')
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
    text = readTextCoref('AliceInWonderland-ch1-coref')
    sentences_list = sentTokenizer(text)
    interactions_sent = interactionsSent(sentences_list,characters)
    sentimentScore(interactions_sent)
    
if __name__ == "__main__":
    main()