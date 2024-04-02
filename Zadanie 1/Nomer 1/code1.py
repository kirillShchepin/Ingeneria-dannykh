with open("C:\\Users\\user\\Desktop\\Vagnoe\\Ucheba.Maga\\1 semestr\\Ingeneria dannykh\\Zadanie 1\\Nomer 1\\text_1_var_82.txt", encoding='utf-8') as file:
    l = file.read()
    #print(l) 
words = l.replace('\n', ' ').replace('.', ' ').replace(',', ' ').replace('!', ' ').replace('?', ' ').split()
#print(words)
slovarr = dict()
for slovo in words:
    if slovo in slovarr:
        slovarr[slovo] += 1
    else:
        slovarr[slovo] = 1

slovarr = (dict(sorted(slovarr.items(), reverse=True, key=lambda item: item[1])))
print(slovarr)

with open("C:\\Users\\user\\Desktop\\Vagnoe\\Ucheba.Maga\\1 semestr\\Ingeneria dannykh\\Zadanie 1\\Nomer 1\\itog1.txt", 'w') as itog1:
    for key, value in slovarr.items():
        itog1.write(key+":"+str(value)+"\n")