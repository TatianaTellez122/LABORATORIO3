# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 20:58:20 2022

@author: Tatiana Tellez
"""
class Parametros:
    f="database/Parametros.csv"
    def __init__(self,valminh,valmaxh,valminn,valmaxn,valminf,valmaxf):
        self.valminh=valminh
        self.valmaxh=valmaxh
        self.valminn=valminn
        self.valmaxn=valmaxn
        self.valminf=valminf
        self.valmaxf=valmaxf
        
    def registroparametros(self):
        f=open(self.file,"w")
        linea=";".join([str(self.min_hip),str(self.max_hip),str(self.min_nor),str(self.max_nor),str(self.min_fie),str(self.max_fie)])
        f.write(linea+"\n")
        f.close()    
        
def rangos():
    print("Ingrese valor máximo y minimo del rango de Hipotermia")
    min_hip=int(input("Valor mínimo"))
    max_hip=int(input("Valor maximo"))
    print("")

    print("Ingrese valor máximo y minimo del rango de Temperatura normal")
    min_nor=int(input("Valor mínimo"))
    max_nor=int(input("Valor maximo"))
    print("")

    print("Ingrese valor máximo y minimo del rango de Fiebre")
    min_fie=int(input("Valor mínimo"))
    max_fie=int(input("Valor maximo"))
    print("")
    df=Parametros(min_hip,max_hip,min_nor,max_nor,min_fie,max_fie)
    
    return df
