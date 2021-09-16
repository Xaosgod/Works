import bs4 as bs
import urllib.request
import re
import nltk
from gensim.models import Word2Vec
from nltk.corpus import stopwords
import numpy as np
import json2
import xml.etree.ElementTree as ET
import sys
import pickle
import requests
import wget
import gensim , logging
from gensim.models import Word2Vec
from ufal.udpipe import Model, Pipeline
import os
import re
import pipeline
import sys
j=0
modelfile = 'D:/work/udpipe_syntagrus.model'
def process(pipeline, text='Строка', keep_pos=False, keep_punct=False):
    entities = {'PROPN'}
    named = False
    memory = []
    mem_case = None
    mem_number = None
    tagged_propn = []

    # обрабатываем текст, получаем результат в формате conllu:
    processed = pipeline.process(text)

    # пропускаем строки со служебной информацией:
    content = [l for l in processed.split('\n') if not l.startswith('#')]

    # извлекаем из обработанного текста леммы, тэги и морфологические характеристики
    tagged = [w.split('\t') for w in content if w]

    for t in tagged:
        if len(t) != 10:
            continue
        (word_id, token, lemma, pos, xpos, feats, head, deprel, deps, misc) = t
        if not lemma or not token:
            continue
        if pos in entities:
            if '|' not in feats:
                tagged_propn.append('%s_%s' % (lemma, pos))
                continue
            morph = {el.split('=')[0]: el.split('=')[1] for el in feats.split('|')}
            if 'Case' not in morph or 'Number' not in morph:
                tagged_propn.append('%s_%s' % (lemma, pos))
                continue
            if not named:
                named = True
                mem_case = morph['Case']
                mem_number = morph['Number']
            if morph['Case'] == mem_case and morph['Number'] == mem_number:
                memory.append(lemma)
                if 'SpacesAfter=\\n' in misc or 'SpacesAfter=\s\\n' in misc:
                    named = False
                    past_lemma = '::'.join(memory)
                    memory = []
                    tagged_propn.append(past_lemma + '_PROPN ')
            else:
                named = False
                past_lemma = '::'.join(memory)
                memory = []
                tagged_propn.append(past_lemma + '_PROPN ')
                tagged_propn.append('%s_%s' % (lemma, pos))
        else:
           
                named = False
                past_lemma = '::'.join(memory)
                memory = []
                tagged_propn.append(past_lemma + '_PROPN ')
                tagged_propn.append('%s_%s' % (lemma, pos))

    if not keep_punct:
        tagged_propn = [word for word in tagged_propn if word.split('_')[1] != 'PUNCT']
    if not keep_pos:
        tagged_propn = [word.split('_')[0] for word in tagged_propn]
    return tagged_propn
def tag_ud(text, modelfile):
   model = Model.load(modelfile)
   process_pipeline = Pipeline(model, 'tokenize', Pipeline.DEFAULT, Pipeline.DEFAULT, 'conllu')
   lines = text.split('\n')
   tagged = []
   for line in lines:
       line = line.lower()
       line=re.sub(r'\s+', ' ', line)
       line = re.sub('[^а-яА-Я]', ' ', line )
       output = process(process_pipeline, text=line)
       tagged_line = ' '.join(output)
       tagged.append(tagged_line)
   return '\n'.join(tagged)

def readInChunks(fileObj, chunkSize=20480000):
     while True:
        data = fileObj.read(chunkSize)
        if not data:
            break
        yield data
text = open('D:/work/info.txt', encoding='utf-8')
for chunk in readInChunks(text):
    processed_text = tag_ud(chunk,modelfile)
    with open('D:/work/5.txt', 'w+', encoding='utf-8') as out:
     out.write(processed_text)
     print(j)
     j=j+1

#text = open('D:/work/2.txt', 'r', encoding='utf-8').read()
#processed_text = tag_ud(text,modelfile)
#print(processed_text[:350])
#with open('D:/work/5.txt', 'w', encoding='utf-8') as out:
  # out.write(processed_text)

import gensim , logging
from gensim.models import word2vec
from gensim.models import Word2Vec
import wget
from gensim.models.phrases import Phrases, Phraser

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
f = open('D:/work/5.txt',encoding='utf-8')

#data = gensim.models.word2vec.LineSentence(f)
#article_text = ""

#for p in f:
 #   article_text += p.text
#processed_article = article_text.lower()
#processed_article=re.sub(r'\s+', ' ', processed_article)
l=word2vec.LineSentence(f)
#print (f)
size=500
window=10
min_count=2
sg=0
model_path=None,
word_freq=None
corpus_count=None
model =Word2Vec(sentences=l,corpus_file=None, vector_size=500,alpha=0.025, window=10, min_count=1)
bigram = gensim.models.Phrases(l, min_count=1, threshold=10) # higher threshold fewer phrases.
trigram = gensim.models.Phrases(bigram[l], threshold=100) 
bigram.save('D:/work/my1.model')
trigram.save('D:/work/my2.model')
model.init_sims(replace=True)
#print(len(model.wv.key_to_index))
model.save('D:/work/my.model')
bigram1 =Phraser(bigram)
#words = 'день_NOUN', 'ночь_NOUN', 'человек_NOUN', 'семантика_NOUN', 'студент_NOUN', 'студент_ADJ'
#sim_words = bigram.wv.most_similar('файл',topn=10)
#print (trigram.vocab)
#print(trigram)