import quantities as pq
import re

# Solicita al usuario que ingrese la cadena con la magnitud
cadena = input("Ingrese un número con magnitud: ")

# Utiliza una expresión regular para separar la magnitud en el valor numérico y la unidad
# valor, unidad = re.findall(r'^(-?\d+(?:[\.]\d+)?)\s*(.*)$', cadena)[0]
valor, unidad = cadena.split(" ")
if(unidad == ""):
    unidad = "m"
    
print(f"Valor: {valor}, Unidad: {unidad}")
# Crea un objeto Quantity con el valor numérico y la unidad
qty = pq.Quantity(float(valor), unidad)

# Imprime la información del objeto Quantity
print(qty)
print("Unidad:", qty.units)
print("Magnitud:", qty.magnitude)
print("Dimensionalidad:", qty.dimensionality)
