from NameEntityRecognition import *
from CoWordAnalysis import *

def main():
    # load the text
    text = readText('AliceInWonderland-ch1')
    # nlp.tokenizer = customTokenizer1
    # Sentence Tokenization
    sentences_list = sentTokenizer(text)
    print(sentences_list[30:40])
    # Select possible character names
    #candidate = nameEntityRecognition(sentences_list)
    # Use frequency to increase accuracy
    #characters= freqFilter(candidate,text)
    

if __name__ == "__main__":
    main()