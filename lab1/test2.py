import utils
# Datos de prueba para MRU
mruprueba1 = {"distancia": 10, "tiempo": 5}
mruprueba2 = {"distancia": 20, "velocidad": 5}
mruprueba3 = {"velocidad": 10, "tiempo": 2}

# Datos de prueba para MRUV
mruvprueba1 = {"distancia": 10, "velocidad_inicial": 0, "velocidad_final": 20, "tiempo": 2}
mruvprueba2 = {"distancia": 50, "velocidad_inicial": 10, "a": 5}
mruvprueba3 = {"velocidad_inicial": 5, "velocidad_final": 15, "distancia": 100}

# Ejemplo de uso de evaluar_formula con MRU
formula = utils.MRU["v"]
resultado = utils.evaluar_formula(formula, mruprueba1)
print(resultado)  # Output: 2.0

# Ejemplo de uso de evaluar_formula con MRUV
formula = utils.MRUV["a"][0]
resultado = utils.evaluar_formula(formula, mruvprueba1)
print(resultado)  # Output: 5.0
