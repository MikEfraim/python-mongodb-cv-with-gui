from pymongo import MongoClient
from random import randint
# from Mongo.sample_data import SampleData
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
        print('db=\n', self.db, '\n')
        self.myCollection = self.db["users"]

    def InsertUser(self,
                   userName: str,
                   userDescription: str):
        aUser = {"name": userName,
                 "description": userDescription,
                 "image_id": self.GetRandomID()}
        # insert user into the database in the users collection
        result = self.myCollection.insert_one(aUser)

    def FindUser(self,
                 userName: str,
                 description: str):
        print('found the following users named:', userName)
        myList = list()

        for i in self.myCollection.find(
            {
                '$and': 
                [
                    {'name': userName}, {'description': description}
                ]
            }
        ):
            myList.append(i)
            print('added to the list: ', i)
        # for i in self.myCollection.find(
        #     {'name': userName, 'description': description}, {
        #         '_id': 0, 'description': 1, 'image_id': 1}
        # ):
            # myList.append(i)
        print('counted numbers in list=', len(myList))
        length = len(myList)
        for i in range(length):
            print(myList[i]['description'], '\n', myList[i]['image_id'])

    def FinderImageID(self, userName: str, description: str):
        print(__name__,' passing user= <',userName,'> description= <',description,'>\n')
        myList = list()
        for i in self.myCollection.find(
            {
                '$and': 
                [
                    {'name': userName}, {'description': description}
                ]
            },
            {'_id': 0, 'image_id': 1}
        ):
            myList.append(i)
            print('found user ',i)
        # if len(myList) > 0:
        print('image id= ', myList[0]['image_id'])
        value=myList[0]['image_id']
        return value

    def FindAllUsers(self):
        print('found the following users')
        myList = list()
        for i in self.myCollection.find({}, {'_id': 0, 'description': 1, 'image_id': 1}):
            myList.append(i)
        print('counted numbers in list=', len(myList))
        for i in range(len(myList)):
            print(myList[i])

    def DeleteAllUsers(self):
        self.myCollection.delete_many({})

    def DeleteUser(self, name: str, description: str):
        tmpQuery = {"name": name, "description": description}
        result = self.myCollection.delete_one(tmpQuery)
        # print('deleted user: ', result)

    def GetRandomID(self):
        '''
        generate a secret id and return it
        '''
        return secrets.token_hex(16)


if __name__ == "__main__":
    client = Client()
    
    client.InsertUser('John', 'this is my description1')
    client.InsertUser('Jack', 'this is my description2')
    client.InsertUser('Jason', 'this is my description3')
    client.InsertUser('Jason', 'this is my description3')

    # client.FindAllUsers()
    client.FindUser('asd', 'asdasd')
    tmp=client.FinderImageID('asd','asdasd')
    # client.FindAllUsers()
    client.DeleteAllUsers()
    time.sleep(0.5)
    # cursor = db.inventory.find(
    # {"status": "A"}, {"item": 1, "status": 1, "_id": 0})
    # for i in self.db.users.find({'name': userName},{'name':1,'_id':0,'description':1}):
    #     print(i)
    # print('testing:\n')
