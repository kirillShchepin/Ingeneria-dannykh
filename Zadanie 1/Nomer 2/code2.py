with open("C:\\Users\\user\\Desktop\\Vagnoe\\Ucheba.Maga\\1 semestr\\Ingeneria dannykh\\Zadanie 1\\Nomer 2\\text_2_var_82.txt", encoding='utf-8') as file:
    lines = file.readlines()
#print(lines)
sum_lines = list()
for line in lines:
    nums = line.split()
    #print(nums)
    sum_line = 0
    for num in nums:
        sum_line += int(num)

    sum_lines.append(sum_line)

#print (sum_lines)

with open ("C:\\Users\\user\\Desktop\\Vagnoe\\Ucheba.Maga\\1 semestr\\Ingeneria dannykh\\Zadanie 1\\Nomer 2\\itog2.txt", 'w') as itog2:
    for value in sum_lines:
        itog2.write(str(value) + "\n")