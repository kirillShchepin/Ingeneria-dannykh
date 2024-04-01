import csv

srednii_dohod = 0
items = list()

with open ("C:\\Users\\user\\Desktop\\Vagnoe\\Ucheba.Maga\\1 semestr\\Ingeneria dannykh\\Zadanie 1\\Nomer 4\\text_4_var_82.csv", newline='\n', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter=",")

    for row in reader:
        item = {
            'number':int(row[0]),
            'name':row[2] + ' ' + row[1],
            'age':int(row[3]),
            'dohod':int(row[4][0:-1])
        }
#print(item)
        srednii_dohod += item['dohod']
        items.append(item)
#print(items)
srednii_dohod /= len(items)
#print(srednii_dohod)

itog = list()
for item in items:
    if (item['dohod'] > srednii_dohod) and item['age'] > 25+8:
        itog.append(item)
#print(itog)
itog = sorted (itog, key=lambda i: i['number'])
#print(itog)

with open ("C:\\Users\\user\\Desktop\\Vagnoe\\Ucheba.Maga\\1 semestr\\Ingeneria dannykh\\Zadanie 1\\Nomer 4\\itog4.csv", 'w', encoding = "utf-8", newline = '') as itog4:
    writer = csv.writer(itog4, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL) 
    for item in itog:
        writer.writerow(item.values())
