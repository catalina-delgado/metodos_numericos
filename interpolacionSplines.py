# importamos la interpolación InterpolatedUnivariateSpline del módulo de interpolación de Scipy
# importamos la librería Matplotlib con un alias
# importamos la librería Numpy con un alias
from scipy.interpolate import InterpolatedUnivariateSpline
import numpy as np
import matplotlib.pyplot as plt

# Guardamos en arreglos los puntos (x,y) a interpolar
x = [0.1, 0.2, 0.5, 1.0, 2.0, 5.0, 10.0]
y = [10.0, 5.0, 2.0, 1.0, 0.5, 0.2, 0.1]

# Hacemos la interpolación correspondiente
# El valor de k es el grado del polinomio deseado, en este caso usaremos k=3
f_interp = InterpolatedUnivariateSpline(x, y, k=3)

# Graficamos el polinomio obtenido
x1 = np.linspace(0.1, 10)
y_interp = f_interp(x1)
plt.plot(x, y, 'x', mew=3)
plt.plot(x1, y_interp)
plt.xlabel("X")
plt.ylabel("Y")
plt.show()