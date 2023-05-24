import numpy as np
import matplotlib.pyplot as plt
import math


q0 = None
t_i = None
t_f = None
l = None
c = None
r = None
phi = None
w0 = None

w = None
y = None

isLC = False
isLCR = False
def IngresoDatos():
    global q0, t_i, t_f, l, c, r, phi, w0, isLC, isLCR
    while(True):
        print("Seleccione que Circuito desea resolver")
        print("[1] LC\t[2] LCR")
        
        option = input(":")
        
        if(option not in ["1", "2"]):
            print("Opcion no valida")
            continue
            
        if(option == "1") :
            print("LC")
            isLC = True
        else:
            print("LCR")
            isLCR = True
            
        
        print("\nIngrese los datos")
        try:
            
            q0 = float(input("Ingrese la CARGA INICIAL (C): "))
            t_i = float(input("Ingrese el TIMEPO INICIAL (s): "))
            t_f = float(input("Ingrese el TIEMPO FINAL (s): "))
            if(t_f <= t_i):
                print("El tiempo final debe ser mayor al tiempo inicial")
                continue
            
            l = float(input("Ingrese la INDUCTANCIA (H): "))
            c = float(input("Ingrese la CAPACITANCIA (F): "))
            
            if(isLCR):
                r = float(input("Ingrese la RESISTENCIA (Ω): "))
                w0 = float(input("Ingrese FRECUENCIA ANGULAR INICIAL (rad/s): "))
            
            phi = float(input("Ingrese la fase: "))

            break
        except ValueError:
            print("Ingrese valores válidos")
            continue

def calcular_w_LC(l, c):
    global w
    try:
        w = 1/math.sqrt(l*c)
    except ZeroDivisionError:
        print("No se puede ser 0 latencia o capacitancia")
    
    return w

def calcular_y_LCR(r, l):
    global y
    
    try:
        y = r/2*l
    except ZeroDivisionError:
        print("Latencia no puede ser 0")
    return y

def calcular_w_LCR(w0, y):
    global w
    w = w0**2 - y**2
    
    return w

def carga_LC(Q,t_i, t_f,L,C,phi):
    
    w = calcular_w_LC(L, C)
    if(w == None):
        return None, None
       
    t_ = np.arange(t_i,t_f,0.1)
    q_ = Q*np.sin(w*t_+phi)
    return t_, q_

def carga_LCR(Q,w0,t_i, t_f,L,C,R,phi):
    y = calcular_y_LCR(R, L)
    w = calcular_w_LCR(w0, y)
    
    t_ = np.arange(t_i,t_f,0.1)
    q_ = Q*np.exp(-y*t_)*np.sin(w*t_+phi)
    
    return t_, q_



def graficaresultados(t_, q_, titulo):
    fig, ax1 = plt.subplots( figsize=(8, 10))
    
    # Gráfico 
    ax1.plot(t_, q_, color='blue', label='Carga')
    ax1.axhline(0, color='black', linewidth=0.5, linestyle='dashed')  # Línea punteada del eje x
    
    ax1.set_ylabel("Carga (C)")
    ax1.set_xlabel("Tiempo (s)")
    ax1.set_title(titulo)
    ax1.legend()
     
    plt.tight_layout()  # Ajusta los espacios entre los subgráficos
    plt.show()


# inicio del progrma
IngresoDatos()
titulo = None
if(isLC):
    t_, q_ = carga_LC(q0, t_i, t_f, l, c, phi)
    titulo = "LC"
else:
    t_, q_ = carga_LCR(q0, w0, t_i, t_f, l, c, r, phi)
    titulo = "LCR"
graficaresultados(t_,q_, titulo)


