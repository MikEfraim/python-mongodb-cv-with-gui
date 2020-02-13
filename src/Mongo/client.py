from pymongo import MongoClient
from random import randint
from Mongo.sample_data import SampleData
from PyQt5 import Qt
from pathlib import Path
import time
import secrets

# to run the database type: sudo mongod

class Client():
    def __init__(self):
        super().__init__()
        self.ConnectToServer()
        print('client initialized successfully!')
    def ConnectToServer(self):
        # will attempt to connect to local host
        self.client = MongoClient("mongodb://localhost:27017/")
        # connect to database
        self.db = self.client["myDatabase"]
        print('self.db a= ', self.db, '\n')
        self.myCollection = self.db["users"]

    def InsertUser(self,
                   userName: str,
                   userDescription: str,
                   userImage: str):
        # attempt to create or connect to users collection

        aUser = {"image_id": self.GetRandomID(),
                 "name": userName,
                 "description": userDescription}
        # insert randomly generated document into the database in the reviews collection
        result = self.myCollection.insert_one(aUser)

    def FindUser(self,
                 userName: str):
        print('found the following users named:',userName,'\n')
        myList=list()
        for i in self.myCollection.find({'name': userName},{'_id':0,'description':1,'image_id':1}):
            myList.append(i)
        print('counted numbers in list=',len(myList))
        length=len(myList)
        for i in range(length):
            print(myList[i]['description'],'\n',myList[i]['image_id'])
    def FindAllUsers(self):
        print('found the following users')
        myList=list()
        for i in self.myCollection.find({'name': userName},{'_id':0,'description':1,'image_id':1}):
            myList.append(i)
        print('counted numbers in list=',len(myList))
    def DeleteAllUsers(self):
        self.myCollection.delete_many({})

    def GetRandomID(self):
        '''
        generate a secret id and return it
        '''
        return secrets.token_bytes(16)
if __name__ == "__main__":
    client = Client()
    client.DeleteAllUsers()
    time.sleep(0.5)
    client.InsertUser('John', 'this is my description:', 'image1')
    client.InsertUser('Jack', 'this is my description:', 'image2')
    client.InsertUser('Jason', 'this is my description:', 'image3')

    client.FindUser('John')
    client.FindAllUsers()

        # cursor = db.inventory.find(
        # {"status": "A"}, {"item": 1, "status": 1, "_id": 0})
        # for i in self.db.users.find({'name': userName},{'name':1,'_id':0,'description':1}):
        #     print(i)
        # print('testing:\n')