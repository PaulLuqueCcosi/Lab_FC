import utils

d = 40
v = 5
t = 0

tiempo = utils.evaluar_formula(utils.MRU["t"], {"distancia": d, "velocidad": v})

try:
    v = utils.evaluar_formula(utils.MRU["v"], {"distancia": d, "tiempo": t})
    print(v)
except ZeroDivisionError:
    print("El tiempo no puede ser 0")
