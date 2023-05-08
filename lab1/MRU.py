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
        "velocidad_inicial * tiempo + (aceleracion * math.pow(tiempo,2)) / 2":  ["velocidad_inicial", "timepo", "aceleracion"],
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
    "v": {
        "velocidad_inicial + (aceleracion * tiempo)": ["velocidad_inicial", "aceleracion", "tiempo"],
    },

}
