import bs4 as bs
import urllib.request
import re
import nltk
from gensim.models import Word2Vec
from nltk.corpus import stopwords
import numpy as np
import json2
import xml.etree.ElementTree as ET

#word = "стали"
#p = morph.parse(word)[0]  # Делаем полный разбор, и берем первый вариант разбора (условно "самый вероятный", но не факт что правильный)
#print(p.normal_form)  # стать

#nltk.download('all')
#with open('D:/work/1.xml') as f:
   #for line in f:
    #   for p in paragraphs:
   # article_text += p.text
#for event, elem in ET.iterparse('D:/work/1.xml', events=("start","end")):

# words = {}
#for word in text.split(" "):
 #   words.setdefault(word,0)
 #   words[word]+=1
o1=1;


with open('D:/work/1.xml',) as f:
 for line in f:
  o1=sys.getsizeof(text1)
  if (o1<1073741824):
   article_text += line.text
  else:
   processed_article = article_text.lower()
   processed_article = re.sub('[^а-яА-Я]', ' ', processed_article ) 
   processed_article = re.sub(r'\s+', ' ', processed_article)
    # Preparing the dataset
   all_sentences = nltk.sent_tokenize(processed_article)
   all_words =[nltk.word_tokenize(sent) for sent in all_sentences]
   for i in range(len(all_words)):
    all_words[i] = [w for w in all_words[i] if w not in stopwords.words('russian')]
   all_words_all[j] = all_words[0]
   j=j+1
   article_text=[]   

x=2
all_words_all = []

url = []
for i in [0,x-1]:
  all_words_all = all_words_all + [i]
  url = url + [i]
print (all_words_all)
url[0] = 'https://ru.wikipedia.org/wiki/%D0%98%D1%81%D0%BA%D1%83%D1%81%D1%81%D1%82%D0%B2%D0%B5%D0%BD%D0%BD%D1%8B%D0%B9_%D0%B8%D0%BD%D1%82%D0%B5%D0%BB%D0%BB%D0%B5%D0%BA%D1%82'
url[1] = 'https://ru.wikipedia.org/wiki/%D0%91%D0%BE%D0%BB%D1%8C%D1%88%D0%BE%D0%B9_%D0%B0%D0%B4%D1%80%D0%BE%D0%BD%D0%BD%D1%8B%D0%B9_%D0%BA%D0%BE%D0%BB%D0%BB%D0%B0%D0%B9%D0%B4%D0%B5%D1%80'



for j in [0,1]:
 scrapped_data = urllib.request.urlopen(url[j])

 article = scrapped_data .read()


 parsed_article = bs.BeautifulSoup(article,'lxml')

 paragraphs = parsed_article.find_all('p')

 article_text = ""
 for p in paragraphs:
    article_text += p.text

# Cleaing the text
 processed_article = article_text.lower()
 processed_article = re.sub('[^а-яА-Я]', ' ', processed_article ) 
 processed_article = re.sub(r'\s+', ' ', processed_article)

# Preparing the dataset
 all_sentences = nltk.sent_tokenize(processed_article)
 all_words =[nltk.word_tokenize(sent) for sent in all_sentences]

# Removing Stop Words
 for i in range(len(all_words)):
  all_words[i] = [w for w in all_words[i] if w not in stopwords.words('russian')]

 all_words_all[j] = all_words[0]

word2vec = Word2Vec(all_words_all, min_count=2)
vocabulary = word2vec.wv.key_to_index

#print(vocabulary)


#a_file = open("D:/pyton/тест/test.json","w")
#json2.dump(vocabulary, a_file)
#a_file.close()
#v1 = word2vec.wv['робот']
#print(v1)
#sim_words = word2vec.wv.most_similar('человека')
#print(sim_words)
#self.wdict = {}
#for i, k in enumerate(all_words):
		#	for d in self.wdict[k]:
			#	all_words[i,d] += 1

#self.A = zeros([len(all_words), len(1)])

#for i in range(len(all_words)):
# u[i],l[i],m[i]= np.linalg.svd(all_words[0][i])

#wx, wy = (-1 * self.U[:, 1:3])[idx]
 