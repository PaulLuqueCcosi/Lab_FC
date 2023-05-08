import math


# definimos las formulas de MRU
MRU = {
    "v": {
        "distancia / tiempo": ["distancia", "tiempo"],
    },

    "d": {
        "velocidad * tiempo": ["velocidad", "tiempo"],
    },
    "t": {
        "distancia / velocidad": ["distancia", "velocidad"],
    },

}


# Definimos las formulas de MRUV

MRUV = {
    # OK
    "a": {
        "2 * (distancia - (velocidad_inicial * tiempo)) / math.pow(tiempo, 2)": ["distancia", "velocidad_inicial", "tiempo"],
        "(velocidad_final - velocidad_inicial) / tiempo": ["velocidad_final", "velocidad_inicial", "tiempo"],
    },
    # OK
    "d": {
        "velocidad_inicial * tiempo + (aceleracion * math.pow(tiempo,2)) / 2":  ["velocidad_inicial", "tiempo", "aceleracion"],
    },
    # OK
    "t": {
        "(-velocidad_inicial + (math.pow(velocidad_inicial,2) + 2 * aceleracion * distancia) ** 0.5) / aceleracion": ["velocidad_inicial", "aceleracion", "distancia"],
        "(velocidad_final - velocidad_inicial) / aceleracion":  ["velocidad_final", "velocidad_inicial", "aceleracion"],

    },
    # OK
    "v0": {

        "distancia/tiempo - (acelaracion * tiempo) / 2": ["distancia", "tiempo", "aceleracion"],
        "velocidad_final - (aceleracion * tiempo)":  ["velocidad_final", "aceleracion", "tiempo"],
    },
    # OK
    "vf": {
        "velocidad_inicial + (aceleracion * tiempo)": ["velocidad_inicial", "aceleracion", "tiempo"],
    },

    # "otro": {
    #     "una weba": ["depe1", "depe2", "depe3"],
    # },
}


def evaluar_formula(formula, valores):
    # Reemplazamos las variables en la fórmula por sus valores correspondientes
    for variable, valor in valores.items():
        formula = formula.replace(variable, str(valor))

    # Evaluamos la fórmula utilizando eval() y el módulo math
    try:
        resultado = eval(formula, {"__builtins__": None}, {"math": math})

    except:
        raise

    return resultado


# MENU DE SELECCION
while (True):
    print("Ingrese que tipo de problema quiere resolver: ")
    print("1. MRU")
    print("2. MRUV")
    try:
        tipo = int(input("Ingrese el número de la opción: "))
    except ValueError:
        print("\nSolo ingrese numeros\n")
        continue

    # verificamos
    if (tipo != 1 and tipo != 2):
        print(f"\nOpción {tipo} INVALIDA\n")
    else:
        break

print("--------------------")
tipo = ("MRU" if tipo == 1 else "MRUV")
print(f"Tipo: {tipo}")
print("--------------------")

#TODO MEJORAR
while (True):

    print("Seleccione la variable que desea calcular: ")
    numeroVariables = 0

    # MRU
    if (tipo == "MRU"):
        for variable in MRU.keys():
            numeroVariables += 1
            print(f"{numeroVariables}. {variable}")

    # MRUV
    else:
        for variable in MRUV.keys():
            numeroVariables += 1
            print(f"{numeroVariables}. {variable}")

    try:

        variable = int(input("Ingrese el una opción: "))
    except ValueError:
        print("\nSolo ingrese numeros\n")
        continue

    if (variable <= 0 or variable > numeroVariables):
        print(f"\nOpción {variable} inválida\n")
        continue

    break

print("--------------------")
# impirmimos el tipo y la variable
print(f"Tipo: {tipo}")
variable = list(MRU.keys())[
    variable - 1] if tipo == 'MRU' else list(MRUV.keys())[variable - 1]

print(f"Variable: {variable}")

print("--------------------")

# imrpimimos las lo que necesitamo para usar una formula posible

while (True):
    numeroFormulas = 0
    print(f"Seleccione segun los parametros que tiene para hallar '{variable}' :")

    for formula, parametros in (MRU[variable].items() if tipo == "MRU" else MRUV[variable].items()):
        numeroFormulas += 1
        print(f"{numeroFormulas}. Parametros:")
        for parametro in parametros:
            print(f"\t- {parametro}")

        print("", end="\n")

    try:
        formulaIndice = int(input("\nSeleccione segun sus parametros: "))
    except ValueError:
        print("\nSolo ingrese numeros\n")
        continue
    
    # print(f"Numero formula {numeroFormulas}")

    if (formulaIndice <= 0 or formulaIndice > numeroFormulas):
        print(f"\nOpción {formulaIndice} invalida\n")
        continue

    break


print("--------------------")
print(f"Tipo: {tipo}")

print(f"Variable: {variable}")
# imprimo la formula
formula = list(MRU[variable].keys())[
    formulaIndice - 1] if tipo == 'MRU' else list(MRUV[variable].keys())[formulaIndice - 1]

print(f"Formula: {formula}")
print("--------------------")


### AQUI EN ADELANTE SE RESUELVE EL PROBLEMA

print("Ingrese los valores de los parametros: ")

valores = {}
for parametro in (MRU[variable][formula] if tipo == "MRU" else MRUV[variable][formula]):
    try:
        valores[parametro] = float(input(f"{parametro}: "))
    except ValueError:
        print("\nSolo ingrese numeros\n")
        continue

print("--------------------")
print(f"Tipo: {tipo}")
print(f"Variable: {variable}")
print(f"Formula: {formula}")
print(f"Parametros: {valores}")
print("--------------------")

# calculamos el resultado
resultado = evaluar_formula(formula, valores)
print("--------------------")
print(f"Resultado: {variable} = {resultado}")
print("--------------------")
