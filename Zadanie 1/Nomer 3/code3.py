with open ("C:\\Users\\user\\Desktop\\Vagnoe\\Ucheba.Maga\\1 semestr\\Ingeneria dannykh\\Zadanie 1\\Nomer 3\\text_3_var_82.txt", encoding = 'utf-8') as file:
    l = file.readlines()
itog3 = open("C:\\Users\\user\\Desktop\\Vagnoe\\Ucheba.Maga\\1 semestr\\Ingeneria dannykh\\Zadanie 1\\Nomer 3\\itog3.txt", 'w')
for line in l:
    nums = line.strip().split(",")
    itog = ''
    for (index, item) in enumerate(nums):
        if item == 'NA':
            nums[index] = int((int(nums[index-1]) + int(nums[index+1]))/2)
        if int(int(nums[index])**0.5) > 50+82:
            itog += str(nums[index]) + ' '
    #print(itog)
    itog3.write(itog + '\n')
itog3.close

