# MRU


def distancia(v, unidadV,t, unidadT):
  
   #TODO: mejorar la unidad
   return [(v*t), f"m"]
  


def velocidad(d, unidadD, t, unidadT):
   try:
       velocidad = d/t
   except ZeroDivisionError:
       return "Imposible dividir entre 0"
  
   return [(velocidad), f"{unidadD}/{unidadT}"]




def tiempo(d, unidadD, v, unidadV):
   try:
       tiempo = d/v
   except ZeroDivisionError:
       return "Imposible dividir entre 0"
  
   # TODO: mejorar la unidades
   return [(tiempo), f"s"]




# RRUV


def distaciaV(vi, unidadVi, t, unidadT, a, unidadA):
   distancia = vi * tiempo + (a * (t**2))/2
  
   return [(distacia), f"m/s2"]






test = distaciaV(5,"m",1, "s", 2, "m/s2")
print(test)






