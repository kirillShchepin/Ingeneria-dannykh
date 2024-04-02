import numpy as np
import json

matrix = np.load("Zadanie 2\\Nomer 1\\matrix_82.npy")
#print (matrix)
size = len(matrix)
#print (len(matrix))

itog1 = dict()
itog1['sum'] = 0
itog1['avr'] = 0
itog1['sumMD'] = 0
itog1['avrMD'] = 0
itog1['sumSD'] = 0
itog1['avrSD'] = 0
itog1['max'] = matrix[0][0]
itog1['min'] = matrix[0][0]

for i in range(0, size):
    for j in range(0, size):
        itog1['sum'] += matrix[i][j]
        if i==j:
            itog1['sumMD'] += matrix[i][j]
        if i+j ==size:
            itog1['sumSD'] += matrix[i][j]
        itog1['max'] = max(itog1['max'], matrix[i][j])
        itog1['min'] = min(itog1['min'], matrix[i][j])

itog1['avr'] = itog1['sum']/(size*size)
itog1['avrMD'] = itog1['sumMD']/size
itog1['avrSD'] = itog1['sumSD']/size

#print (itog1)

for key in itog1.keys():
    itog1[key] = float(itog1[key])

with open("Zadanie 2\\Nomer 1\\itog1.json", "w") as result:
    result.write(json.dumps(itog1))

norm_matrix = np.ndarray(shape=(size,size), dtype=float)

for i in range(0, size):
    for j in range(0, size):
        norm_matrix[i][j] = matrix[i][j]/itog1['sum']

#print (norm_matrix)

np.save(file="Zadanie 2\\Nomer 1\\norm_matrix", arr=norm_matrix)