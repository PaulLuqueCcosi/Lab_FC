import math

K = 2.97e-19 #s2/m3

def inputData():
  global m, G, r
  continuar = ""
  while(True):
    try:
        r = float(input("Ingrese el semieje mayor (km) (1.496e8 'tierra'): "))
        r = r*1000 # km to m
        return r
    except ValueError:
      print("Valor incorrecto")
      continuar = input("\n'exit' para salir: ")
      
    if(continuar == "exit"):
      exit()

def calcularPeriodo(r):
  global K
  T = math.sqrt(K * r**3)
  return T

def main():
  r = inputData()
  periodo = calcularPeriodo(r)
  periodoDias = periodo / (24 * 60 * 60) # para los dias

  print(f"El periodo orbital del planeta es: {round(periodo,4)} s")
  print(f"El periodo orbital del planeta es: {round(periodoDias,4)} dias terrestres")

if __name__ == "__main__":
  main()
