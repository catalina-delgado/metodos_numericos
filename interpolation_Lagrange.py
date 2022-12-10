# importamos la interpolación de Langrange del módulo de interpolación de Scipy
# from scipy.interpolate import lagrange
# importamos la librería Numpy con un alias, para hacer los cálculos
import numpy as np
# importamos la librería Sympy, para desarrollar la forma algebraica del polinomio
import sympy as sym
# importamos la librería Matplotlib con un alias, para graficas
import matplotlib.pyplot as plt

# Ingresamos los datos de prueba
xi = np.array([0, 0.2, 0.3, 0.4])
fi = np.array([1, 1.6, 1.7, 2.0])

# xi = np.array([1, 2, 3, 4, 6])
# fi = np.array([275000, 530000, 810000, 1155000, 1650000])

# Procedimiento
# Conocer cuantos elementos tiene xi 
n = len(xi)
# Asignamos un carácter X
x = sym.Symbol('x')
# Inicializamos el polinomio
polinomio = 0
# Desplazamos i dentro del rango
for i in range(0,n,1):
    # Para calcular el primer termino de la Langrage, es necesario calcular un numerador que se obtiene por multiplicaciones
    numerador = 1
    denominador = 1
    # El numerador debe recorrer todos los puntos del vector xi
    for j in range(0,n,1):
        if (i != j):
            numerador = numerador*(x-xi[j])
            denominador = denominador*(xi[i]-xi[j])
        # Calculamos los terminos de lagrange
        termino = (numerador/denominador)*fi[i]
    # Acumulamos los terminos
    polinomio = polinomio + termino
    
# Simplificamos la ecuación
polisimple = sym.expand(polinomio)

# Forma lamda del polinomio px, referencia x y el polinomio que se desea convertir
px = sym.lambdify(x, polinomio)

# Vectores para graficas
muestras = 100 # Numero cualquiera
a = np.min(xi)
b = np.max(xi)
p_xi = np.linspace(a,b,muestras)
pfi = px(p_xi)

# Salida
print('polinomio')
print(polinomio)
print(' ')
print('polinomio simplificado')
print(polisimple)

# Ejemplo con la librería lagrange
# p = lagrange(xi,fi)
# print('polinomio con lagrange')
# print(p)

# Grafica
plt.plot(xi,fi, 'o')
plt.plot(p_xi,pfi)
plt.show()

# print(' ')
# print('Evaluación del polinomio')
# print(px(5.5))