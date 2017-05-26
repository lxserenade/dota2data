from time import sleep
import cPickle as pickle
import requests
import datetime
import sys
from pymongo import MongoClient
import json
import logging
    

class Dota2Crawler(object):

    def __init__(self):
        # logging
        self.logger = logging.getLogger('dota2')
        self.logger.setLevel(logging.INFO)
        # create file handler which logs even debug messages
        fh = logging.FileHandler('../log/crawler.txt')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)
        # init mongo client
        self.client = MongoClient()

    def get_hero_stats(self):
        '''
            Get stats about hero performance in recent matches
        '''
        collection = self.client.Dota2.hero_stats
        query_url="https://api.opendota.com/api/heroStats"    
        response = requests.get(query_url)
        datas = json.loads(response.content)
        collection.remove()
        for data in datas:
            collection.insert(data)
            self.logger.info('Processed Hero ID: %s - Hero Name: %s' % (data['id'],data['localized_name']))
        print "get_hero_stats - done"    
    
    def match_crawler(self,start_id,end_id):
        for i in range(start_id,end_id):
            # sleep(1.0)
            self.get_match_by_id(i)

    def get_match_by_id(self,mid):
        '''
        Get Match data by match id
        '''
        try:
            collection = self.client.Dota2.matches
            query_url="https://api.opendota.com/api/matches/%s"    
            response = requests.get(query_url%(mid))
            data = json.loads(response.content)
            key = {'match_id':data['match_id']}
            collection.update(key,data,upsert=True)
            self.logger.info('Processed Match ID: %s' % (data['match_id']))
        except Exception,e:
            self.logger.error('Failed Match ID: %s' % (mid))
    
    def get_heroes(self):
        collection = self.client.Dota2.heroes
        query_url="https://api.opendota.com/api/heroes"    
        response = requests.get(query_url)
        datas = json.loads(response.content)
        collection.remove()
        for data in datas:
            collection.insert(data)
            self.logger.info('Processed Hero ID: %s - Hero Name: %s' % (data['id'],data['localized_name']))
        print "get_hero - done"    

    def get_publicMatches(self):
        pass

    def get_game_mode_string(self, game_mode_id):
        try:
            return game_mode_dict[int(game_mode_id)]
        except :
            return 'Unknown mode %s' % game_mode_id

    def getSkillLevel(self, match_id):
        ''' we query dotabuff to obtain the skill level of the match
            3: very high, 2: high, 1: normal, -1: unknown
        '''
        query_url = 'http://dotamax.com/match/detail/%s' % (match_id)
        response = requests.get(query_url)
        if '>Very High</font>' in response.content:
            return 3
        elif '>High</font>' in response.content:
            return 2
        elif '>Normal</font>' in response.content:
            return 1
        else:
            # unknown skill level
            return -1

if __name__ == '__main__':
    crawler = Dota2Crawler()
    # crawler.get_heroes()
    crawler.match_crawler(3199890122,3200070000) #3203325781