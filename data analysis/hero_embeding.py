import gensim
import numpy as np
from models.match import Match
from pymongo import MongoClient
from gensim.models import Word2Vec
from gensim.models.word2vec import Word2Vec, LineSentence
from util import heroes

heroIdName_dict={}

def loadHeroDict():
    client = MongoClient()
    hero_col = client.Dota2.heroes
    heroes = hero_col.find()
    for hero in heroes:
        heroIdName_dict[hero['id']]=hero['name']
    print 'load hero dict done.'
    return heroIdName_dict

def getHeroSentenceFromMatch(match):
    players = match['players']
    hero_sentence = ' '.join([ heroIdName_dict[player['hero_id']] for player in players])
    return hero_sentence

def dataPreProcessing():
    M = Match()
    matches = M.getAllMatches()
    with open('./data/matchTeamSentences.txt','w') as f:
        for match in matches:
            try:
                f.write(getHeroSentenceFromMatch(match))
            except:
                print match['match_id']
                continue

def train():
    sentences = LineSentence('./data/matchTeamSentences.txt')
    model = Word2Vec(sentences,size=200,window=5,min_count=0)
    model.save('./result/matchTeamEmbeding')
    return model

def LocallizedHeroName(name):
    pass

if __name__=='__main__':
    # model = train()
    model = Word2Vec.load('./result/matchTeamEmbeding') 
    heroes = model.most_similar('npc_dota_hero_invoker',topn=113)
    for hero in heroes:
        print hero
