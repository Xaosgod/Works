

import gensim , logging
from gensim.models import word2vec
from gensim.models import Word2Vec
import wget
from gensim.models.phrases import Phrases, Phraser
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
def tag_ud(text):
 lines = text.split('\n')
 tagged = []
 for line in lines:
       line = line.lower()
       line=re.sub(r'\s+', ' ', line)
       line = re.sub('[^а-яА-Я]', ' ', line )
       tagged_line = line
       tagged.append(tagged_line)
 return '\n'.join(tagged)
 









def readInChunks(fileObj, chunkSize=52428800):
     while True:
        data = fileObj.read(chunkSize)
        if not data:
            break
        yield data
text = open('D:/work/info.txt', encoding='utf-8')
for chunk in readInChunks(text):
    processed_text = tag_ud(chunk)
    with open('D:/work/5.txt', 'a', encoding='utf-8') as out:
     out.write(processed_text)
    print(j)
    j=j+1

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
f = open('D:/work/5.txt',encoding='utf-8')
l=word2vec.LineSentence(f)
#print (f)
size=500
window=10
min_count=2
sg=0
model_path=None,
word_freq=None
corpus_count=None
model =Word2Vec(sentences=l,corpus_file=None, vector_size=500,alpha=0.025, window=10, min_count=2)
bigram = gensim.models.Phrases(l, min_count=1, threshold=10) # higher threshold fewer phrases.
trigram = gensim.models.Phrases(bigram[l], threshold=100) 
bigram.save('D:/work/my1.model')
trigram.save('D:/work/my2.model')
model.init_sims(replace=True)
#print(len(model.wv.key_to_index))
model.save('D:/work/my.model')
