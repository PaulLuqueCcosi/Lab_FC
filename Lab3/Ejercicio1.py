import numpy as np
import matplotlib.pyplot as plt


def MAS():
    A = float(input("Ingrese la amplitud: "))
    t_i = float(input("Ingrese el tiempo inicial: "))
    t_f = float(input("Ingrese el tiempo final: "))
    w = float(input("Ingrese la velocidad angular: "))
    phi = float(input("Ingrese de la fase: "))

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