import quantities as pq

def getAceleracion(vf, unidad_vf, vi, unidad_vi, t, unidad_t, numeroDecimales=3):
    vfUnidades =  pq.Quantity(float(vf), unidad_vf)
    viUnidades =  pq.Quantity(float(vi), unidad_vi)
    tUnidades =  pq.Quantity(float(t), unidad_t)

    aceleracion = (vfUnidades - viUnidades) / tUnidades
    aceleracion = aceleracion.simplified
    aceleracion = pq.Quantity(round(float(aceleracion.magnitude), numeroDecimales),aceleracion.units)
    print(f"Aceleracion: {aceleracion}")
    return aceleracion

# def getAceleracion(vf, unidad_vf, vi, unidad_vi, t, unidad_t, masa, unidad_masa):
#     vfUnidades =  pq.Quantity(float(vf), unidad_vf)
#     viUnidades =  pq.Quantity(float(vi), unidad_vi)
#     tUnidades =  pq.Quantity(float(t), unidad_t)
#     masaUnidades =  pq.Quantity(float(masa), unidad_masa)

#     aceleracion = (vfUnidades - viUnidades) / tUnidades
#     aceleracion = aceleracion.simplified

#     fuerza = aceleracion/masa
#     print(aceleracion)
#     return aceleracion

if __name__ == "__main__":
    vf = input("Velocidad final: ")
    unidad_vf = input("Unidad de velocidad final: ")
    vi = input("Velocidad inicial: ")
    unidad_vi = input("Unidad de velocidad inicial: ")
    t = input("Tiempo: ")
    unidad_t = input("Unidad de tiempo: ")
    
    getAceleracion(vf, unidad_vf, vi, unidad_vi, t, unidad_t)