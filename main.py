# Use venv1 : source /Users/bencolie/Desktop/Github/CharacterNetwork/venv1/bin/activate
from FileManagement import *
from SentTokenizer import *
from NameEntityRecognition import *
from Coocurence_Sentiment import * 
from NetworkDisplay import *

def main():
    """
    PartI : NameEntityRecognition
    """ 
    datafile_name = 'AliceInWonderland'#-ch' + str(12)
    # load the text 
    text = readTextData(datafile_name)
    # Sentence Tokenization
    sentences_list = sentTokenizer(text)
    # Select possible character names
    candidate = nameEntityRecognition(sentences_list)
    # Use frequency to increase accuracy
    characters_freq = freqFilter(candidate,text)
    characters= list(zip(*characters_freq))[0]
    print(characters)
                
    """
    PartII : Cooccurence + SentimentAnalysis
    """
    coreffile_name = 'AliceInWonderland-coref'#-ch'+str(12)
    text = readTextCoref(coreffile_name)
    sentences_list = sent_tokenize(text)
    sentiment_matrix,occurence_matrix = sentimentANDoccurenceMatrix(sentences_list,characters)
    print(sentiment_matrix)
    networkxDisplay(sentiment_matrix,characters_freq)

if __name__ == "__main__":
    main()