import quantities as pq

UNIDADES_MASA = ["kg", "g", "lb", "oz"]

def ingresoMasa(countMasa):
    unidad = "kg"
    ## Ingresamos los datos 
    ingreso = input(f"Ingrese el dato de m{countMasa} (kg): ")
    
    if(ingreso == ""):
        print(f"[ERROR]: No ingreso ningun dato.", end="\n\n")
        return ingresoMasa(countMasa)
    
    # verificamos si solo se ingreso un numero
    ingreso = ingreso.replace(",", ".")
       
    try: 
        dato = float(ingreso)
    except:
        try:
            # Separamos el dato de la unidad
            dato, unidad = ingreso.split()
        except:
            print("[ERROR]: Ingrese el dato con el formato: '<numero> <unidad>'", end="\n\n")
            return ingresoMasa(countMasa)
            
        try:
            ## verificamos que el dato sea un numero
            dato = float(dato)
        except:
                ## Si no es un numero, volvemos a pedir el dato
            print(f"[ERROR]: El dato: '{dato}' no es un numero.", end="\n\n")
            return ingresoMasa(countMasa)
            
        # Verificamos que la unidad sea valida
        if(unidad not in UNIDADES_MASA):
            # Indicamos que la unidad no es valida y volvemos a pedir el dato
            print(f"[ERROR]: La unidad: '{unidad}' no es valida.", end="\n\n")
            return ingresoMasa(countMasa)
        
    return dato, unidad
        
    

def formulaAtwood(m1, unidad_m1, m2, unidad_m2, cantidadDecimales = 3):
    g = pq.Quantity(9.81, "m/s**2")

    m1ConUnidad = pq.Quantity(float(m1), unidad_m1)
    m2ConUnidad = pq.Quantity(float(m2), unidad_m2)


    aceleracion = g*((m2ConUnidad - m1ConUnidad)/(m1ConUnidad+m2ConUnidad))
    aceleracion = aceleracion.simplified
    aceleracion = pq.Quantity(round(float(aceleracion.magnitude), cantidadDecimales),aceleracion.units)

    print(f"ACELERACION (punto de referencia m1): {aceleracion}")
    
    #tension = g*(2 * m1ConUnidad * m2ConUnidad) / (m1ConUnidad + m2ConUnidad)
    tension = m1ConUnidad*aceleracion + m1ConUnidad*g
    tension = tension.simplified
    tension = pq.Quantity(round(float(tension.magnitude), cantidadDecimales),tension.units)
    
    print(f"TENSION: {tension.magnitude} N")
    return aceleracion


if __name__ == "__main__":
    # 
    print("MAQUINA DE ATWOOD")
    print(f"---------------------------------")
    print(f"Ingrese los datos de las masas ")
    print("Si no ingresa la unidad, se asumira que es en kg")
    print(f"---------------------------------")
    nuemero1, unidad1 = ingresoMasa(1)
    print(f"m1: {nuemero1} {unidad1}")

    print("\n")

    nuemero2, unidad2 = ingresoMasa(2)
    print(f"m2: {nuemero2} {unidad2}")
    print(f"-----------CALCULANDO-----------------")
    formulaAtwood(nuemero1, unidad1, nuemero2, unidad2)