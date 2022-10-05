# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 18:32:35 2022

@author: Tatiana Tellez
"""
from CLASSES.menu import *
from CLASSES.rangostemp import *
from CLASSES.pedirdatos import *
from CLASSES.reportes import *
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
import sys


global pause
pause = False
global y_data
y_data = []


def onclick(event):
    global pause
    print("pausa")
    pause=True
    


fig, ax=plt.subplots()
fig.canvas.mpl_connect("button_press_event", onclick)
            

def update_data(i): 
    if not pause:
        #dato=Puerto.leer(op_pu)
        dato=int(puerto.readline().decode().strip())
        print(dato)
        y_data.append(dato)
        ax.clear()
        ax.plot(y_data)
        time.sleep(1)
        

def main():
    menu=Menu()
    op=menu.ver()

    
    if op==1:
        menu2= Datos()
        op2=menu2.ver()
        if op2==1:
            solicitardatos()
            main()
        elif op2== 2:
            animacion= animation.FuncAnimation(fig,update_data)
            plt.show()
            print(y_data)
            save_dato(y_data)
            main()
        else:
            print("Ha seleccionado una opcion inválida")
            main()

   
    elif op==2:
        df=rangos()
        df.registroparametros()
        main()

   
    elif op==3:
        menu2=Reportes()
        op2=menu2.ver()
        if op2==1:
            grafico()
            main()
        elif op2==2:
            valor_max()
            main()
        elif op2==3:
            valor_min()
            main()
        elif op2==4:
            temperaturaprom()
            main()
        else:
            print("Ha seleccionado una opción inválida, por favor intente de nuevo")
            main()

 
    elif op == 4:
        print(sys.exit("Fin del proceso"))

  
    else:
        print("Ha seleccionado una opción inválida, por favor intente de nuevo")
        main()


if __name__=='__main__':
    main()
    