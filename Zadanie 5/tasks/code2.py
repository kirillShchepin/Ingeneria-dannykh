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


for item in byte_data:
    collection.insert_one(item)

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
jobs = list(set(df['job']))

for item in jobs:
    print(len(list(collection.find({'job': item}))), 'записей с професией', item)

print('-------------------------------------------------')

#Задание 3

for item in cities:
    print(list(collection.find({'city': item}).sort({'salary': -1}).limit(1))[0]['salary'], 'макс. зарплата в городе', item)
    print(list(collection.find({'city': item}).sort({'salary': 1}).limit(1))[0]['salary'], 'мин. зарплата в городе', item)
    print('-------------------------------------------------')
for item in list(collection.aggregate([{'$group':{'_id': "$city",'avg': { '$avg': "$salary" }}}])):
    print(item['avg'], 'средняя зарплата в', item['_id'])
    print('-------------------------------------------------')
print('-------------------------------------------------')

# Задание 4


for item in jobs:
    print(list(collection.find({'job': item}).sort({'salary': -1}).limit(1))[0]['salary'], 'макс. зарплата у профессии', item)
    print(list(collection.find({'job': item}).sort({'salary': 1}).limit(1))[0]['salary'], 'мин. зарплата у профессии', item)
    print('-------------------------------------------------')
for item in list(collection.aggregate([{'$group':{'_id': "$job",'avg': { '$avg': "$salary" }}}])):
    print(item['avg'], 'средняя зарплата у профессии', item['_id'])
    print('-------------------------------------------------')
print('-------------------------------------------------')

# Задание 5
for item in cities:
    print(list(collection.find({'city': item}).sort({'age': -1}).limit(1))[0]['age'], 'макс. возраст в', item)
    print(list(collection.find({'city': item}).sort({'age': 1}).limit(1))[0]['age'], 'мин. возраст в', item)
    print('-------------------------------------------------')
for item in list(collection.aggregate([{'$group':{'_id': "$city",'avg': { '$avg': "$age" }}}])):
    print(item['avg'], 'средний возраст в', item['_id'])
    print('-------------------------------------------------')
print('-------------------------------------------------')

# Задание 6-7
for item in jobs:
    print(list(collection.find({'job': item}).sort({'age': -1}).limit(1))[0]['salary'], 'макс. зп у миниального возраста', item)
    print(list(collection.find({'job': item}).sort({'age': 1}).limit(1))[0]['salary'], 'мин. зп у максимального возраста', item)
    print('-------------------------------------------------')
print('-------------------------------------------------')

# Задание 8
for item in cities:
    print(list(collection.find({'city': item, 'salary': {"$gt": 50000}}).sort({'age': -1}).limit(1))[0]['age'], 'макс. возраст в городе', item)
    print(list(collection.find({'city': item, 'salary': {"$gt": 50000}}).sort({'age': 1}).limit(1))[0]['age'], 'мин. возраст в городе', item)
    summ = 0
    need_list = list(collection.find({'city': item, 'salary': {"$gt": 50000}}).sort({'age': 1}))
    for i in range(len(need_list)):
        summ += need_list[i]['age']
    summ /= (i + 1)
    print(summ, 'средний возраст в городе', item)
    print('-------------------------------------------------')
print('-------------------------------------------------')

# Задание 9

city = random.choice(cities)
job = random.choice(jobs)
try:
    print(list(collection.find({'city': city, 'job': job, "$and": [{'age': {'$in': list(range(19,25))} } , {'age': {'$in': list(range(51,65))}}]}).sort({'age': -1}).limit(1))[0]['salary'], 'макс. возраст в городе', city)
    print(list(collection.find({'city': city, 'job': job, "$and": [{'age': {'$in': list(range(19,25))} } , {'age': {'$in': list(range(51,65))}}] }).sort({'age': 1}).limit(1))[0]['salary'], 'мин. возраст в городе', city)
    summ = 0
    need_list = list(collection.find({'city': city, 'job': job, "$and": [{'age': {'$in': list(range(19,25))} } , {'age': {'$in': list(range(51,65))}}]}).sort({'age': 1}))
    for i in range(len(need_list)):
        summ += need_list[i]['salary']
    summ /= (i + 1)
    print(summ, 'средний возраст в городе', city)
except:
    print('Нет такой информации')
print('-------------------------------------------------')

# Задание 10
pprint(json.loads(json_util.dumps(list(collection.aggregate([ { '$match' : 
                                   { 'job' : "Инженер" }} 
                                ])))), indent = 2)
print(json.dumps(list(collection.aggregate([ { '$group' : 
                                   { '_id' : "$job",
                                    'avgSalary' : {'$avg': '$salary'} } } 
                                ])), ensure_ascii=False, indent = 2).encode('utf8').decode())