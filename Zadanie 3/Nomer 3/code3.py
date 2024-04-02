import os
import re
import statistics
import json
from bs4 import BeautifulSoup

def file_read(file_name):
    with open(file_name, encoding='utf-8') as f:
        str_xml = ''
        lines = f.readlines()
        for line in lines:
            str_xml += line
    
        soup = BeautifulSoup(str_xml, 'xml')
        item = {}
        item['name'] = soup.find_all('name')[0].get_text().strip()
        item['const'] = soup.find_all('constellation')[0].get_text().strip()
        item['class'] = soup.find_all('spectral-class')[0].get_text().strip()
        item['radius'] = int(soup.find_all('radius')[0].get_text().strip())
        item['rotation'] = soup.find_all('rotation')[0].get_text().strip()
        item['age'] = soup.find_all('age')[0].get_text().strip()
        item['distance'] = soup.find_all('distance')[0].get_text().strip()
        item['magn'] = soup.find_all('absolute-magnitude')[0].get_text().strip()

        return item


max_file = 501
items = []
for i in range(1, max_file):
    temp = file_read(f'.\\Zadanie 3\\Nomer 3\\task3_var82\\{i}.xml')
    items.append(temp)

items = sorted(items, key=lambda x: x['name'])

with open(".\\Zadanie 3\\Nomer 3\\itog_sort.json", 'w', encoding='utf-8') as f:
    f.write(json.dumps(items, ensure_ascii=False, indent=2))

filter_views = []
for star in items:
    if star['const'] == 'Дева':
        filter_views.append(star)

with open(".\\Zadanie 3\\Nomer 3\\itog_filter.json", 'w', encoding='utf-8') as f:
    f.write(json.dumps(filter_views, ensure_ascii=False, indent=2))

all_radius = {}
zz = {}
all_radius['sum_radius'] = 0
all_radius['min_radius'] = 10 ** 9 + 1
all_radius['max_radius'] = 0
std_radius = [0]
for star in items:
    temp = star['radius']
    all_radius['sum_radius'] += temp
    if all_radius['min_radius'] > temp:
        all_radius['min_radius'] = temp
    if all_radius['max_radius'] < temp:
        all_radius['max_radius'] = temp
    std_radius.append(temp)
    if star['const'] in zz:
        zz[star['const']] += 1
    else:
        zz[star['const']] = 1
all_radius['avr_radius'] = all_radius['sum_radius'] / len(items)
all_radius['std_radius'] = statistics.stdev(std_radius)

all_res = [all_radius, zz]

with open(".\\Zadanie 3\\Nomer 3\\itog_charact.json", 'w', encoding='utf-8') as f:
   f.write(json.dumps(all_res, ensure_ascii=False, indent=2))