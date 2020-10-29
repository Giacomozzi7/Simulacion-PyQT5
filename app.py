#Por Francisco Giacomozzi R.
#----------------------------------------------
import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QMessageBox
from PyQt5 import uic
from functools import partial
import random as ra
import math as e

#Clase para instanciar la ventana a utilizar
class Ventana(QMainWindow):
    #Se inicializan los componentes y las variables iniciales
    #Se establece el modelo a resolver
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi('C:\\Users\\frant\\Desktop\\EC DIF\\Simulacion\\interfaz.ui',self)
        self.setWindowTitle("Simulacion")
        self.setMinimumSize(1280,720)
        self.setMaximumSize(1280,720)
        self.nTi=0
        self.nTf=0
        self.nC=0
        self.F = lambda c,u : [
            [ c*(u[1]+u[5]+u[6]-3*u[0])],     #u1
            [ c*(u[0]+u[2]-2*u[1])],          #u2
            [ c*(u[1]+u[3]-2*u[2])],          #u3
            [ c*(u[2]+u[4])-2*u[3]],	      #u4
            [c*(u[3]+u[5]-2*u[4])], 	      #u5
            [c*(u[0]+u[4]+u[6]-3*u[5])],	  #u6
            [c*(u[0]+u[5]-2*u[6])],		      #u7
        ]
        self.pushBoton()

    #Envia numero del boton al label
    #Boton 8 procede a hacer los calculos
    def pushBoton(self):
        self.pushButton.clicked.connect(partial(self.cambiaLabel, numero=self.pushButton.text()))
        self.pushButton_2.clicked.connect(partial(self.cambiaLabel, numero=self.pushButton_2.text()))
        self.pushButton_3.clicked.connect(partial(self.cambiaLabel, numero=self.pushButton_3.text()))
        self.pushButton_4.clicked.connect(partial(self.cambiaLabel, numero=self.pushButton_4.text()))
        self.pushButton_5.clicked.connect(partial(self.cambiaLabel, numero=self.pushButton_5.text()))
        self.pushButton_6.clicked.connect(partial(self.cambiaLabel, numero=self.pushButton_6.text()))
        self.pushButton_7.clicked.connect(partial(self.cambiaLabel, numero=self.pushButton_7.text()))
        self.pushButton_8.clicked.connect(self.calcular)
    
    #Recibe el numero del boton y cambia el label
    def cambiaLabel(self,numero):
        self.num.setText(str(numero))
    
    #Se validan los datos ingresados y se randomizan los valores para u y h
    #Procede a ejecutar la funcion del metodo de heun
    def calcular(self):
        try:
            self.nTi =int(self.ti.text()) 
            self.nTf = int(self.tf.text()) 
            self.nC = int(self.c.text())
            self.aU = ra.sample(range(0,20), 7)
            self.h=ra.random()
            self.metodoHeun(self.nTi,self.aU,self.h,self.nTf,self.F,self.nC)
        except:
            QMessageBox.about(self, "Error", "Se debe introducir numero entero")

    #Se resuelve el sistema usando el metodo de heun
    def metodoHeun(self,t,u,h,f,F,c):
        self.T = [t];self.P=[];self.C=[];CU=u
        for i in range(0,len(u)):
            self.P.append([u[i]])
            self.C.append([u[i]])
        for i in range(0,f):
            self.T.append(self.T[i]+h)
            for j in range(0,len(u)):
                SF=F(c,CU)
                DT=self.T[i+1]-self.T[i]
                self.P[j].append(self.P[j][i]+((SF[j][0])*DT))
                CUP=[]
                for data in self.P:
                    CUP.append(data[i])
                SFP=F(c,CUP)
                self.C[j].append(self.C[j][i]+((SFP[j][0]+SF[j][0])/2)*DT)
        self.muestraData()
    
    #Muestra la prediccion y correccion para el nodo elegido
    def muestraData(self):
        self.nIndice=int(self.num.text())
        self.pred.setPlainText(str(self.P[self.nIndice-1]))
        self.corr.setPlainText(str(self.C[self.nIndice-1]))

app = QApplication(sys.argv)
gui=Ventana()
gui.show()
sys.exit(app.exec_())