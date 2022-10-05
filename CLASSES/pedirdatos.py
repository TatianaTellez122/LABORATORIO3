# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 18:32:40 2022

@author: Tatiana Tellez
"""

from datetime import datetime
import time
import serial
import struct
import matplotlib.pyplot as plt 
import matplotlib.animation as animation


try:
    global puerto
    puerto = serial.Serial("COM12",9600)
    puerto.close()
    puerto.open()
    print("Port is open")
except:
    print("Problemas abriendo puerto :( ")
    
    
def solicitardatos():
    ob=int(input("Por favor ingrese el número de datos que desea obtener"))
    file="database/Datos.csv"
    f=open(file,"w")
    datos=get_all_parametros()
    vec=[]
    datos_0=datos[0].split(";")
    for i in range (len(datos_0)):
        vec.append(int(datos_0[i]))
        
    for i in range(ob):
        now = datetime.now()
        now=now.strftime('%d/%m/%Y %H:%M:%S')
        dato=int(puerto.readline().decode().strip())
        if dato>= vec[0] and dato <=vec[1]:
            temp="H"
        elif dato >=vec[2] and dato <= vec[3]:
            temp ="N"
        elif dato >=vec[4] and dato <= vec[5]:
            temp="F"
        else:
            temp="N"
        puerto.write(temp.encode())
        linea=now+" " + str(dato)
        linea.replace(" ", ";")
        f.write(linea+"\n")
        time.sleep(1)
    f.close()

    return puerto    

def get_all_parametros():
    a=open("database/Parametros.csv","r")
    datos=a.readlines()

    return 

def save_dato(y_data):
    y_data=y_data
    file="database/Datos.csv"
    f=open(file,"w")
    datos=get_all_parametros()
    vec=[]
    datos_0=datos[0].split(";")
    for i in range (len(datos_0)):
        vec.append(int(datos_0[i]))
  
    for i in range(len(y_data)):
        now = datetime.now()
        now=now.strftime('%d/%m/%Y %H:%M:%S')
        if y_data[i]>= vec[0] and y_data[i] <=vec[1]:
            temp="H"
        elif y_data[i] >=vec[2] and y_data[i]<= vec[3]:
            temp ="N"
        elif y_data[i] >=vec[4] and y_data[i] <= vec[5]:
            temp="F"
        else:
            temp="N"
        puerto.write(temp.encode())
        linea=now+" " + str(y_data[i])
        linea.replace(" ", ";")
        f.write(linea+"\n")
        time.sleep(0.5)
    f.close()