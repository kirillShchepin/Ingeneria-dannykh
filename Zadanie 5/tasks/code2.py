from pymongo import MongoClient
import json
import pandas as pd
import json
from bson import json_util
from pprint import pprint
import random
import pandas as pd
import msgpack

client = MongoClient("mongodb://localhost:27017/")

client.list_database_names()

db = client['admin']
collection = db['kirill']

with open("task_2_item_msgpack.msgpack", "rb") as data_file:
    byte_data = data_file.read()
byte_data = msgpack.unpackb(byte_data)


# for item in byte_data:
#     collection.insert_one(item)

# Задание 1
print(list(collection.find().sort({'salary': -1}).limit(1))[0]['salary'], 'max')
print(list(collection.find().sort({'salary': 1}).limit(1))[0]['salary'], 'min')
print(list(collection.aggregate([{
    '$group': {
        '_id': 'city',
        'avg': {'$avg': '$salary'}
    }}]))[0]['avg'], 'avg')

print('-------------------------------------------------')

# Задание 2

df = pd.DataFrame(collection.find({}, {'city': 1, 'job': 1}))
cities = list(set(df['city']))

for item in cities:
    print(len(list(collection.find({'city': item}))), 'записей с городом', item)

print('-------------------------------------------------')

# Задание 3

for item in cities:
    print(list(collection.find({'city': item}).sort({'salary': -1}).limit(1))[0]['salary'], 'макс. зарплата в городе', item)
    print(list(collection.find({'city': item}).sort({'salary': 1}).limit(1))[0]['salary'], 'мин. зарплата в городе', item)
for item in list(collection.aggregate([{'$group':{'_id': "$city",'avg': { '$avg': "$salary" }}}])):
    print(item['avg'], 'средняя зарплата в', item['_id'])
print('-------------------------------------------------')

# Задание 4
jobs = list(set(df['job']))

for item in jobs:
    print(list(collection.find({'job': item}).sort({'salary': -1}).limit(1))[0]['salary'], 'макс. зарплата у профессии', item)
    print(list(collection.find({'job': item}).sort({'salary': 1}).limit(1))[0]['salary'], 'мин. зарплата у профессии', item)
for item in list(collection.aggregate([{'$group':{'_id': "$job",'avg': { '$avg': "$salary" }}}])):
    print(item['avg'], 'средняя зарплата у профессии', item['_id'])
print('-------------------------------------------------')

# Задание 5
for item in jobs:
    print(list(collection.find({'job': item}).sort({'age': -1}).limit(1))[0]['age'], 'макс. возраст у', item)
    print(list(collection.find({'job': item}).sort({'age': 1}).limit(1))[0]['age'], 'мин. возраст у', item)
for item in list(collection.aggregate([{'$group':{'_id': "$job",'avg': { '$avg': "$age" }}}])):
    print(item['avg'], 'средний возраст у', item['_id'])
print('-------------------------------------------------')

# Задание 6-7
for item in jobs:
    print(list(collection.find({'job': item}).sort({'age': -1}).limit(1))[0]['salary'], 'макс. зп у миниального возраста', item)
    print(list(collection.find({'job': item}).sort({'age': 1}).limit(1))[0]['salary'], 'мин. зп у максимального возраста', item)
print('-------------------------------------------------')