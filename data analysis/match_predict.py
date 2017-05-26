from models.match import Match
from pymongo import MongoClient
from gensim.models import Word2Vec
from gensim.models.word2vec import Word2Vec, LineSentence
import numpy as np
from sklearn.neighbors import NearestNeighbors

from hero_embeding import loadHeroDict

client = MongoClient()
def dataPrepeocess():
	matches = client.Dota2.matches
	m = matches.find_one()
	players = m['players']


heroIdName_dict = loadHeroDict()

model = Word2Vec.load('./result/matchTeamEmbeding')
word_vectors = model.wv
del model
word_vectors.save('./result/hero_vector')

x=[]
for k,v in heroIdName_dict.iteritems():
	x.append(word_vectors[v])

x= np.array(x)

nbrs = NearestNeighbors(n_neighbors=3, algorithm='ball_tree').fit(x)
distances, indices = nbrs.kneighbors(x)
for one in indices:
	if 23 in one or 107 in one :
		continue
	print [heroIdName_dict[x+1] for x in one]
	