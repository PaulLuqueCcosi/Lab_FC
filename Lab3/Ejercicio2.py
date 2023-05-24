import numpy as np
import matplotlib.pyplot as plt
import math

A = None

fuerza = None
m = None
b = None
w = None
w0 = None

t_i = None
t_f = None
phi = None


def IngresoDatos():
    global A, fuerza, m, b, w, w0, t_i, t_f, phi
    while(True):
        print("\nIngrese los datos de la onda Oscilacion forzada")
        try:
            fuerza = float(input("Ingrese la FUERZA (N): "))
            m = float(input("Ingrese la MASA (kg): "))
            if(m <= 0):
                print("La MASA tiene que ser positiva")
                continue
            
            b = float(input("Ingrese el COEFICIENTE DE AMORTIGUAMIENTO: "))
            w = float(input("Ingrese la VELOCIDAD ANGULAR (rad/s): "))
            w0 = float(input("Ingrese la VELOCIDAD ANGULAR NATURAL (rad/s): "))
            
            t_i = float(input("Ingrese el TIEMPO INICIAL (s): "))
            t_f = float(input("Ingrese el TIEMPO FINAL (s): "))
            if(t_f <= t_i):
                print("El tiempo final debe ser mayor al tiempo inicial")
                continue
            
            phi = float(input("Ingrese de la FASE (rad): "))
            break
        except ValueError:
            print("Ingrese valores válidos")
            continue

def calculateAmplitud(fuerza, m, b, w, w0):
    global A
    numerador = fuerza/m
    denominador = pow(pow(w,2)-pow(w0,2),2)+pow(b*w/m,2)
    
    # halla mso el numerador entre la raiz del denominador
    A = numerador/math.sqrt(denominador)
    print(f"Amplitud : {A} m")
    return A

def posicion_forzada(fuerza, m, b,w, w0, t_i, t_f, phi):
    A = calculateAmplitud(fuerza, m, b, w, w0)
    t_ = np.arange(t_i, t_f, 0.1)
    x_ = A*np.cos(w*t_ + phi)
    return t_, x_

def graficaresultados(t_, x_):
    fig, ax1 = plt.subplots( figsize=(8, 10))
    
    # Gráfico de posición
    ax1.plot(t_, x_, color='blue', label='Posición')
    ax1.axhline(0, color='black', linewidth=0.5, linestyle='dashed')  # Línea punteada del eje x
    
    ax1.set_ylabel("Posición (m)")
    ax1.set_xlabel("Tiempo (s)")
    ax1.set_title("Posición")
    ax1.legend()
     
    plt.tight_layout()  # Ajusta los espacios entre los subgráficos
    plt.show()


# Inicio del programa-----------------------
IngresoDatos()
t_, x_ = posicion_forzada(fuerza, m, b, w, w0, t_i, t_f, phi)
graficaresultados(t_, x_)
