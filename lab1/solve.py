import math
import quantities as pq
import DATA


def separar_magnitud(cadena):
    num = ''
    magnitud = ''
    for caracter in cadena:
        if caracter.isdigit() or caracter == '.' or caracter == '-':
            num += caracter
        else:
            magnitud += caracter

    try:
        num = float(num)
    except:
        print(f"\nERROR: '{num}' no es un número válido")
        return None, None

    # verificamos que la unidad sea valida
    try:
        extra = pq.Quantity(num, magnitud)
    except:
        print(f"\nERROR: '{magnitud}' no es una magnitud válida")
        return None, None

    # if magnitud != "" and (magnitud.strip() not in dir(pq.units)):
    #     print(f"\nERROR: '{magnitud.strip()}' no es una magnitud válida")
    #     return None, None

    return num, magnitud.strip()


def evaluar_formula(formula, valores, unidades):
    # Reemplazamos las variables en la fórmula por sus valores correspondientes
    for variable, valor in valores.items():
        # valor en numero
        valor = str(valor)
        # la unidad con la que se va a trabajar
        unidad = unidades[variable]
        # lo que vamos a reemplazar en la formula
        valorParaReemplazar = f"pq.Quantity({valor}, '{unidad}')"
        # Reemplazamos en la formula
        formula = formula.replace(variable, valorParaReemplazar)

    # Evaluamos la fórmula utilizando eval() y el módulo mat
    try:
        # agregamos pq y math
        resultado = eval(formula, {"__builtins__": None}, {
                         "math": math, "pq": pq})

        # Ahora simplificamos el resultado
        resultado = resultado.simplified
    except:
        print("Error al evaluar la formula")

    return resultado


# MENU DE SELECCION ------------------------------------
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
dataSet = DATA.MRU if tipo == "MRU" else DATA.MRUV
print(f"Tipo: {tipo}")
print("--------------------")

# --------------------------------------------------------
while (True):

    print("Seleccione el NUMERO de la variable que desea calcular: ")
    numeroVariables = 0

    for variable in dataSet.keys():
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
variable = list(dataSet.keys())[variable - 1]

print(f"Variable: {variable}")

print("--------------------")

# imrpimimos las lo que necesitamo para usar una formula posible --------------------

while (True):
    numeroFormulas = 0
    print(
        f"Seleccione el NUMERO de la opcion que desea hallar '{variable}' :")

    for formula, dataFormula in (dataSet[variable].items()):\

        numeroFormulas += 1
        print(f"{numeroFormulas}. :")
        for parametro in dataFormula["parametros"]:
            print(f"\t- {parametro}", end=" \t -> ")
            # IMPRIMIMO LAS RESTRICCIONES
            print(f"Restricciones: (", end="")
            for restriccion in dataFormula["restricciones"][parametro]:
                print(f" {restriccion},", end="")
            print(")")

    try:
        formulaIndice = int(input("Seleccione una opcion: "))
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
formula = list(dataSet[variable].keys())[formulaIndice - 1]

print(f"Formula: {formula}")
print("--------------------")

# INGRESO DE PARAMETROS ------------------------------------
while (True):
    ok = True

    print("\nIngrese los valores de los parametros: ")
    print("PUEDE INGRESAR CON DIFERENTE UNIDAD ('10 km', '10 h', etc)")
    print("SI SOLO INGRESA EL NUMERO, SE TOMARA LA UNIDAD POR DEFECTO")

    valores = {}
    unidades = dataSet[variable][formula]["unidades"]

    # Ingreso del parametro
    for parametro in (dataSet[variable][formula]["parametros"]):

        cadena = input(f"\n{parametro} ({unidades[parametro]}): ")

        # ingreso de la cadena
        valor, unidad = separar_magnitud(cadena)

        # verificamos que no sea None
        if (valor == None or unidad == None):
            ok = False
            break

        # Comprombamos las restricciones
        for restriccion in dataSet[variable][formula]["restricciones"][parametro]:
            if not eval(restriccion.replace(parametro, str(valor))):
                print(
                    f"\nLa restricción '{restriccion}' no se cumple para el valor de '{parametro}' = {valores[parametro]}.")
                ok = False
                continue

        if (ok):
            # llenamos los valores
            valores[parametro] = valor
            if (unidad != ""):
                unidades[parametro] = unidad

    if (ok):
        # salimos del infinito
        break


print("--------------------")
print(f"Tipo: {tipo}")
print(f"Variable: {variable}")
print(f"Formula: {formula}")
print(f"Parametros: {valores}")
print(f"Unidades: {unidades}")
print("--------------------")

# calculamos el resultado
try:
    resultado = evaluar_formula(formula, valores, unidades)
except:
    print("\nNo se puede dividir entre 0\n")


print("--------------------")
print(f"Resultado: {variable} = {resultado}")
print("--------------------")
