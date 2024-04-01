import numpy as np 
import os

matrix = np.load("Zadanie 2\\Nomer 2\\matrix_82_2.npy")
#print (matrix)

size = len(matrix)

x = list()
y = list()
z = list()

lim = 582

for i in range(0, size):
    for j in range(0, size):
        if matrix[i][j] > lim:
            x.append(i)
            y.append(j)
            z.append(matrix[i][j])

np.savez(file="Zadanie 2\\Nomer 2\\itog2", x=x, y=y, z=z)
np.savez_compressed(file="Zadanie 2\\Nomer 2\\itog2_zip", x=x, y=y, z=z)

print(f"itog2 = {os.path.getsize('Zadanie 2\\Nomer 2\\itog2.npz')}")
print(f"itog2_zip = {os.path.getsize('Zadanie 2\\Nomer 2\\itog2_zip.npz')}")