
# generación de matrices
import numpy as np   

size_ = (1000,1000)
matriz1 = np.random.randint(10, size=size_).astype("float") / 100
matriz2 = np.random.randint(10, size=size_).astype("float") / 100



#print(matriz1[:10][:10])
#print(matriz2[:10][:10])

# suma de matrices secuencial
import time



#TODO: implementar los metodos necesarios para realizar la suma y resta de matrices aplicando técnicas de multiprocesamiento

subMatriz = np.vsplit(matriz1,4)
sizeM = (len(subMatriz[0]),len(subMatriz[0]))
global sumaT
global restaT
suma1 = np.zeros(dtype=float, shape=sizeM)
suma2 = np.zeros(dtype=float, shape=sizeM)
suma3 = np.zeros(dtype=float, shape=sizeM)
suma4 = np.zeros(dtype=float, shape=sizeM)

resta1 = np.zeros(dtype=float, shape=sizeM)
resta2 = np.zeros(dtype=float, shape=sizeM)
resta3 = np.zeros(dtype=float, shape=sizeM)
resta4 = np.zeros(dtype=float, shape=sizeM)

#******************************************MULTIPROCESOS*************************************************************
def MultiProcesoSuma ():
  
  subMatriz = np.vsplit(matriz1,4)
  subMatriz2 = np.vsplit(matriz2,4)

  subM0=subMatriz[0]
  subM1=subMatriz[1]
  subM2=subMatriz[2]
  subM3=subMatriz[3]

  sub2M0=subMatriz2[0]
  sub2M1=subMatriz2[1]
  sub2M2=subMatriz2[2]
  sub2M3=subMatriz2[3]
  sizeM = (len(subM0[0]),len(subM0[0]))

#--------------------------------------------
  sizeM= (len(subM0),len(sub2M0))

  name = multiprocessing.current_process().name

  if(name=='proceso1'):
    print(name)
    for i in range(len(subMatriz[0])):
      for j in range(len(subMatriz[0])):
        suma1[i][j] = subM0[i][j]+sub2M0[i][j]


  if(name=='proceso2'):
    print(name) 
    for i in range(len(subMatriz[0])):
      for j in range(len(subMatriz[0])):
        suma2[i][j] = subM1[i][j]+sub2M1[i][j]


  if(name=='proceso3'):
    print(name) 

    for i in range(len(subMatriz[0])):
      for j in range(len(subMatriz[0])):
        suma3[i][j] = subM2[i][j]+sub2M2[i][j]
        
  if(name=='proceso4'):
    print(name) 

    for i in range(len(subMatriz[0])):
      for j in range(len(subMatriz[0])):
        suma4[i][j] = subM3[i][j]+sub2M3[i][j]
       
  sumaT=np.vstack((suma1,suma2,suma3,suma4))

def MultiProcesoResta ():

  subMatriz = np.vsplit(matriz1,4)
  subMatriz2 = np.vsplit(matriz2,4)

  subM0=subMatriz[0]
  subM1=subMatriz[1]
  subM2=subMatriz[2]
  subM3=subMatriz[3]

  sub2M0=subMatriz2[0]
  sub2M1=subMatriz2[1]
  sub2M2=subMatriz2[2]
  sub2M3=subMatriz2[3]
  sizeM = (len(subM0[0]),len(subM0[0]))

#--------------------------------------------
  sizeM= (len(subM0),len(sub2M0))


  name = multiprocessing.current_process().name

  if(name=='proceso5'):
    print(name) 

    for i in range(len(subMatriz[0])):
      for j in range(len(subMatriz[0])):
        resta1[i][j] = subM0[i][j]-sub2M0[i][j]


  if(name=='proceso6'):
    print(name) 

    for i in range(len(subMatriz[0])):
      for j in range(len(subMatriz[0])):
        resta2[i][j] = subM1[i][j]-sub2M1[i][j]


  if(name=='proceso7'):
    print(name) 

    for i in range(len(subMatriz[0])):
      for j in range(len(subMatriz[0])):
        resta3[i][j] = subM2[i][j]-sub2M2[i][j]
        
  if(name=='proceso8'):
    print(name) 

    for i in range(len(subMatriz[0])):
      for j in range(len(subMatriz[0])):
        resta4[i][j] = subM3[i][j]-sub2M3[i][j]
  
  restaT=np.vstack((resta1,resta2,resta3,resta4))

#Ejecución de funciones  de multiprocesamiento
import multiprocessing
if __name__ == "__main__":  
    inicio = time.time()
    proceso1 = multiprocessing.Process\
                         (name='proceso1',\
                          target=MultiProcesoSuma)    #TODO: llamar a los metodos necesarios para realizar la suma
    proceso2 = multiprocessing.Process\
                         (name='proceso2',\
                          target=MultiProcesoSuma) 
    proceso3 = multiprocessing.Process\
                         (name='proceso3',\
                          target=MultiProcesoSuma)    #TODO: llamar a los metodos necesarios para realizar la suma
    proceso4 = multiprocessing.Process\
                         (name='proceso4',\
                          target=MultiProcesoSuma) 
    proceso5 = multiprocessing.Process\
                         (name='proceso5',\
                          target=MultiProcesoResta)    #TODO: llamar a los metodos necesarios para realizar la suma
    proceso6 = multiprocessing.Process\
                         (name='proceso6',\
                          target=MultiProcesoResta) 
    proceso7 = multiprocessing.Process\
                         (name='proceso7',\
                          target=MultiProcesoResta)    #TODO: llamar a los metodos necesarios para realizar la suma
    proceso8 = multiprocessing.Process\
                         (name='proceso8',\
                          target=MultiProcesoResta)                                                
    
    proceso1.start()
    proceso2.start()
    proceso3.start()
    proceso4.start()
    proceso5.start()
    proceso6.start()
    proceso7.start()
    proceso8.start()

    proceso1.join()    
    proceso2.join()
    proceso3.join()
    proceso4.join()
    proceso5.join()
    proceso6.join()
    proceso7.join()
    proceso8.join()


    fin = time.time()  

    print("El proceso de sumar y restar las matrices paralelamente se ejecutó en %d segundos" % (fin - inicio))



