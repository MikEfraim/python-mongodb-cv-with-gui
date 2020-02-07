from pymongo import MongoClient
from random import randint
import time
#$sudo mongod 

# def InitializeClient():
client = MongoClient() #will attempt to connect to local host
db=client.business
print('done initializing')

# a basic class for fetching random data
class SampleData:    
    def __init__(self):
        self.names = ['Kitchen','Animal','State', 'Tastey', 'Big','City','Fish', 'Pizza','Goat', 'Salty','Sandwich','Lazy', 'Fun']
        self.company_type = ['LLC','Inc','Company','Corporation']
        self.company_cuisine = ['Pizza', 'Bar Food', 'Fast Food', 'Italian','Mexican', 'American', 'Sushi Bar', 'Vegetarian']
    
    def PrintSampleData(self):
        print('Printing Sample Data:')
        print('names=',self.names)
        print('company_types=',self.company_type)
        print('company_cuisine=',self.company_cuisine)

    def GetRandomName(self):
        tmp_name=self.names[randint(0, (len(self.names)-1))]
        tmp_company_type=self.company_type[randint(0,(len(self.company_type)-1))]
        final_name=tmp_name+' '+tmp_company_type
        return final_name
    def GetRandomRating(self):
        return randint(1, 5)
    def GetRandomCuisine(self):
        tmp_company_cuisine=self.company_cuisine[randint(0,(len(self.company_cuisine)-1))]
        return tmp_company_cuisine

# A function for filling the database with random generated documents 
def InsertRandomDocuments(sampleTable: SampleData):
    businesses=100
    for x in range(0, businesses):
        tmp_business ={'name' : sampleTable.GetRandomName(),
            'rating' : sampleTable.GetRandomRating(),
            'cuisine' : sampleTable.GetRandomCuisine()
        }        
        #insert randomly generated document into the database in the reviews collection
        result=db.reviews_copy.insert_one(tmp_business)

        print('Created {0} of {1} as {2}'.format(x,businesses,result.inserted_id))

# def DeleteDocumentsFromCollection()
#     db.inventory.delete_many({})

#prints documents with X number of stars
def FindRatings(stars):
    for i in db.reviews.find({'rating': stars}):
        print(i)
    print('total found:',db.reviews.find({'rating': stars}).count())

if __name__=="__main__":
    # client,db=InitializeClient()
    print('client is:',client,'\n db is:',db)
    print('\n')
    # print(GetSampleData.names)
    sampleData=SampleData()
    time.sleep(0.5)
    FindRatings(4)
    # InsertRandomDocuments(sampleData)