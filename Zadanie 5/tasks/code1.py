from pymongo import MongoClient
import json
import pandas as pd
import json
from bson import json_util
from pprint import pprint
import random
import pandas as pd

client = MongoClient("mongodb://localhost:27017/")

client.list_database_names()

db = client['admin']
collection = db['kirill']

info = {}

with open('.\\Zadanie 5\\data\\task_1_item.text', 'r', encoding="utf-8") as file:
    lines = file.readlines()
    for i in range(len(lines)):
        if (i + 1) % 7 == 0:
            collection.insert_one(info)
            info = {}
            continue
        try:
            info[lines[i].split('::')[0]] = int(lines[i].split('::')[1].strip())
        except:
            info[lines[i].split('::')[0]] = lines[i].split('::')[1].strip()
        
# Вывод для первого задания  
for item in list(collection.find().sort({'salary': -1}))[0:10]:
    pprint(json.loads(json_util.dumps(item)), indent = 2)
print('-------------------------------------------------')


# Вывод для второго задания  
for item in list(collection.find({'age': {"$lt": 30}}).sort({'salary': -1}))[0:15]:
    pprint(json.loads(json_util.dumps(item)), indent = 2)
print('-------------------------------------------------')

# Вывод для третьего задания 
df = pd.DataFrame(collection.find({}, {'city': 1, 'job': 1}))
city = random.choice(list(set(df['city'])))

jobs = []
for i in range(3):
    jobs.append(random.choice(list(set(df['job']))))

query = {'city': city, 'job': {"$in": jobs}}
for item in list(collection.find(query).sort({'age': 1}))[0:10]:
    pprint(json.loads(json_util.dumps(item)), indent = 2)
print('-------------------------------------------------')

# Вывод для четвертого задания 

age = list(range(random.randint(1, 20), random.randint(21, 90)))

query = { "$or": [{'salary': {'$in': list(range(50001,75001))} } , {'salary': {'$in': list(range(125001,150001))}}], 'year ': {'$in': list(range(2019,2023))}, 'age': {"$in": age}}
print(len(list(collection.find(query))))
print('-------------------------------------------------')