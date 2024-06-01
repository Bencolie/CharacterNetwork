# Use venv2
import spacy
# if line 4 and 5 have been executed, please comment it out
#import nltk
#nltk.download("popular")
from nltk.tokenize import PunktSentenceTokenizer
from spacy.tokens import Doc
from FileManagement import *

def CorefResolver(doc:Doc) -> str:
    reference_mapper = dict()
    result_text = ""
    clusters = [ val for key,val in doc.spans.items() if key.startswith("coref_cluster")]

    for cluster in clusters:
        reference = cluster[0]
        for pronoun in list(cluster)[1:]:
            reference_word = reference.text
            reference_mapper[pronoun[0].idx] = reference_word
            for token in pronoun[1:]:
                reference_mapper[token.idx] = ""
    for token in doc:
        if token.idx in reference_mapper:
            result_text += reference_mapper[token.idx] + token.whitespace_
        else:
            result_text += token.text + token.whitespace_
    return result_text

# load the English language model
# please pip install https://github.com/explosion/spacy-experimental/releases/download/v0.6.1/en_coreference_web_trf-3.4.0a2-py3-none-any.whl
nlp = spacy.load('en_coreference_web_trf')
for i in range (1,13): 
    datafile_name ='AliceInWonderland-ch'+str(i)
    text = readTextData(datafile_name)
    doc = nlp(text)
    result_text = CorefResolver(doc)
    #print(result_text)
    coreffile_name = 'AliceInWonderland-coref-ch'+str(i)
    writeText(coreffile_name,result_text)
