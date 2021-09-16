import bs4 as bs
import urllib.request
import re
import nltk
from gensim.models import Word2Vec
from nltk.corpus import stopwords



#word = "стали"
#p = morph.parse(word)[0]  # Делаем полный разбор, и берем первый вариант разбора (условно "самый вероятный", но не факт что правильный)
#print(p.normal_form)  # стать
#nltk.download('all')



#scrapped_data = urllib.request.urlopen('https://en.wikipedia.org/wiki/Artificial_intelligence')
scrapped_data = urllib.request.urlopen('https://ru.wikipedia.org/wiki/%D0%98%D1%81%D0%BA%D1%83%D1%81%D1%81%D1%82%D0%B2%D0%B5%D0%BD%D0%BD%D1%8B%D0%B9_%D0%B8%D0%BD%D1%82%D0%B5%D0%BB%D0%BB%D0%B5%D0%BA%D1%82')
article = scrapped_data .read()

parsed_article = bs.BeautifulSoup(article,'lxml')

paragraphs = parsed_article.find_all('p')

article_text = ""

for p in paragraphs:
    article_text += p.text

# Cleaing the text
processed_article = article_text.lower()
#processed_article = re.sub('[^a-zA-Z]', ' ', processed_article )
#processed_article = re.sub(r'\s+', ' ', processed_article)
processed_article = re.sub('[^а-яА-Я]', ' ', processed_article )
processed_article = re.sub(r'\s+', ' ', processed_article)


# Preparing the dataset
all_sentences = nltk.sent_tokenize(processed_article)
all_words = [nltk.word_tokenize(sent) for sent in all_sentences]

# Removing Stop Words
for i in range(len(all_words)):
 all_words[i] = [w for w in all_words[i] if w not in stopwords.words('russian')]


 

#print(stopwords.words('russian'))
#for i in range(len(all_words)):
# print ( all_words[i] )



#word2vec = Word2Vec(all_words, min_count=2)
word2vec = Word2Vec(all_words, min_count=2)
vocabulary = word2vec.wv.key_to_index
#print(vocabulary)
v1 = word2vec.wv['робот']
#print(v1)
sim_words = word2vec.wv.most_similar('человека')
print(sim_words)


