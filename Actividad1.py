"""
DISENIO OPTIMO DE UN MECANISMO DE CUATRO BARRAS
Dimensionamiento para un segmento rectilineo de 20 Cm y un rango de giro de 55 grados
segun criterios de rectitud y velocidad (Norton. Design of Machinery)
Metodo: Interpolacion de Lagrange
"""
#_______________________________________________________________________
# Librerias_____________________________________________________________
#
from symtable import Symbol
import numpy as np # Libreria numpy
import sympy as sym # Libreria Sympy, para desarrollar la forma algebraica del polinomio
import matplotlib.pyplot as plt # Libreria Matplotlib, para graficas
#_______________________________________________________________________
# angulo de recorrido de la linea cuasi recta___________________________
#
deltax = 20 # cm
xi = np.array([20, 40, 60, 80])
#_______________________________________________________________________
# Datos de prueba segun el criterio de rectitud_________________________
#
l1l2_r = np.array([2.975, 2.950, 2.900, 2.825]) # L1/L2
l3l2_r = np.array([3.963, 3.925, 3.850, 3.738]) # L3/L2
dxl2_r = np.array([0.601, 1.193, 1.763, 2.299]) # Delta_x/L2
#_______________________________________________________________________
# Datos de prueba segun el criterio de velocidad________________________
#
l1l2_v = np.array([2.075, 2.050, 2.025, 1.975]) # L1/l2
l3l2_v = np.array([2.613, 2.575, 2.538, 2.463]) # L3/L2
dxl2_v = np.array([0.48, 0.95, 1.411, 1.845]) # Delta_x/L2
#_______________________________________________________________________
# Procedimiento_________________________________________________________
#
n = len(xi) # numero de elementos de las entradas a evaluar
x = sym.Symbol('x') # simbolo algebraico de la variable de entrada
radios = np.array([l1l2_r, l3l2_r, dxl2_r, l1l2_v, l3l2_v, dxl2_v]) # arreglo de datos de prueba
polinomios = [] # arreglo de polinomios inicializados para cada radio
PX = [] # arreglo vacio para almacenamiento de polinomios
#
# Recorrido por cada indice del arreglo radios
for k in range(0, len(radios), 1):
    # Inicializando el polinomio
    polinomios.append(0)
    # Recorrido por cada indice de los datos de prueba
    for i in range(0,n,1):
        # Para calcular el primer termino de la Langrage, es necesario calcular un numerador que se obtiene por multiplicaciones
        numerador = 1
        denominador = 1
        # Recorrido del numerador por todos los puntos del arreglo xi
        for j in range(0,n,1):
            if (i != j):
                numerador = numerador*(x-xi[j])
                denominador = denominador*(xi[i]-xi[j])
            # Terminos de lagrange
            termino = (numerador/denominador)*radios[k][i] # termino para el radio entre los eslabones 
        # Acumulacion de los terminos
        polinomios[k]+=termino
    #
    # Polinomio simplificado
    polisimple = sym.expand(polinomios[k])
    # Forma lamda del polinomio px, referencia x y el polinomio que se desea convertir
    px = sym.lambdify(x, polinomios[k])
    # Almacenamiento de la forma del polinomio
    PX.append(px) 
#
#_______________________________________________________________________
# Dimensionamiento por criterio de rectitud --> Evaluacion de polinomios en el punto beta = 55
#_______________________________________________________________________
# Para el radio delta_x / L2
p55_l2_r = PX[2](55) 
# Para el radio L1 / L2 
p55_l1_r = PX[0](55)
# Para el radio L3 / L2 
p55_l3_r = PX[1](55)
#_______________________________________________________________________
# Dimensionamiento por criterio de velocidad --> Evaluacion de polinomios en el punto beta = 55
#_______________________________________________________________________
# Para el radio delta_x / L2 
p55_l2_v = PX[5](55) 
# Para el radio L1 / L2 
p55_l1_v = PX[3](55)
# Para el radio L3 / L2 
p55_l3_v = PX[4](55)
#_______________________________________________________________________
# Salida
#_______________________________________________________________________
print('Dimensionamiento por criterio de rectitud')
print(' ')
L2_r = deltax/p55_l2_r
print('l2 = ')
print(L2_r)
L1_r = p55_l1_r*L2_r
print(' ')
print('l1 = ')
print(L1_r)
L3_r = p55_l3_r*L2_r
print(' ')
print('l3 = ')
print(L3_r)
print(' ')
print(' ')
print('Dimensionamiento por criterio de velocidad')
print(' ')
L2_v = deltax/p55_l2_v
print('l2 = ')
print(L2_v)
L1_v = p55_l1_v*L2_v
print(' ')
print('l1 = ')
print(L1_v)
L3_v = p55_l3_v*L2_v
print(' ')
print('l3 = ')
print(L3_v)