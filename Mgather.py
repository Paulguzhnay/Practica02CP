from turtle import shape
from mpi4py import MPI
import numpy as np
size_ = (10000,10000)

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

matriz1 = np.random.randint(10, size=size_).astype("float") / 100
'''
print("--------------------MATRIZ 1------------------------------------")
print(matriz1)
print("***********************************************************")
'''
subMatriz1 = np.vsplit(matriz1,4)

P1=subMatriz1[0]
P2=subMatriz1[1]
P3=subMatriz1[2]
P4=subMatriz1[3]

sizeM=np.shape(P1)
P1=comm.gather(P1, root=0)
P2=comm.gather(P2, root=0)
P3=comm.gather(P3, root=0)
P4=comm.gather(P4, root=0)
#print("---")


if rank==0:
   '''
   print("rank 0")
   print(sizeM)

   print("submatriz1-1")
   print(P1[0])
   print("submatriz1-2")
   print(P1[1])

   print("-------")
   print(np.shape(P1))
   print(np.shape(P1)[1])
   print(np.shape(P1)[2])
   print("----------------")
   '''


   suma1 = np.zeros(dtype=float, shape=sizeM)
   suma2 = np.zeros(dtype=float, shape=sizeM)
   suma3 = np.zeros(dtype=float, shape=sizeM)
   suma4 = np.zeros(dtype=float, shape=sizeM)

   resta1 = np.zeros(dtype=float, shape=sizeM) 
   resta2 = np.zeros(dtype=float, shape=sizeM) 
   resta3 = np.zeros(dtype=float, shape=sizeM) 
   resta4 = np.zeros(dtype=float, shape=sizeM) 

   #print(np.shape(suma1))

   for i in range(np.shape(P1)[1]):
      for j in range(np.shape(P1)[2]):
         suma1[i][j] = P1[1][i][j] + P1[0][i][j]
         suma2[i][j] = P2[1][i][j] + P2[0][i][j]
         suma3[i][j] = P3[1][i][j] + P3[0][i][j]
         suma4[i][j] = P4[1][i][j] + P4[0][i][j]
#RESTA
         resta1[i][j] = P1[1][i][j] - P1[0][i][j]
         resta2[i][j] = P2[1][i][j] - P2[0][i][j]
         resta3[i][j] = P3[1][i][j] - P3[0][i][j]
         resta4[i][j] = P4[1][i][j] - P4[0][i][j]

   sumaT=np.vstack((suma1,suma2,suma3,suma4))
   restaT=np.vstack((resta1,resta2,resta3,resta4))
   '''
   print("suma total")
   print(sumaT)
   print("resta total")
   print(restaT)
   '''