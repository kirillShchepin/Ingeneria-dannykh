import requests
import json
import json2table


api = 'https://www.boredapi.com/api/activity'
itog = requests.get(api)
JI = json.loads(itog.text)
LtR = "LEFT_TO_RIGHT"
attributes = {"style": "background-color:red; border: 4px solid; padding: 4px"}

itog5 = open("C:\\Users\\user\\Desktop\\Vagnoe\\Ucheba.Maga\\1 semestr\\Ingeneria dannykh\\Zadanie 1\\Nomer 6\\itpg5.html", 'w')
itog5.write(json2table.convert(JI, build_direction = LtR, table_attributes=attributes))
itog5.close()
