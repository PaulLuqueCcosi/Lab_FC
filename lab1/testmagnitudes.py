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
        valor = str(valor)
        unidad = unidades[variable]
        valorParaReemplazar = f"pq.Quantity({valor}, '{unidad}')"
        formula = formula.replace(variable, valorParaReemplazar)

    # Evaluamos la fórmula utilizando eval() y el módulo mat
    try:
        print(formula)
        resultado = eval(formula, {"__builtins__": None}, {"math": math, "pq":pq})

    except:
        raise

    return resultado

formula = "distancia / velocidad"
valores = {'distancia': 10, 'velocidad': 5}
unidades = {
    "distancia": "m",
    "velocidad": "m/s",
}


resultado = evaluar_formula(formula, valores, unidades)

print(f"result: {resultado}")