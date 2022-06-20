from mpi4py import MPI
import numpy as np
comm=MPI.COMM_WORLD
rank = comm.rank
size_ = (1000,1000)
#print("my rank is : " , rank)

destination_process9= 9   
#global start_time3

if rank==0:

    
    matriz1 = np.random.randint(10, size=size_).astype("float") / 100
    matriz2 = np.random.randint(10, size=size_).astype("float") / 100
    
    subMatriz1 = np.vsplit(matriz1,4)
    subMatriz2 = np.vsplit(matriz2,4)

    listaM1=(subMatriz1[0],subMatriz1[1],subMatriz1[2],subMatriz1[3])
    listaM2=(subMatriz2[0],subMatriz2[1],subMatriz2[2],subMatriz2[3])

    destination_process = 1
    destination_process2= 2
    destination_process3= 3
    destination_process4= 4
    destination_process5= 5
    destination_process6= 6
    destination_process7= 7
    destination_process8= 8    
    
    comm.send(listaM1,dest=destination_process)
    comm.send(listaM2,dest=destination_process)

    comm.send(listaM1,dest=destination_process2)
    comm.send(listaM2,dest=destination_process2)

    comm.send(listaM1,dest=destination_process3)
    comm.send(listaM2,dest=destination_process3)

    comm.send(listaM1,dest=destination_process4)
    comm.send(listaM2,dest=destination_process4)

    comm.send(listaM1,dest=destination_process5)
    comm.send(listaM2,dest=destination_process5)

    comm.send(listaM1,dest=destination_process6)
    comm.send(listaM2,dest=destination_process6)

    comm.send(listaM1,dest=destination_process7)
    comm.send(listaM2,dest=destination_process7)

    comm.send(listaM1,dest=destination_process8)
    comm.send(listaM2,dest=destination_process8)

    comm.send(matriz1,dest=destination_process9)
    comm.send(matriz2,dest=destination_process9)        

if rank==1:
    dataLista=comm.recv(source=0)
    dataLista2=comm.recv(source=0)
    
    sizeM = (len(dataLista[0]),len(dataLista[0]))
    suma = np.zeros(dtype=float, shape=sizeM)

    for i in range(len(dataLista[0])):
        for j in range(len(dataLista[0])):
            suma[i][j] = dataLista[0][i][j] + dataLista2[0][i][j]
    
    comm.send(suma,dest=destination_process9)




if rank==2:
    dataLista=comm.recv(source=0)
    dataLista2=comm.recv(source=0)
    sizeM = (len(dataLista[0]),len(dataLista[0]))
    suma = np.zeros(dtype=float, shape=sizeM)

    for i in range(len(dataLista[1])):
        for j in range(len(dataLista[1])):
            suma[i][j] = dataLista[1][i][j] + dataLista2[1][i][j]
    
    comm.send(suma,dest=destination_process9)   
            
if rank==3:
    dataLista=comm.recv(source=0)
    dataLista2=comm.recv(source=0)
    sizeM = (len(dataLista[0]),len(dataLista[0]))
    suma = np.zeros(dtype=float, shape=sizeM)

    for i in range(len(dataLista[2])):
        for j in range(len(dataLista[2])):
            suma[i][j] = dataLista[2][i][j] + dataLista2[2][i][j]
    
    comm.send(suma,dest=destination_process9)   


if rank==4:   
    dataLista=comm.recv(source=0)
    dataLista2=comm.recv(source=0)
    sizeM = (len(dataLista[0]),len(dataLista[0]))
    suma = np.zeros(dtype=float, shape=sizeM)

    for i in range(len(dataLista[3])):
        for j in range(len(dataLista[3])):
            suma[i][j] = dataLista[3][i][j] + dataLista2[3][i][j]

    comm.send(suma,dest=destination_process9)   



if rank==5:
    dataLista=comm.recv(source=0)
    dataLista2=comm.recv(source=0)
    sizeM = (len(dataLista[0]),len(dataLista[0])) 
    resta = np.zeros(dtype=float, shape=sizeM) 

    for i in range(len(dataLista[0])):
        for j in range(len(dataLista[0])):
            resta[i][j] = dataLista[0][i][j] - dataLista2[0][i][j]
    
    comm.send(resta,dest=destination_process9)


if rank==6:
    dataLista=comm.recv(source=0)
    dataLista2=comm.recv(source=0)
    sizeM = (len(dataLista[0]),len(dataLista[0])) 
    resta = np.zeros(dtype=float, shape=sizeM) 

    for i in range(len(dataLista[1])):
        for j in range(len(dataLista[1])):
            resta[i][j] = dataLista[1][i][j] - dataLista2[1][i][j]

    comm.send(resta,dest=destination_process9)


if rank==7:
    
    dataLista=comm.recv(source=0)
    dataLista2=comm.recv(source=0)
    sizeM = (len(dataLista[0]),len(dataLista[0])) 
    resta = np.zeros(dtype=float, shape=sizeM) 

    for i in range(len(dataLista[2])):
        for j in range(len(dataLista[2])):
            resta[i][j] = dataLista[2][i][j] - dataLista2[2][i][j]

    comm.send(resta,dest=destination_process9)


if rank==8:    
    dataLista=comm.recv(source=0)
    dataLista2=comm.recv(source=0)
    sizeM = (len(dataLista[0]),len(dataLista[0])) 
    resta = np.zeros(dtype=float, shape=sizeM) 

    for i in range(len(dataLista[3])):
        for j in range(len(dataLista[3])):
            resta[i][j] = dataLista[3][i][j] - dataLista2[3][i][j]

    comm.send(resta,dest=destination_process9)
 
if rank==9:
    start_time3 = MPI.Wtime()    
    sumaP1=comm.recv(source=1)
    sumaP2=comm.recv(source=2)
    sumaP3=comm.recv(source=3)
    sumaP4=comm.recv(source=4)

    restaP1=comm.recv(source=5)
    restaP2=comm.recv(source=6)
    restaP3=comm.recv(source=7)
    restaP4=comm.recv(source=8)

    valor1=comm.recv(source=0)
    valor2=comm.recv(source=0)

    
    sumaT=np.vstack((sumaP1,sumaP2,sumaP3,sumaP4))
    restaT=np.vstack((restaP1,restaP2,restaP3,restaP4))
    

    
    #for i in range(5):
        #print(" %f + %f = %f" % (valor1[i][i], valor2[i][i], sumaT[i][i]))

    #print("Resta de matrices")
    #for i in range(5):
        #print(" %f - %f = %f" % (valor1[i][i], valor2[i][i], restaT[i][i]))
    #print("------------------RANGO------------------------------------------")
    #print(len(sumaT))
    #print(len(restaT))

    #print("--Matriz")
    #print(len(valor1))
    #print(len(valor2))

    end_time3 = MPI.Wtime()  
    #print("Tiempo Rank Total: " + str(end_time3-start_time3))  

