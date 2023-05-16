import matplotlib.pyplot as plt

def calcular_fuerza(m, d, t, vi, vf):
    a = (vf - vi) / t
    F = m * a
    return F

# Datos del móvil
m = 1.0  # masa del móvil
d = 10.0  # distancia recorrida
t = 5.0  # tiempo transcurrido
vi = 2.0  # velocidad inicial
vf = 8.0  # velocidad final

# Cálculo de la fuerza
F = calcular_fuerza(m, d, t, vi, vf)

# Creación del gráfico
tiempo = [0, t]  # Lista de tiempos
velocidad = [vi, vf]  # Lista de velocidades
fuerza = [0, F]  # Lista de fuerzas

plt.figure()
plt.subplot(2, 1, 1)
plt.plot(tiempo, velocidad)
plt.xlabel('Tiempo')
plt.ylabel('Velocidad')
plt.title('Cambio de velocidad en el tiempo')

plt.subplot(2, 1, 2)
plt.plot(tiempo, fuerza)
plt.xlabel('Tiempo')
plt.ylabel('Fuerza')
plt.title('Fuerza en función del tiempo')

plt.tight_layout()
plt.show()
