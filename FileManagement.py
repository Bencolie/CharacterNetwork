import os

# input the text file
def readTextData(file_name):
    # adapt different directory structure
    file_path = os.path.abspath(f"TextData/{file_name}.txt")
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text
def readTextCoref(file_name):
    # adapt different directory structure
    file_path = os.path.abspath(f"CorefText/{file_name}.txt")
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text
# out put the text file
def writeText(file_name:str,result_text:str):
    file_path = os.path.abspath(f"CorefText/{file_name}.txt")
    try:
        open(file_path, 'r', encoding='utf-8')
        print(f'File : {file_name} is already exist!')
    except IOError:
        f = open(file_path, "a", encoding='utf-8')
        f.write(result_text)
        f.close()