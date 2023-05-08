import math
import quantities as pq



# definimos las formulas de MRU
MRU = {
    "v": {
        "distancia / tiempo":
            {
                "parametros": ["distancia", "tiempo"],
                "restricciones": {
                    "tiempo": ["tiempo > 0",],
                    "distancia": [],

                },
                "unidad": {
                    "distancia": "m",
                    "tiempo": "s",
                }
            },
    },


    "d": {
        "velocidad * tiempo":
            {
                "parametros": ["velocidad", "tiempo"],
                "restricciones": {
                    "tiempo": [],
                    "velocidad": [],
                },
                "unidad": {
                    "velocidad": "m/s",
                    "tiempo": "s",
                },
            },
    },
    "t": {
        "distancia / velocidad":
            {
                "parametros": ["distancia", "velocidad"],
                "restricciones": {
                    "velocidad": ["velocidad > 0",],
                    "distancia": [],
                },
                "unidad": {
                    "distancia": "m",
                    "velocidad": "m/s",
                },
            },
    },


}


# Definimos las formulas de MRUV

MRUV = {
    # OK
    "a": {
        "2 * (distancia - (velocidad_inicial * tiempo)) / math.pow(tiempo, 2)": {
            "parametros": ["distancia", "velocidad_inicial", "tiempo"],
            "restricciones": {
                "distancia": [],
                "velocidad_inicial": [],
                "tiempo": ["tiempo > 0",],
            },
        },

        "(velocidad_final - velocidad_inicial) / tiempo": {
            "parametros": ["velocidad_final", "velocidad_inicial", "tiempo"],
            "restricciones": {
                "velocidad_final": [],
                "velocidad_inicial": [],
                "tiempo": ["tiempo > 0",],
            },
        },


    },
    # OK
    "d": {
        "velocidad_inicial * tiempo + (aceleracion * math.pow(tiempo,2)) / 2":  {
            "parametros": ["velocidad_inicial", "tiempo", "aceleracion"],
            "restricciones": {
                "velocidad_inicial": [],
                "tiempo": [],
                "aceleracion": [],
            },
        },
    },
    # OK
    "t": {
        "(-velocidad_inicial + (math.pow(velocidad_inicial,2) + 2 * aceleracion * distancia) ** 0.5) / aceleracion": {

            "parametros": ["velocidad_inicial", "aceleracion", "distancia"],
            "restricciones": {
                "velocidad_inicial": [],
                "aceleracion": ["aceleracion > 0",],
                "distancia": [],
            },
        },




        "(velocidad_final - velocidad_inicial) / aceleracion":  {


            "parametros": ["velocidad_final", "velocidad_inicial", "aceleracion"],
            "restricciones": {
                "velocidad_final": [],
                "velocidad_inicial": [],
                "aceleracion": ["aceleracion > 0",],
            },
        },

    },
    # OK
    "v0": {

        "distancia/tiempo - (acelaracion * tiempo) / 2": {
            "parametros": ["distancia", "tiempo", "aceleracion"],
            "restricciones": {
                "distancia": [],
                "tiempo": ["tiempo > 0",],
                "aceleracion": [],
            },
        },


        "velocidad_final - (aceleracion * tiempo)":  {
            "parametros": ["velocidad_final", "aceleracion", "tiempo"],
            "restricciones": {
                "velocidad_final": [],
                "aceleracion": [],
                "tiempo": [],
            },
        },
    },
    # OK
    "vf": {
        "velocidad_inicial + (aceleracion * tiempo)": {
            "parametros": ["velocidad_inicial", "aceleracion", "tiempo"],
            "restricciones": {
                "velocidad_inicial": [],
                "aceleracion": [],
                "tiempo": [],
            },
        },
    },

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
dataSet = MRU if tipo == "MRU" else MRUV
print(f"Tipo: {tipo}")
print("--------------------")

# --------------------------------------------------------
while (True):

    print("Seleccione la variable que desea calcular: ")
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
        f"Seleccione segun los parametros que tiene para hallar '{variable}' :")

    for formula, dataFormula in (dataSet[variable].items()):\

        numeroFormulas += 1
        print(f"{numeroFormulas}. Parametros:")
        for parametro in dataFormula["parametros"]:
            print(f"\t- {parametro}", end="\t-> ")
            # IMPRIMIMO LAS RESTRICCIONES
            print(f"Restricciones: (", end="")
            for restriccion in dataFormula["restricciones"][parametro]:
                print(f" {restriccion},", end="")
            print(")")

    try:
        formulaIndice = int(input("Seleccione segun sus parametros: "))
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
    parametrosOK = True
    print("Ingrese los valores de los parametros: ")

    valores = {}
    for parametro in (dataSet[variable][formula]["parametros"]):
        if (not ok):
            break

        try:
            
            cadena = input(f"{parametro}: ")
            valor, unidad = cadena.split(" ")
            valores[parametro] = float(valor)
            unidad = pq.Quantity(1, unidad)

            
            # valores[parametro] = float(input(f"{parametro}: "))

        except ValueError:
            print("\nSolo ingrese numeros\n")
            ok = False
            continue

        # Comprombamos las restricciones
        for restriccion in dataSet[variable][formula]["restricciones"][parametro]:
            if not eval(restriccion.replace(parametro, str(valores[parametro]))):
                print(
                    f"\nLa restricción '{restriccion}' no se cumple para el valor de '{parametro}' = {valores[parametro]}.")
                parametrosOK = False
                valores.pop(parametro)
                break

        if (not parametrosOK):
            break

    if (not parametrosOK):
        continue

    break


print("--------------------")
print(f"Tipo: {tipo}")
print(f"Variable: {variable}")
print(f"Formula: {formula}")
print(f"Parametros: {valores}")
print("--------------------")

# calculamos el resultado
try:
    resultado = evaluar_formula(formula, valores)
except:
    print("\nNo se puede dividir entre 0\n")


print("--------------------")
print(f"Resultado: {variable} = {resultado}")
print("--------------------")
