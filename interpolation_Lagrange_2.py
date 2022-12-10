# importamos la interpolación de Langrange del módulo de interpolación de Scipy
# importamos la librería Matplotlib con un alias
# importamos la librería Numpy con un alias
from scipy.interpolate import lagrange
import numpy as np
import matplotlib.pyplot as plt

# Guardamos los valores de x y f(x) a usar, en vectores.
x = [0,1,3,6]
y = [-3,0,5,7]

# Graficamos los valores a interpolar
plt.figure('1')
plt.plot(x,y,'x', mew=2, label='Datos')
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()

# Obtendremos el polinomio de Lagrange para los puntos dados
p = lagrange(x,y)

# Evaluaremos el polinomio obtenido, en un intervalo de [0,6]
x1 = np.linspace(0,6,100)
y1 = p(x1)

# Graficamos el polinomio obtenido, así como los puntos usados
plt.figure('2')
plt.plot(x1, y1, label='interpolacion')
plt.plot(x, y, 'x', mew=2, label='Datos')
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()

# Si queremos obtener valores de f(x), lo único que necesitamos hacer es evaluar el polinomio en el punto x, por ejemplo, para hallar f(x) cuando x=1.8
print(p(1.8))