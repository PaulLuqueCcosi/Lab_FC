import utils
def elegir_formula(opcion):
    if opcion == 'MRU':
        print('Seleccione la fórmula deseada:')
        for key, value in utils.MRU.items():
            print(f'{key}: {value}')
        formula = input()
    elif opcion == 'MRUV':
        print('Seleccione la variable que desea calcular:')
        for key in utils.MRUV.keys():
            print(key)
        variable = input()
        print('Seleccione la fórmula deseada:')
        for index, formula in enumerate(utils.MRUV[variable]):
            print(f'{index+1}: {formula}')
        formula_index = int(input()) - 1
        formula = utils.MRUV[variable][formula_index]
    else:
        print('Opción inválida')
        return None
    return formula

def menu():
    # Imprimir opciones de fórmulas
    print("¿Qué desea hallar?")
    print("1. Velocidad (MRU)")
    print("2. Distancia (MRU)")
    print("3. Tiempo (MRU)")
    print("4. Aceleración (MRUV)")
    print("5. Velocidad final (MRUV)")
    print("6. Velocidad inicial (MRUV)")
    print("7. Tiempo (MRUV)")
    print("8. Distancia (MRUV)")

    opcion = input("Ingrese el número correspondiente a la opción que desea: ")

    if opcion == "1":
        formula = elegir_formula('MRU')
        variable1 = "distancia"
        variable2 = "tiempo"
    elif opcion == "2":
        formula = utils.MRU["d"]
        variable1 = "velocidad"
        variable2 = "tiempo"
    elif opcion == "3":
        formula = utils.MRU["t"]
        variable1 = "distancia"
        variable2 = "velocidad"
    elif opcion == "4":
        formula = utils.MRUV["a"][0]
        variable1 = "velocidad_inicial"
        variable2 = "velocidad_final"
        variable3 = "tiempo"
        variable4 = "distancia"
    elif opcion == "5":
        formula = utils.MRUV["v"][1]
        variable1 = "velocidad_inicial"
        variable2 = "a"
        variable3 = "distancia"
    elif opcion == "6":
        formula = utils.MRUV["v0"][1]
        variable1 = "velocidad_final"
        variable2 = "a"
        variable3 = "tiempo"
        variable4 = "distancia"
    elif opcion == "7":
        formula = utils.MRUV["t"][0]
        variable1 = "velocidad_inicial"
        variable2 = "a"
        variable3 = "distancia"
    elif opcion == "8":
        formula = utils.MRUV["d"][0]
        variable1 = "velocidad_inicial"
        variable2 = "tiempo"
        variable3 = "a"

    # Solicitar valores de variables necesarias para la fórmula
    valores = {}
    valores[variable1] = float(input(f"Ingrese el valor de {variable1}: "))
    if "variable2" in locals():
        valores[variable2] = float(input(f"Ingrese el valor de {variable2}: "))
    if "variable3" in locals():
        valores[variable3] = float(input(f"Ingrese el valor de {variable3}: "))
    if "variable4" in locals():
        valores[variable4] = float(input(f"Ingrese el valor de {variable4}: "))

    # Evaluar la fórmula con los valores ingresados
    resultado = utils.evaluar_formula(formula, valores)

    # Imprimir el resultado
    print(f"El resultado es: {resultado}")


menu()