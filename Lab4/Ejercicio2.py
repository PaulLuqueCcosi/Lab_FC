import math

# datos globales
m = None
G = 6.673*10**-11
r = None


def inputData():
  global m, G, r
  continuar = ""
  while(True):
    try:
      m = float(input("Ingrese la MASA del planeta (Kg)\nNOTA: puede usar notacion cientifica (por ejemplo, 5.972e24 kg): "))
      r = float(input("Ingrese el RADIO del planeta (km): "))
      r = r * 1000 # convetimos a metros
      break
    except ValueError:
      print("Valor incorrecto")
      continuar = input("\n'exit' para salir: ")
      
    if(continuar == "exit"):
      exit()
  
def calculeG(m, r):
  global G
  g = G*m/r**2
  return g

def calculeDesidad(m,r):
  global G
  g = calculeG(m,r)
  densidad = (3/4)*g / (math.pi*G*r)
  return densidad


def main():
  global m, r
  inputData()
  print("\n-----------DATOS-----------")
  print(f"MASA: {round(m,3)} kg")
  print(f"RADIO {round(r,3)} m")
  p = calculeDesidad(m, r)
  print(f"\nLa DENSIDAD es: {round(p, 4)} kg/m3")

if __name__ == "__main__":
  main()

