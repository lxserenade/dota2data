from pymongo import MongoClient
class Hero():

    def __init__(self):
    	client = MongoClient()
    	self.matchcollection = client.Dota2.matches
    	self.herocollection = client.Dota2.heroes

    def getHeroById(self,hid):
    	return self.herocollection.find_one({"id":hid})



