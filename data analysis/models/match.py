from pymongo import MongoClient
class Match():

    def __init__(self):
    	client = MongoClient()
    	self.matchcollection = client.Dota2.matches
    	self.herocollection = client.Dota2.heroes
    	
    def getAllMatches(self,filter_dict = {}):
    	return self.matchcollection.find(filter_dict)

    def getMatchById(self,mid):
    	return self.matchcollection.find_one({'match_id': mid})

    def getHeroById(self,hid):
    	return self.herocollection.find_one({"id":hid})

    def getMatchHeroTeam(self,mid):
        return self.getMatchById(mid)['players']

    def printMatchHeroTeam(self):
    	players = self.getMatchHeroTeam()
        radiant_Team = [self.getHeroById(player['hero_id'])['localized_name']
                         for player in players if player['isRadiant']]
        dire_Team = [self.getHeroById(player['hero_id'])['localized_name']
                      for player in players if not player['isRadiant']]
        print "radiant Team:",
        print ",".join(radiant_group)
        print "dire Team:",
        print ",".join(dire_group)

    def findMacthByAccountId(aid):
        return self.matchcollection.find({"players":{"$elemMatch":{"account_id":aid}}})