import utils



# tiempo = utils.evaluar_formula(utils.MRU["t"], {"distancia": d, "velocidad": v})

try:
    v = utils.evaluar_formula(utils.MRU["v"], {"distancia": d, "tiempo": t})
    print(v)
except ZeroDivisionError:
    print("El tiempo no puede ser 0")
except NameError:
    print("Las variables no se identifican")
    
except TypeError:
    print("El tipo de dato no es correcto")