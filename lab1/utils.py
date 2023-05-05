import math


# definimos las formulas de MRU

MRU = {
    "v" : "distancia / tiempo",
    "d" : "velocidad * tiempo",
    "t" : "distancia / velocidad"
}

# Definimos las formulas de MRUV

MRUV = {
    "a": [
        "2 * (distancia - velocidad_inicial * tiempo) / tiempo**2",
        "(velocidad_final - velocidad_inicial) / tiempo",
        "(velocidad_final**2 - velocidad_inicial**2) / (2 * distancia)"
    ],
    "d": [
        "velocidad_inicial * tiempo + 1/2 * a * tiempo**2",
        "(velocidad_final**2 - velocidad_inicial**2) / (2 * a)",
        "velocidad_promedio * tiempo",
        "velocidad_inicial * tiempo + 1/2 * (velocidad_final - velocidad_inicial) * tiempo"
    ],
    "t": [
        "(-velocidad_inicial + (velocidad_inicial**2 + 2 * a * distancia)**0.5) / a",  # solución positiva de la ecuación de segundo grado
        "(velocidad_final - velocidad_inicial) / a",
        "2 * distancia / (velocidad_final + velocidad_inicial)",
        "distancia / velocidad_promedio"
    ],
    "v0": [
        "(distancia - 1/2 * a * tiempo**2) / tiempo",
        "velocidad_final - a * tiempo",
        "(2 * distancia / tiempo) - velocidad_final"
    ],
    "v": [
        "velocidad_inicial + a * tiempo",
        "(velocidad_inicial**2 + 2 * a * distancia)**0.5",
        "(2 * distancia / tiempo) - velocidad_inicial"
    ],
    
}



def evaluar_formula(formula, valores) :
    # Reemplazamos las variables en la fórmula por sus valores correspondientes
    for variable, valor in valores.items():
        formula = formula.replace(variable, str(valor))
        
    # Evaluamos la fórmula utilizando eval() y el módulo math
    try:
        resultado = eval(formula, {"__builtins__": None}, {"math": math})
    
    except:
        raise
    
    return resultado