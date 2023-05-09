# ingreso de la cadena
cadena = input(f"Ingrese t: ")

# tratamos de separa
try:
    valor, unidad = cadena.split(" ")
except:
    
    print(f"Valor inválido: {cadena}")
    

print(valor)
print(unidad)