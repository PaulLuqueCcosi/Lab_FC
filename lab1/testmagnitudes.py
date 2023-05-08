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

def evaluar_formula(formula, valores, unidades):
    # Reemplazamos las variables en la fórmula por sus valores correspondientes
    for variable, valor in valores.items():
        formula = formula.replace(variable, str(pq.Quantity(float(valor), unidades[variable])))


    # Evaluamos la fórmula utilizando eval() y el módulo math
    

    try:
        resultado = eval(formula, {"__builtins__": None}, {"math": math})

    except:
        raise

    return resultado


formula = MRU['v']['distancia / tiempo']
valores = {'distancia': 10, 'tiempo': 5}
unidades = {
    "distancia": "m",
    "velocidad": "m/s",
},

resultado = evaluar_formula(formula, valores, unidades)
