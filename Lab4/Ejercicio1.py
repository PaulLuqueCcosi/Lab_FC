import numpy as np

# datos globales
m = None
G = 6.673*(10**-11)
r = None
g = None


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
  global G, g
  g = G*m/(r**2)
  return g

def test():
  # ejemplo de la tieraa
  m = 5.972 * (10**24) #5.972 x 10^24 kg
  r = 6371.0 * 1000 # 6371 km
  g = calculeG(m, r)
  print(f"Gravedad (m/s2): {round(g,4)} m/s2")

def main():
  inputData()
  print("\n-----------DATOS-----------")
  print(f"MASA: {round(m,3)} kg")
  print(f"RADIO {round(r,3)} km")
  g = calculeG(m, r)
  print(f"\nGRAVEDAD: {round(g,4)} m/s2")

if __name__ == "__main__":
  # test()
  main()
