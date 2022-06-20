from logging import root
from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
print(rank)
size_ = (10000,10000)
destino=5
if rank == 0:
   matriz1 = np.random.randint(10, size=size_).astype("float") / 100
   matriz2 = np.random.randint(10, size=size_).astype("float") / 100 
   subMatriz1 = np.vsplit(matriz1,4)
   subMatriz2 = np.vsplit(matriz2,4)

   array_to_share = [0,subMatriz1[0],subMatriz1[1],subMatriz1[2],subMatriz1[3],0] 
   array_to_share2 = [0,subMatriz2[0],subMatriz2[1],subMatriz2[2],subMatriz2[3],0] 

   comm.scatter(array_to_share,root=0)        
   comm.scatter(array_to_share2,root=0)

   #Envio matriz completa
   comm.send(matriz1,dest=destino)    
   comm.send(matriz2,dest=destino)
else:
   array_to_share=None
   array_to_share2=None

if rank==1:
   recvbuf = comm.scatter(array_to_share, root=0)
   recvbuf2 = comm.scatter(array_to_share2, root=0)

   sizeM = (np.shape(recvbuf))
   suma = np.zeros(dtype=float, shape=sizeM)
   resta = np.zeros(dtype=float, shape=sizeM)
   for i in range(np.shape(recvbuf)[0]):
      for j in range(np.shape(recvbuf)[1]):
            suma[i][j] = recvbuf[i][j] + recvbuf2[i][j]
            resta[i][j] = recvbuf[i][j] - recvbuf2[i][j]
   
   comm.send(suma,dest=destino)    
   comm.send(resta,dest=destino)
else:
   suma=None 

if rank==2:
   recvbuf = comm.scatter(array_to_share, root=0)
   recvbuf2 = comm.scatter(array_to_share2, root=0)
   sizeM = (np.shape(recvbuf))
   suma = np.zeros(dtype=float, shape=sizeM)
   resta = np.zeros(dtype=float, shape=sizeM)

   for i in range(np.shape(recvbuf)[0]):
      for j in range(np.shape(recvbuf)[1]):
            suma[i][j] = recvbuf[i][j] + recvbuf2[i][j]
            resta[i][j] = recvbuf[i][j] - recvbuf2[i][j]
   
   comm.send(suma,dest=destino)    
   comm.send(resta,dest=destino)
else:
   suma=None 


if rank==3:
   recvbuf = comm.scatter(array_to_share, root=0)
   recvbuf2 = comm.scatter(array_to_share2, root=0)
   sizeM = (np.shape(recvbuf))
   suma = np.zeros(dtype=float, shape=sizeM)
   resta = np.zeros(dtype=float, shape=sizeM)

   for i in range(np.shape(recvbuf)[0]):
      for j in range(np.shape(recvbuf)[1]):
            suma[i][j] = recvbuf[i][j] + recvbuf2[i][j]
            resta[i][j] = recvbuf[i][j] - recvbuf2[i][j]
   
   comm.send(suma,dest=destino)    
   comm.send(resta,dest=destino)
else:
   suma=None 

if rank==4:
   recvbuf = comm.scatter(array_to_share, root=0)
   recvbuf2 = comm.scatter(array_to_share2, root=0)
   sizeM = (np.shape(recvbuf))
   suma = np.zeros(dtype=float, shape=sizeM)
   resta = np.zeros(dtype=float, shape=sizeM)

   for i in range(np.shape(recvbuf)[0]):
      for j in range(np.shape(recvbuf)[1]):
            suma[i][j] = recvbuf[i][j] + recvbuf2[i][j]
            resta[i][j] = recvbuf[i][j] - recvbuf2[i][j]
   
   comm.send(suma,dest=destino)    
   comm.send(resta,dest=destino)
else:
   suma=None    

if rank==5:
   recvbuf = comm.scatter(array_to_share, root=0)
   recvbuf2 = comm.scatter(array_to_share2, root=0)
   sumaP1=comm.recv(source=1)
   sumaP2=comm.recv(source=2)
   sumaP3=comm.recv(source=3)
   sumaP4=comm.recv(source=4)

   restaP1=comm.recv(source=1)
   restaP2=comm.recv(source=2)
   restaP3=comm.recv(source=3)
   restaP4=comm.recv(source=4)
   
   valor1=comm.recv(source=0)
   valor2=comm.recv(source=0)

    
   sumaT=np.vstack((sumaP1,sumaP2,sumaP3,sumaP4))
   restaT=np.vstack((restaP1,restaP2,restaP3,restaP4))
'''
   print(valor1)
   print("--------------------")
   print(valor2)
   print("================================================")
   print(restaT)      
   print("hola rank5")
'''