def calcular_diferencia_presiones(densidad_flujo, v1, v2, h1, h2):
    gravedad = 9.8  # Aceleración debido a la gravedad en m/s^2
    # Calculamos la diferencia de presiones utilizando la ecuación de Bernoulli
    diferencia_presiones = 0.5 * densidad_flujo * ((v2 ** 2) - (v1 ** 2)) + (densidad_flujo * gravedad * (h2 - h1))
    return diferencia_presiones


# Ejemplo de uso
densidad_fluido = 1000  # Densidad del agua en kg/m^3
velocidad_punto1 = 10  # Velocidad en el punto 1 en m/s
velocidad_punto2 = 5  # Velocidad en el punto 2 en m/s
altura_punto1 = 10  # Altura en el punto 1 en metros
altura_punto2 = 5  # Altura en el punto 2 en metros

diferencia = calcular_diferencia_presiones(densidad_fluido, velocidad_punto1, velocidad_punto2, altura_punto1, altura_punto2)
print("La diferencia de presiones entre los dos puntos es:", diferencia , "Pa")
