#Por Francisco Giacomozzi R.
#----------------------------------------------
import random as ra
from math import e

F = lambda c,u : [
            [ c*(u[1]+u[5]+u[6]-3*u[0])],     #u1
            [ c*(u[0]+u[2]-2*u[1])],          #u2
            [ c*(u[1]+u[3]-2*u[2])],          #u3
            [ c*(u[2]+u[4])-2*u[3]],	      #u4
            [c*(u[3]+u[5]-2*u[4])], 	      #u5
            [c*(u[0]+u[4]+u[6]-3*u[5])],	  #u6
            [c*(u[0]+u[5]-2*u[6])],		      #u7
]
#Se establece un tiempo inicial y un tiempo final usando lib random
nTi=0  
nTf=ra.randint(4, 7)

#Valores para U
aU = ra.sample(range(0,20), 7)

#DT
h=ra.random()

#Valor para la constante
nC=ra.randint(0,20)

def metodoHeun(t,u,h,f,F,c):
    T = [t];P=[];C=[];CU=u
    for i in range(0,len(u)):
        P.append([u[i]])
        C.append([u[i]])
    for i in range(0,f):
        T.append(T[i]+h)
        for j in range(0,len(u)):
            SF=F(c,CU)
            DT=T[i+1]-T[i]
            P[j].append(P[j][i]+((SF[j][0])*DT))
            CUP=[]
            for data in P:
                CUP.append(data[i])
            SFP=F(c,CUP)
            C[j].append(C[j][i]+((SFP[j][0]+SF[j][0])/2)*DT)
    return P,C,T

def resEcuacion(t,u,h,f,F,c):
    T = [t];U = []
    for i in range(0,len(u)):
        U.append([u[i]])
    for i in range(0,f):
        T.append(T[i]+h)
        for j in range(0,len(u)):
            CU=[]
            for data in U:
                CU.append(data[0])
            SF=F(c,CU)
            U[j].append(U[j][i]+h*SF[j][0])
    return U,T


aPrediccion,aCorreccion,aTiempoH=metodoHeun(nTi,aU,h,nTf,F,nC)
aResultados,aTiempo=resEcuacion(nTi,aU,h,nTf,F,nC)
nMax=len(aPrediccion)

def muestraData():
    print("Metodo de Heun con el modelo creado")
    print("#-------------------------------------------------------------------------#")
    print("Parametros utilizados")
    print("Tiempo Inicial: "+str(nTi)," Tiempo Final: "+str(nTf)) 
    print("Arreglo de valores de U: "+str(aU))
    print("Constante: "+str(nC))
    print("Valores para u: \n")
    for i in range(0,nMax):
        print("u"+str(i+1)," Prediccion :",aPrediccion[i])
        print("u"+str(i+1)," Coreccion :",aCorreccion[i],"\n")

muestraData()