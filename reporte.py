# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 11:43:13 2022

@author: Catalina
"""
#______________________________________________________________________________
# LIBRERÍAS
#
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression 
import numpy as np
#______________________________________________________________________________
# RECOPILACIÓN DE DATOS
#
tabla1 = pd.read_excel('1NA.xlsx')
#______________________________________________________________________________
# EXPORTACIÓN DE DATOS
#
Carga = tabla1.FORCE #Fuerza aplicada en N
deformacion = tabla1.EXT #alargamiento del especímen %
Deformacion = abs(deformacion/(100*100)) #alargamiento del especímen mm/mm
Alargamiento = tabla1.POSIT #alargamiento del especímen
Deformacion = Alargamiento/25
#______________________________________________________________________________
# ENTRADAS Y SALIDAS / CARACTERÍSTICAS DEL MATERIAL
#
area = 6.48*6.03 #área de la sección transversal en mm
longitud_inicial = 25; #Longitud inicial del especímen mm
Esfuerzo = Carga/area
# Alargamiento = Deformacion/longitud_inicial
max_esf = np.amax(Esfuerzo) # Esfuerzo último
S_f = Esfuerzo[len(Esfuerzo)-1] # Esfuerzo a la fractura
F_f = S_f*area # Fuerza de fractura
e_f = Alargamiento[len(Alargamiento)-1] # Alargamiento a la fractura
#______________________________________________________________________________
#______________________________________________________________________________
# CURVAS Carga Vs Alargamiento ...
#
plt.figure(figsize=(8,5), layout="constrained")
# plt.subplot(211)
plt.plot(Alargamiento, Carga, color="blue", linewidth=".7")
# plt.title("Carga Vs Alargamiento")
plt.xlabel(r'$\delta$'+'(mm)')
plt.ylabel(r'$F$'+' (N)')
plt.xlim([0,e_f])
#______________________________________________________________________________
# DELIMITACIÓN DE LA ZONA ELÁSTICA
#
LE = Esfuerzo/Deformacion 
for i in Esfuerzo:
  pos = np.where(Esfuerzo == i)[0][0] #i es el valor del esfuerzo
  if pos < len(Esfuerzo)-1:
    index = pos 
    #si la sensibilidad del módulo de young es cercana al 5%
    print(LE[index+1]/LE[index])
    if LE[index+1]/LE[index]<1 and LE[index+1]/LE[index]>0.999:
       limit = np.where(Esfuerzo==i)[0][0]
       print(i)
          

sigma = [] #asignación de los datos de esfuerzo a un array
for i in Esfuerzo:
  if np.where(Esfuerzo == i)[0][0] < limit:
    sigma.append(i)
#______________________________________________________________________________
# ESFUERZO DE FLUENCIA
#
Sy_Sigma = np.amax(sigma)
sd_e = Deformacion[np.where(Esfuerzo==Sy_Sigma)[0][0]]
#______________________________________________________________________________
# MÓDULO DE YOUNG / LÍMITE ELÁSTICO
#
Sigma = []
Epsilon = []
delta_l = []
for i in Esfuerzo:
  if np.where(Esfuerzo == i)[0][0] < np.where(Esfuerzo == Sy_Sigma)[0][0]:
    if i > 200 and i < 300:
      index = np.where(Esfuerzo==i)[0][0]
      Sigma.append(i)
      epsilon = Deformacion[index]
      Epsilon.append(epsilon)
      delta_l.append(epsilon*longitud_inicial)
      
regresion_lineal = LinearRegression() # instancia de LinearRegression
regresion_lineal.fit(np.reshape(Epsilon,(-1,1)), Sigma)
E = regresion_lineal.coef_/1000

estimado_sigma = regresion_lineal.predict(np.reshape(Epsilon,(-1,1)))
estimado_carga = estimado_sigma*area
rho = np.corrcoef(Epsilon, estimado_sigma)

print(rho)
#______________________________________________________________________________
# ELONGACIÓN
epsilon_e = (e_f/longitud_inicial-(S_f/(E*1000)))*100
e = epsilon*longitud_inicial
#______________________________________________________________________________
#______________________________________________________________________________
#...Curvas Esfuerzo Vs Deformación
#
plt.figure()
plt.plot(Deformacion,Esfuerzo, color="blue", linewidth=".7")
# plt.plot(Epsilon, estimado_sigma, color="red", linewidth=".7")
plt.title("Esfuerzo Vs Deformación")
plt.xlabel(r'$\epsilon$'+' (mm/mm)')
plt.ylabel(r'$\sigma$'+' (MPa)')
plt.xlim([0,sd_e-0.0005])
plt.scatter([Epsilon[0],Epsilon[len(Epsilon)-1]],
            [estimado_sigma[0],estimado_sigma[len(estimado_sigma)-1]])
plt.text(Epsilon[0], estimado_sigma[0],
         str(round(Epsilon[0],5))+' , '+
         str(round(estimado_sigma[0],2))+'  ', horizontalalignment='right',
         verticalalignment="bottom")
plt.text(Epsilon[len(Epsilon)-1], estimado_sigma[len(estimado_sigma)-1],
         str(round(Epsilon[len(Epsilon)-1],5))+' , '+
         str(round(estimado_sigma[len(estimado_sigma)-1],2))+'  ', 
         horizontalalignment='right')

plt.subplots_adjust(left=0.125,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.2, 
                    hspace=0.6)
#______________________________________________________________________________
# VISUALIZACIÓN DE DATOS
#
plt.figure(layout="constrained")
plt.subplot(131)
plt.plot(Deformacion, Esfuerzo, color="blue", linewidth=".7")
plt.plot(Epsilon, estimado_sigma, color="red", linewidth=".7")
plt.plot(sd_e, Sy_Sigma, color="white", marker='o', markerfacecolor='black', markersize=3)
plt.xlabel('Deformación (mm/mm)')
plt.ylabel('Esfuerzo (MPa)')
plt.legend(['',
            'E = '+str(E)+' GPa',
            'Sy = '+str(round(Sy_Sigma, 2))+' MPa \n'
            'Smax = '+str(round(max_esf,2))+' MPa \n'
            'Sf = '+str(round(S_f,2))+' MPa']);

plt.subplot(122)
plt.plot(Alargamiento,Carga, color="blue", linewidth=".7")
plt.plot(delta_l, estimado_carga, color="red", linewidth=".7")
plt.plot([e,e_f], [0,F_f], linestyle="--", color="red", linewidth=".5")
plt.xlabel('Alargamiento (mm)')
plt.ylabel('Carga (N)')
plt.legend(['Fy = '+str(round(Sy_Sigma*area, 2))+' N \n'
            'Fmax = '+str(round(max_esf*area,2))+' N \n'
            'Ff = '+str(round(F_f,2))+' N \n'
            'e = '+str(epsilon_e)+' %']);