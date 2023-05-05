import math


# definimos las formulas de MRU

MRU = {
    "v" : "distancia / tiempo",
    "d" : "velocidad * tiempo",
    "t" : "distancia / velocidad"
}


def evaluar_formula(formula, valores) :
    # Reemplazamos las variables en la fórmula por sus valores correspondientes
    for variable, valor in valores.items():
        formula = formula.replace(variable, str(valor))
    # Evaluamos la fórmula utilizando eval() y el módulo math
    try:
        resultado = eval(formula, {"__builtins__": None}, {"math": math})
    except ZeroDivisionError:
        raise ZeroDivisionError("Imposible dividir entre 0")
    
    return resultado