import gensim , logging
from gensim.models import word2vec
from gensim.models import Word2Vec
import wget

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
f = open('D:/work/5.txt','r')
#data = gensim.models.word2vec.LineSentence(f)
l=word2vec.LineSentence(f)
print (f)
size=500
window=10
min_count=2
sg=0
model_path=None,
word_freq=None
corpus_count=None
corpus_file='D:/work/my.model'
#model =Word2Vec(sentences=l,corpus_file=None, vector_size=500,alpha=0.025, window=10, min_count=1)

#model.init_sims(replace=True)
#print(len(model.wv.key_to_index))
#model.save('D:/work/my.model')
model = word2vec.Word2Vec.load('D:/work/my.model')
#words = 'день_NOUN', 'ночь_NOUN', 'человек_NOUN', 'семантика_NOUN', 'студент_NOUN', 'студент_ADJ'
sim_words = model.wv.most_similar(' дымовой_ADJ ',topn=10)
print (sim_words)
