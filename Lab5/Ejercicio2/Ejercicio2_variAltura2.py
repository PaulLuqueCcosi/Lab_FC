import matplotlib.pyplot as plt
import numpy as np

# Datos de ejemplo
densidad_fluido = 1000  # Densidad del agua en kg/m^3
velocidad_punto1 = 10  # Velocidad en el punto 1 en m/s
velocidad_punto2 = 12  # Velocidad en el punto 2 en m/s
altura_punto1 = 10  # Altura en el punto 1 en metros

## NOTA
# en este caso la velocidad 2 va ser constante, y solo variara la altura 2
# si la velocidad 2 es MAYOR que la velocidad 1, la altura para que sea la presion igual sera MENOR a altura 1
# si la velocidad 2 es MENOR que la velocidad 1, la altura para que sea la presion igual sera MAYOR a altura 1
# si la velocidad 2 es IGUAL que la velocidad 1, la altura para que sea la presion igual sera IGUAL a altura 1


def calcular_diferencia_presiones(densidad_fluido, velocidad_1, velocidad_2, altura_1, altura_2):
    gravedad = 9.8  # Aceleración debido a la gravedad en m/s^2
    # Calculamos la diferencia de presiones utilizando la ecuación de Bernoulli
    diferencia_presiones = 0.5 * densidad_fluido * ((velocidad_2 ** 2) - (velocidad_1 ** 2)) + (densidad_fluido * gravedad * (altura_2 - altura_1))
    return diferencia_presiones

def calcular_h2_diferenciaPresiones_0(velocidad_1, velocidad_2, altura_1):
    gravedad = 9.8
    h2 = (-0.5 * (velocidad_2**2 - velocidad_1**2)/gravedad) + altura_1
    return h2


# Rango de alturas para el punto 2
alturas = np.linspace(0, 20, 100)  # Genera 100 valores de altura desde 0 hasta 20

# Calcula la diferencia de presiones para cada altura
diferencias_presiones = []
for altura in alturas:
    diferencia = calcular_diferencia_presiones(densidad_fluido, velocidad_punto1, velocidad_punto2, altura_punto1, altura)
    diferencias_presiones.append(diferencia)

# Calcula la altura donde la diferencia de presiones es cero
altura2_difePresion0 = calcular_h2_diferenciaPresiones_0(velocidad_punto1, velocidad_punto2, altura_punto1)

# Imprime los resultados
print("Datos de ejemplo:")
print(f"Densidad del fluido: {densidad_fluido} kg/m^3")
print(f"Velocidad en el punto 1: {velocidad_punto1} m/s")
print(f"Velocidad en el punto 2: {velocidad_punto2} m/s")
print(f"Altura en el punto 1: {altura_punto1} m")
print(f"Altura 2 para que las presiones sean iguales: {altura2_difePresion0} m")
print("")

# Graficar
plt.plot(alturas, diferencias_presiones)
plt.xlabel('Altura (m)')
plt.ylabel('Diferencia de Presiones (Pa)')
plt.title('Diferencia de Presiones vs Altura')
plt.grid(True)
plt.show()
