import numpy as np
import matplotlib.pyplot as plt
import math

def calculateAmplitude(fuerza, m, b, w, w0):
    numerador = fuerza/m
    denominador = pow(pow(w,2)-pow(w0,2),2)+pow(b*w/m,2)
    
    # halla mso el numerador entre la raiz del denominador
    result = numerador/math.sqrt(denominador)
    return result

     

def MAS():
    #A = float(input("Ingrese la amplitud: "))
    
    fuerza = float(input("Ingrese la fuerza: "))
    m = float(input("Ingrese la masa: "))
    b = float(input("Ingrese el coeficiente de amortiguamiento: "))
    w = float(input("Ingrese la velocidad angular: "))
    w0 = float(input("Ingrese la velocidad angular inicial: "))
    
    t_i = float(input("Ingrese el tiempo inicial: "))
    t_f = float(input("Ingrese el tiempo final: "))
    phi = float(input("Ingrese de la fase: "))  

    A = calculateAmplitude(fuerza, m, b, w, w0)
    print("La amplitud es: ", A)
    
    t_ = np.arange(t_i, t_f, 0.5)
    x_ = A*np.cos(np.radians(w*t_ + phi))
    velocidad_ = -A*w*np.sin(np.radians(w*t_+phi))
    

    fig, (ax1, ax2) = plt.subplots(1,2)
    fig.set_size_inches(12,5)
    ax1.plot(t_,x_)
    ax1.set_title("Posición")
    ax2.plot(t_,velocidad_)
    ax2.set_title("Velocidad")


    plt.show()

    velocidad_max = w*A
    print("La velocidad máxima es: ", velocidad_max, "m/s")
    
    aceleracion_max = pow(w,2)*A
    print("La aceleración máxima es: ", aceleracion_max, "m/s2")
    
MAS()