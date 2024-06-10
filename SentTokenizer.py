# Use venv1 : source /Users/bencolie/Desktop/Github/CharacterNetwork/venv1/bin/activate
from FileManagement import *
# if line 4 and 5 have been executed, please comment it out
#import nltk
#nltk.download("popular")
from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktTrainer
import re

"""
To improve setence tokenization to complicated sentences in literature
This is consisted of three parts : preprocess, punkt training, and postprocess
"""

def textPreprocess(text:str) -> str:
    quote_regex = r'(".*?")'
    ps_regex = r'(\(.*?\))'
    text_preprocessed = re.sub(quote_regex,
                               lambda m: m.group(0).replace('.', '<dot>').replace('!', '<excl>').replace('?','<ques>'),
                                text,flags=re.DOTALL)

    # removing text in the parathesis
    text_preprocessed = re.sub(ps_regex,
                                "",
                                text_preprocessed,flags=re.DOTALL)
    #print(text_preprocessed)
    return text_preprocessed
def customPunkt(text_preprocessed:str):
    trainer = PunktTrainer()
    trainer.INCLUDE_ALL_COLLOCS = True
    trainer.train(text_preprocessed)
    return trainer
def textPostprocess(rowsent_list:list) -> list:
    sentences_list = [re.sub('<dot>','.',re.sub('<excl>','!',re.sub('<ques>','?',rowsent)))
                      for rowsent in rowsent_list]    
    return sentences_list
def sentTokenizer(text:str) -> list:
    text_preprocessed = textPreprocess(text)
    trainer = customPunkt(text_preprocessed)
    tokenizer = PunktSentenceTokenizer(trainer.get_params())
    rowsent_list = tokenizer.tokenize(text_preprocessed)
    sentences_list = textPostprocess(rowsent_list)
    return sentences_list
