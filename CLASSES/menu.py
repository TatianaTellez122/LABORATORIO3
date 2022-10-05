# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 18:32:16 2022

@author: Tatiana Tellez
"""

class Menu():
    
      def ver(self):
        print("MONITOR DE TEMPERATURA".center(50,"*"))
        print("Laboratorio 3: ")
        print("1. Captura de datos")
        print("2. Configuracion de parametros")
        print("3. Reportes")
        print("4. Salir")
        op=input(">>>")
        return op

class Datos:
    def ver(self):
      print("CAPTURA DE DATOS".center(20,"*"))
      print('''Seleccione la forma en la cual desea realizar la obtención de datos de temperatura:
            1. Número de datos 
            2. Gráfica en tiempo real ''')
      op=input(">>> ")
      
      return op


class Reportes():
    
    def ver(self):
      print("MENÚ REPORTES".center(20,"*"))
      print("1. Ver gráfica de los datos capturados")
      print("2. Valor maximo")
      print("3. Valor minimo")
      print("4. Promedio de temperatura")
      op=int(input(">>> "))
      
      return op


        
        
