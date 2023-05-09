import numpy as np
import quantities as pq

# definimos una cantidad
cantidad = 2.345 * pq.m



# redondeamos la magnitud a 2 decimales utilizando la función around() de numpy
magnitud_redondeada = np.around(cantidad.magnitude, 2)

# creamos una nueva cantidad con la magnitud redondeada
cantidad_redondeada = magnitud_redondeada * cantidad.units

print(cantidad)
print(cantidad_redondeada)
