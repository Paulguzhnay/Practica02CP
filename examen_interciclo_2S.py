
# generación de matrices
import numpy as np   

size_ = (10000,10000)
matriz1 = np.random.randint(10, size=size_).astype("float") / 100
matriz2 = np.random.randint(10, size=size_).astype("float") / 100



#print(matriz1[:10][:10])
#print(matriz2[:10][:10])

# suma de matrices secuencial
import time
inicio = time.time()
suma = np.zeros(dtype=float, shape=size_)
resta = np.zeros(dtype=float, shape=size_)

for i in range(len(matriz1)):
  for j in range(len(matriz1)):
    suma[i][j] = matriz1[i][j] + matriz2[i][j]
    resta[i][j] = matriz1[i][j] - matriz2[i][j]

fin = time.time()
print("El proceso de sumar y restar las matrices secuencialmente se ejecutó en %d segundos" % (fin - inicio))


