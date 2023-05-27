
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
                "unidades": {
                    "distancia": "m",
                    "tiempo": "s",
                },
                "restriccion_formula": "",
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
                "unidades": {
                    "velocidad": "m/s",
                    "tiempo": "s",
                },
                "restriccion_formula": "",

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
                "unidades": {
                    "distancia": "m",
                    "velocidad": "m/s",
                },

                "restriccion_formula": "",

            },
    },


}


# Definimos las formulas de MRUV

MRUV = {
    # OK
    "a": {
        "2 * (distancia - (velocidad_inicial * tiempo)) / (tiempo*tiempo)": {
            "parametros": ["distancia", "velocidad_inicial", "tiempo"],
            "restricciones": {
                "distancia": [],
                "velocidad_inicial": [],
                "tiempo": ["tiempo > 0",],
            },
            "unidades": {
                "distancia": "m",
                "velocidad_inicial": "m/s",
                "tiempo": "s",
            },
            "restriccion_formula": "",
          

        },

        "(velocidad_final - velocidad_inicial) / tiempo": {
            "parametros": ["velocidad_final", "velocidad_inicial", "tiempo"],
            "restricciones": {
                "velocidad_final": [],
                "velocidad_inicial": [],
                "tiempo": ["tiempo > 0",],
            },
            "unidades": {
                "velocidad_final": "m/s",
                "velocidad_inicial": "m/s",
                "tiempo": "s",
            },
            "restriccion_formula": "",
        },


    },
    # OK
    "d": {
        "velocidad_inicial * tiempo + (aceleracion * (tiempo*tiempo)) / 2":  {
            "parametros": ["velocidad_inicial", "tiempo", "aceleracion"],
            "restricciones": {
                "velocidad_inicial": [],
                "tiempo": ["tiempo >= 0",],
                "aceleracion": [],
            },
            "unidades": {
                "velocidad_inicial": "m/s",
                "tiempo": "s",
                "aceleracion": "m/s**2",
            },
            "restriccion_formula": "",
        },
    },
    # TODO
    "t": {
        "(-velocidad_inicial + ((velocidad_inicial*velocidad_inicial) + 2 * aceleracion * distancia) ** 0.5) / aceleracion": {

            "parametros": ["velocidad_inicial", "aceleracion", "distancia"],
            "restricciones": {
                "velocidad_inicial": [],
                "aceleracion": ["aceleracion != 0", ],
                "distancia": [],
            },
            "unidades": {
                "velocidad_inicial": "m/s",
                "aceleracion": "m/s**2",
                "distancia": "m",
            },
            "restriccion_formula": "velocidad_inicial**2 + 2 * aceleracion * distancia >= 0"
        },

        "(velocidad_final - velocidad_inicial) / aceleracion":  {


            "parametros": ["velocidad_final", "velocidad_inicial", "aceleracion"],
            "restricciones": {
                "velocidad_final": [],
                "velocidad_inicial": [],
                "aceleracion": ["aceleracion != 0",],
            },
            "unidades": {
                "velocidad_final": "m/s",
                "velocidad_inicial": "m/s",
                "aceleracion": "m/s**2",
            },
            "restriccion_formula": ""
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
            "unidades": {
                "distancia": "m",
                "tiempo": "s",
                "aceleracion": "m/s**2",
            },
            "restriccion_formula": ""
        },


        "velocidad_final - (aceleracion * tiempo)":  {
            "parametros": ["velocidad_final", "aceleracion", "tiempo"],
            "restricciones": {
                "velocidad_final": [],
                "aceleracion": [],
                "tiempo": ["tiempo >= 0",],
            },
            "unidades": {
                "velocidad_final": "m/s",
                "aceleracion": "m/s**2",
                "tiempo": "s",
            },
            "restriccion_formula": ""
        },
    },
    # OK
    "vf": {
        "velocidad_inicial + (aceleracion * tiempo)": {
            "parametros": ["velocidad_inicial", "aceleracion", "tiempo"],
            "restricciones": {
                "velocidad_inicial": [],
                "aceleracion": [],
                "tiempo": ["tiempo >= 0",],
            },
            "unidades": {
                "velocidad_inicial": "m/s",
                "aceleracion": "m/s**2",
                "tiempo": "s",
            },
            "restriccion_formula": ""
        },
    },

}
