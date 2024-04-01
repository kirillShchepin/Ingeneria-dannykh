import json
import msgpack
import os

with open ("Zadanie 2\\Nomer 3\\products_82.json") as f:
    data = json.load(f)
    #print (data)

    info = dict()

    for item in data:
        if item['name'] in info:
            info[item['name']].append(item['price'])
        else:
            info[item['name']] = list()
            info[item['name']].append(item['price'])
        
    #print (info)
    
    itog = list()
    
    for name, prices in info.items():
        sum_price = 0
        max_price = prices[0]
        min_price = prices[0]
        size = len(prices)
        for price in prices:
            sum_price += price
            max_price = max(max_price, price)
            main_price = min(min_price, price)

        itog.append({
            "name": name,
            "max": max_price,
            "min": min_price,
            "avr": sum_price / size
        })
    #print (itog)

    with open ("Zadanie 2\\Nomer 3\\itog3_info.json", "w") as i_json:
        i_json.write(json.dumps(itog))

    with open ("Zadanie 2\\Nomer 3\\itog3_info.msgpack", "wb") as i_msgpack:
        i_msgpack.write(msgpack.dumps(itog))

print(f"itog3_info.json = {os.path.getsize('Zadanie 2\\Nomer 3\\itog3_info.json')}")
print(f"itog2_info.msgpack = {os.path.getsize('Zadanie 2\\Nomer 3\\itog3_info.msgpack')}")