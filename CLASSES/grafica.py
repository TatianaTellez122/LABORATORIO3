# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 22:28:20 2022

@author: Tatiana Tellez
"""

import serial
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
pause=False

try:
    global puerto
    puerto = serial.Serial("COM12",9600)
    puerto.close()
    puerto.open()
    print("Port is open")
except:
    print("Problemas abriendo puerto :( ")
    
def onclick(event):
    global pause
    print("pausa")
    pause=True


fig, ax=plt.subplots()
fig.canvas.mpl_connect("button_press_event", onclick)
y_data=[]

def update_data(i):#parametro i para que tome referencia de que punto debe ir mostrando 
    if not pause:
        punto=puerto.readline().decode().strip()
        print(punto)
        y_data.append(punto)
        ax.clear()
        ax.plot(y_data)

ani= animation.FuncAnimation(fig,update_data)
plt.show()

