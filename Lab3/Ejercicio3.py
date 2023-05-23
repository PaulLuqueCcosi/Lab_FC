import numpy as np
import matplotlib.pyplot as plt
import math

def diviseByZero(a,b):
    if b == 0:
        return "diviseByZero"
    return a/b

def calc_w(L,C):
    return diviseByZero(1,math.sqrt(L*C))

def graf(t,c,src):
    fig, (ax1) = plt.subplots(1)
    ax1.plot(t, c)
    title = "Carga ", src
    ax1.set_title(title)
    plt.show()

def CircuitoLC(Q,t0, tf,L,C,phi):
    # Q = float(Q)
    # t = float(t)
    # L = float(L)
    # C = float(C)
    # phi = float(phi)
    
    try:
        w = 1/(math.sqrt(L*C))
    except ZeroDivisionError:
        print("No se puede dividir por cero")
        return None
    
    
    t = tf - t0
    t_ = np.arange(t0,tf,0.5)
    q_ = Q*np.sin(w*t_+phi)
    return t_, q_


q0 = float(input("Ingrese la carga inicial: "))
ti = float(input("Ingrese el tiempo inicial: "))
tf = float(input("Ingrese el tiempo final: "))
l = float(input("Ingrese la inductancia: "))
c = float(input("Ingrese la capacitancia: "))
phi = float(input("Ingrese la fase: "))

t_, q_ = CircuitoLC(q0,ti,tf,l,c,phi)
graf(t_,q_,"LC")


def CircuitoLCR(Q,t,L,C,R,phi):
    Q = float(Q)
    t = float(t)
    L = float(L)
    C = float(C)
    phi = float(phi)
    w = calc_w(L,C)
    y =  diviseByZero(R,2*L)
    t= np.arange(0,t,0.5)
    src = "LCR"
    clcr = Q*np.exp(-y*t)*np.sin(w*t+phi)
    graf(t,clcr,src)
