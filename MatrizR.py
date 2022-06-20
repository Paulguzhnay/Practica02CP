from ast import Div
import numpy as np
from mpi4py import MPI 
comm = MPI.COMM_WORLD 
i=0
size = comm.size 
rank = comm.rank

size_ = (10000,10000)
lista1 = []
lista2 = []

matriz1 = np.random.randint(10, size=size_).astype("float") / 100
sub_matriz1 = np.vsplit(matriz1, 4)

Div1=sub_matriz1[0]
Div2=sub_matriz1[1]
Div3=sub_matriz1[2]
Div4=sub_matriz1[3]


sizeM=np.shape(Div1)
suma1 = np.zeros(dtype=float, shape=sizeM)
suma2 = np.zeros(dtype=float, shape=sizeM)
suma3 = np.zeros(dtype=float, shape=sizeM)
suma4 = np.zeros(dtype=float, shape=sizeM)

comm.Reduce(Div1,suma1,root=0,op=MPI.SUM)
comm.Reduce(Div2,suma2,root=0,op=MPI.SUM)
comm.Reduce(Div3,suma3,root=0,op=MPI.SUM)
comm.Reduce(Div4,suma4,root=0,op=MPI.SUM)

sumaT=np.vstack((suma1,suma2,suma3,suma4))

#--------------------------------------------RESTA--------------------------------------------
resta1 = np.zeros(dtype=float, shape=sizeM)
resta2 = np.zeros(dtype=float, shape=sizeM)
resta3 = np.zeros(dtype=float, shape=sizeM)
resta4 = np.zeros(dtype=float, shape=sizeM)

#RESTA
Div1R=Div1
Div2R=Div2
Div3R=Div3
Div4R=Div4
#print(i)
if(i==1):
    Div1R=np.negative(Div1)
    Div2R=np.negative(Div2)
    Div3R=np.negative(Div3)
    Div4R=np.negative(Div4)



if rank == 0:
    sumaP1=np.vstack((Div1,Div2,Div3,Div4))
    restaP1=np.vstack((Div1R,Div2R,Div3R,Div4R))
    #print("RESTA MATRIZ 1")
    #print(restaP1)

    i=i+1
    
else:
    sumaP2=np.vstack((Div1,Div2,Div3,Div4))
    Div1R=np.negative(Div1)
    Div2R=np.negative(Div2)
    Div3R=np.negative(Div3)
    Div4R=np.negative(Div4)
    restaP2=np.vstack((Div1R,Div2R,Div3R,Div4R))
    #print("RESTA MATRIZ 2")
    #print(restaP2)

#----------------------OPERACION RESTA------------------------------
comm.Reduce(Div1R,resta1,root=0,op=MPI.SUM)
comm.Reduce(Div2R,resta2,root=0,op=MPI.SUM)
comm.Reduce(Div3R,resta3,root=0,op=MPI.SUM)
comm.Reduce(Div4R,resta4,root=0,op=MPI.SUM)
restaT=np.vstack((resta1,resta2,resta3,resta4))

'''
if(i==1):
    print("==============================================")
    print(restaT)
'''
