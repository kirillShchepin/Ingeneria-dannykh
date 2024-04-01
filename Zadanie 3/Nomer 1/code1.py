import os
import re
import statistics
import json
from bs4 import BeautifulSoup


def file_read(file_name):
    with open(file_name, encoding='utf-8') as f:
        str_html = ''
        lines = f.readlines()
        for line in lines:
            str_html += line
    
        soup = BeautifulSoup(str_html, 'html.parser')
#         print(soup)

        item = {}
        item['type'] = soup.find('span').text.split(':')[1].strip()
#         print(item['type'])
        item['name'] = soup.find('h1').text.strip()
#         print(item['tur'])
        item['author'] = soup.find('p', class_='author-p').text.strip()
#         print(item['author'])
        item['pages'] = int(soup.find('span', class_='pages').text.strip().split()[1])
#         print(item['pages'])
        item['year'] = int(soup.find('span', class_='year').text.strip().split()[2])
#         print(item['year'])
        item['ISBN'] = soup.find_all('span')[3].text.split(':')[1].strip()
#         print(item['ISBN'])
        item['description'] = soup.find_all('p')[1].text.split('Описание')[1].strip()
#         print(item['description'])
        item['rating'] = float(soup.find_all('span')[4].text.split(':')[1].strip())
#         print(item['rating'])
        item['views'] = int(soup.find_all('span')[5].text.split(':')[1].strip())
#         print(item['views'])
        
        return item


max_file = 1000


items = []


for i in range(1, max_file):
    temp = file_read(f'.\\Zadanie 3\\Nomer 1\\task1_var82\\{i}.html')
    items.append(temp)

items = sorted(items, key=lambda x: x['rating'], reverse=True)


with open(".\\Zadanie 3\\Nomer 1\\itog_items.json", 'w', encoding='utf-8') as f:
    f.write(json.dumps(items, ensure_ascii=False, indent=2))

filter_views = []
for olimp in items:
    if olimp['views'] >= 50000:
        filter_views.append(olimp)

with open(".\\Zadanie 3\\Nomer 1\\itog_filter.json", 'w', encoding='utf-8') as f:
    f.write(json.dumps(filter_views, ensure_ascii=False, indent=2))


all_views = []
all_ratings = []
all_years = []
all_pages = []


for i in range(len(items)):
    all_views.append(items[i]['views'])
    all_ratings.append(items[i]['rating'])
    all_years.append(items[i]['year'])
    all_pages.append(items[i]['pages'])
    
count = {}

count['avg_views'] = int(sum(all_views)/len(all_views))
count['avg_ratings'] = round(sum(all_ratings)/len(all_ratings), 2)
count['avg_pages'] = int(sum(all_pages)/len(all_pages))
count['max_year'] = max(all_years)
count['min_pages'] = min(all_pages)

with open(".\\Zadanie 3\\Nomer 1\\itog.json", 'w', encoding='utf-8') as f:
    f.write(json.dumps(count, ensure_ascii=False, indent=2))