import math


def inputData():
  global m, G, r
  continuar = ""
  while(True):
    try:
        l = float(input("Ingrese el momento angular (kg·m2/s) (7.046e33 'tierra'): "))
        m = float(input("Ingrese la masa reducida del planeta (Kg) (5.972e24 'tierra'): "))
        t = float(input("Ingrese el tiempo transcurrido (s): "))
        return l, m, t
    except ValueError:
      print("Valor incorrecto")
      continuar = input("\n'exit' para salir: ")
      
    if(continuar == "exit"):
      exit()


def calculeA(l, m, t):
    A = (l / (2 * m)) * t
    return A

def main():
    l, m, t = inputData()
    area = calculeA(l, m, t)
    areaKm = area*1e-6
    print("El área barrida por el planeta es:", round(areaKm,4) ,"km2")

if __name__ == "__main__":
    main()
