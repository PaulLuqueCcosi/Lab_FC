import math
MRU = {
    "v": {
        "distancia / tiempo":
            {
                "parametros": ["distancia", "tiempo"],
                "restricciones": {
                    "tiempo": ["tiempo > 0",],
                }
            },
    },

    "d": {
        "velocidad * tiempo":
            {
                "parametros": ["velocidad", "tiempo"],
                "restricciones": {
                    "tiempo": ["tiempo > 0",],
                }
            },
    },
    "t": {
        "distancia / velocidad":
            {
                "parametros": ["distancia", "velocidad"],
                "restricciones": {
                    "velocidad": ["velocidad > 0",],
                }
            },
    },


}


def evaluar_formula(formula, valores, restricciones):
    # Reemplazamos las variables en la fórmula por sus valores correspondientes
    for variable, valor in valores.items():
        formula = formula.replace(variable, str(valor))

    # Evaluamos las restricciones antes de evaluar la fórmula
    for variable, restricciones in restricciones.items():
        for restriccion in restricciones:
            valor = valores.get(variable)
            if valor is not None:
                if not eval(restriccion.replace(variable, str(valor))):
                    raise ValueError(
                        f"La restricción '{restriccion}' no se cumple para el valor de '{variable}' = {valor}.")

    # Evaluamos la fórmula utilizando eval() y el módulo math
    try:
        resultado = eval(formula, {"__builtins__": None}, {"math": math})
    except:
        raise

    return resultado


# Definimos una fórmula de MRU
formula_mru = "distancia / tiempo"

# Definimos los valores de las variables
valores_mru = {
    "distancia": 50,
    "tiempo": -12,
}

# Definimos las restricciones
restricciones_mru = {
    "distancia": ["distancia >= 0",],
    "tiempo": ["tiempo > -10",],
}

# Evaluamos la fórmula con las restricciones
resultado_mru = evaluar_formula(formula_mru, valores_mru, restricciones_mru)

# Imprimimos el resultado
print("El resultado es:", resultado_mru)
