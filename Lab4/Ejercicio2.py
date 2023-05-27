import numpy as np
import math

# datos globales
m = None
G = 6.673*10**-11
r = None
g = None


def inputData():
  global m, G, r
  m = float(input("Ingrese la MASA del planeta (kg): "))
  r = float(input("Ingrese el RADIO del planeta (m), puede ingresar en km: "))
  

def calculeG(m, r):
  global G, g
  g = G*m/r**2
  print(f"Gravedad (m/s2): {g}")
  return g

def calculeDesidad(m,r):
  global G
  g = calculeG(m,r)
  densidad = (3/4)*g / (math.pi*G*r)
  print(f"La DENSIDAD es: {densidad} kg/m3")
  
  return densidad

# ejemplo
r = 6371.0 * 1000
m = 5.972 * 10**24




calculeDesidad(m, r)
