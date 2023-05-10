import quantities as pq

def hallarAceleracion(vf, unidad_vf, vi, unidad_vi, t, unidad_t, masa, unidad_masa):
    vfUnidades =  pq.Quantity(float(vf), unidad_vf)
    viUnidades =  pq.Quantity(float(vi), unidad_vi)
    tUnidades =  pq.Quantity(float(t), unidad_t)
    masaUnidades =  pq.Quantity(float(masa), unidad_masa)

    aceleracion = (vfUnidades - viUnidades) / tUnidades
    aceleracion = aceleracion.simplified

    fuerza = aceleracion/masa
    print(aceleracion)
    return aceleracion

