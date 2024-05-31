# Use venv2
import spacy,os
# if line 4 and 5 have been executed, please comment it out
#import nltk
#nltk.download("popular")
from nltk.tokenize import PunktSentenceTokenizer
from spacy.tokens import Doc

def readText(file_name:str) -> str:
    # adapt different directory structure
    file_path = os.path.abspath(f"CorefText/{file_name}.txt")
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

def writeText(file_name:str,result_text:str):
    file_path = os.path.abspath(f"CorefText/{file_name}.txt")
    try:
        open(file_path, 'r', encoding='utf-8')
        print(f'File : {file_name} is already exist!')
    except IOError:
        f = open(file_path, "a", encoding='utf-8')
        f.write(result_text)
        f.close()

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
text = readText('AliceInWonderland-ch1')
doc = nlp(text)
result_text = CorefResolver(doc)
writeText('AliceInWonderland-ch1-coref',result_text)
