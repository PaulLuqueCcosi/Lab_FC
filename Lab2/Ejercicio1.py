import quantities as pq

def formulaAtwood(m1, unidad_m1, m2, unidad_m2, cantidadDecimales = 3):
    g = pq.Quantity(9.81, "m/s**2")

    m1ConUnidad = pq.Quantity(float(m1), unidad_m1)
    m2ConUnidad = pq.Quantity(float(m2), unidad_m2)


    aceleracion = g*((m2ConUnidad - m1ConUnidad)/(m1ConUnidad+m2ConUnidad))
    aceleracion = aceleracion.simplified
    aceleracion = pq.Quantity(round(float(aceleracion.magnitude), cantidadDecimales),aceleracion.units)

    print(f"aceleracion: {aceleracion}")
    
    #tension = g*(2 * m1ConUnidad * m2ConUnidad) / (m1ConUnidad + m2ConUnidad)
    tension = m1ConUnidad*aceleracion + m1ConUnidad*g
    tension = tension.simplified
    
    print(f"tension: {tension.magnitude} N")
    return aceleracion


while(True):

    m1 , unidadm1= input("m1 :").split()
    m2 , unidadm2= input("m2 :").split()
    formulaAtwood(m1, unidadm1, m2, unidadm2)
    if(input() == "exit"):
        break
    