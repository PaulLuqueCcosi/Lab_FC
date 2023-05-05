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
        newFormula = formula.replace(variable, str(valor))
        # verificamos si se hizo la sustitucion
        if(formula == newFormula ):
            raise NameError("Las variables no se identifican")
        formula = newFormula
        
    # Evaluamos la fórmula utilizando eval() y el módulo math
    try:
        resultado = eval(formula, {"__builtins__": None}, {"math": math})
    except SyntaxError:
        raise TypeError("El tipo de dato no es correcto")

    except:
        raise
    
    return resultado