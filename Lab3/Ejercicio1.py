import numpy as np
import matplotlib.pyplot as plt

A = None
t_i = None
t_f = None
w = None
phi = None

def MAS_posicion(A, t_i, t_f, w, phi):
    t_ = np.arange(t_i, t_f, 0.1)
    x_ = A*np.cos(w*t_ + phi)
    return t_, x_

def MAS_velocidad(A, t_i, t_f, w, phi):
    
    t_ = np.arange(t_i, t_f, 0.1)
    velocidad_ = -A*w*np.sin(w*t_+phi)
    return t_, velocidad_

def MAS_aceleracion(A, t_i, t_f, w, phi):
    t_ = np.arange(t_i, t_f, 0.1)
    aceleracion = -A*pow(w,2)*np.cos(w*t_+phi)    
    return t_, aceleracion
    
def printVelocidadMaxima(w, A):
    velocidad_max = w*A
    print("La velocidad máxima es: ", velocidad_max, "m/s")
    
def printAceleracionMaxima(w, A):
    aceleracion_max = pow(w,2)*A
    print("La aceleración máxima es: ", aceleracion_max, "m/s2")
   

def graficaresultados(t_, x_, velocidad_, aceleracion_):
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 10))
    
    # Gráfico de posición
    ax1.plot(t_, x_, color='blue', label='Posición')
    ax1.axhline(0, color='black', linewidth=0.5, linestyle='dashed')  # Línea punteada del eje x
    
    ax1.set_ylabel("Posición (m)")
    ax1.set_title("Posición")
    ax1.legend()
    
    # Gráfico de velocidad
    ax2.plot(t_, velocidad_, color='green', label='Velocidad')
    ax2.axhline(0, color='black', linewidth=0.5, linestyle='dashed')  # Línea punteada del eje x
    
    ax2.set_ylabel("Velocidad (m/s)")
    ax2.set_title("Velocidad")
    ax2.legend()
    
    # Gráfico de aceleración
    ax3.plot(t_, aceleracion_, color='red', label='Aceleración')
    ax3.axhline(0, color='black', linewidth=0.5, linestyle='dashed')  # Línea punteada del eje x
    
    ax3.set_xlabel("Tiempo (s)")
    ax3.set_ylabel("Aceleración (m/s²)")
    ax3.set_title("Aceleración")
    ax3.legend()
    
    plt.tight_layout()  # Ajusta los espacios entre los subgráficos
    plt.show()


def IngresoDatos():
    global A, t_i, t_f, w, phi
    while(True):
        print("\nIngrese los datos de la onda MAS")
        try:
            A = float(input("Ingrese la AMPLITUD (m): "))
            t_i = float(input("Ingrese el TIEMPO inicial (s): "))
            t_f = float(input("Ingrese el TIEMPO final (s): "))
            if(t_f <= t_i):
                print("El tiempo final debe ser mayor al tiempo inicial")
                continue
            w = float(input("Ingrese la VELOCIDAD ANGULAR (rad/s): "))
            phi = float(input("Ingrese de la FASE (rad): "))
            break
        except ValueError:
            print("Ingrese valores válidos")
            continue
        
# Inicio del programa-----------------------
IngresoDatos()
t_, x_ = MAS_posicion(A, t_i, t_f, w, phi)
t_, velocidad_ = MAS_velocidad(A, t_i, t_f, w, phi)
t_, aceleracion_ = MAS_aceleracion(A, t_i, t_f, w, phi)
printVelocidadMaxima(w, A)
printAceleracionMaxima(w, A)
graficaresultados(t_, x_, velocidad_, aceleracion_)

