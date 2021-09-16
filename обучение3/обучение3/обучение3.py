
















def get_sentences(input_file_pointer):
    while True:
        line = input_file_pointer.readline()
        if not line:
            break

import re
def clean_sentence(sentence):
    sentence = sentence.lower().strip()
    sentence = re.sub('[^а-я0-9\s]', ' ', sentence ) 
    return re.sub(r'\s{2,}', ' ', sentence)
from spacy.lang.ru.stop_words import STOP_WORDS

def tokenize(sentence):
  return [token for token in sentence.split() if token not in STOP_WORDS]

from gensim.models.phrases import Phrases, Phraser

def build_phrases(sentences):
    phrases = Phrases(sentences,
                      min_count=5,
                      threshold=7,
                      progress_per=1000)
    phrases.save('D:/work/phrases_model.txt')
    phrases= Phraser.load('D:/work/phrases_model.txt')
    return Phraser(phrases)



def sentence_to_bi_grams(phrases_model, sentence):
    return ' '.join(phrases_model[sentence])

def sentences_to_bi_grams(n_grams, input_file_name, output_file_name):
    with open(input_file_name, 'r',encoding='utf-8') as input_file_pointer:
        with open(output_file_name, 'w+',encoding='utf-8') as out_file:
            for sentence in get_sentences(input_file_pointer):
                cleaned_sentence = clean_sentence(sentence)
                tokenized_sentence = tokenize(cleaned_sentence)

                parsed_sentence = build_phrases(tokenized_sentence)
                out_file.write(parsed_sentence + '\n')


a= 'D:/work/2.txt'
b= 'D:/work/6.txt'
c='D:/work/phrases_model.txt'
sentences_to_bi_grams(c,a,b)
#phrases_model.save('D:/work/phrases_model.txt')
#phrases_model= Phraser.load('D:/work/phrases_model.txt')