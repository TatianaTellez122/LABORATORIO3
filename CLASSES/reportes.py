# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 21:29:17 2022

@author: Tatiana Tellez
"""

from datetime import datetime
import time
import matplotlib.pyplot as plt 
import matplotlib.animation as animation


def get_all_temp():
    a=open("database/Datos.csv","r")
    datos=a.readlines()
    return datos


def grafico():
    datos=get_all_temp()
    eje_y=[]
    datos_0=";".join(datos)
    datos_0=datos_0.split(";")

    for i in range(len(datos_0)):
        e=datos_0[i].split(" ")
        eje_y.append(int(e[2]))
    print(eje_y)

    eje_x=[]
    for i in range(len(datos_0)):
        e=datos_0[i].split(" ")
        eje_x.append(e[1])
    print(eje_x)
    plt.plot(eje_x,eje_y)
    plt.show()
    

def valmax():
    d=get_all_temp()
    vector=[]
    datos_0=";".join(d)
    datos_0=datos_0.split(";")

    for i in range(len(datos_0)):
        m=datos_0[i].split(" ")
        vector.append(int(m[2]))
    maxi=max(vector)
    maxi_ub=[]

    for n in range(len(vector)):
        if vector[n] == maxi:
            maxi_ub.append(n)

    for i in range(len(maxi_ub)):
        r=datos_0[maxi_ub[i]].split(" ")
        print("El valor maximo de temperatura es "+str(r[2])+" en la fecha "+r[0]+" a la hora "+r[1])
        print("")


def valmin():
    d=get_all_temp()
    vector=[]
    datos_0=";".join(d)
    datos_0=datos_0.split(";")

    for i in range(len(datos_0)):
        h=datos_0[i].split(" ")
        vector.append(int(h[2]))
    mini=min(vector)
    mini_ub=[]

    for n in range(len(vector)):
        if vector[n] == mini:
            mini_ub.append(n)
 
    for i in range(len(mini_ub)):
        g=datos_0[mini_ub[i]].split(" ")
        print("El valor minimo de temperatura es "+str(g[2])+" en la fecha "+g[0]+" a la hora "+g[1])
        print("")


def temperaturaprom():
    d=get_all_temp()
    vector=[]
    datos_0=";".join(d)
    datos_0=datos_0.split(";")

    for i in range(len(datos_0)):
        h=datos_0[i].split(" ")
        vector.append(int(h[2]))
    suma = 0

    for valor in vector:
        suma = suma + valor
    promedio= suma / len(vector)
    dato=get_all_parametros()
    vec=[]
    dato=dato[0].split(";")

    
    print("La temperatura promedio es de"+str(promedio)+" grados centigrados")
    
    
def get_all_parametros():
    a=open("database/Parametros.csv","r")
    datos=a.readlines()
    
    return datos