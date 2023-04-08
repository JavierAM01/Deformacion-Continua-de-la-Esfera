import numpy as np



def dif1(x, y, z, t):

    c = 1.0 / (1.0 - z*t)
    k = 2./np.pi*np.arctan(np.tan(np.pi*t/2.0)/20.) # [0,1] -> [0,1) de forma que se mantiene en 0 la mayoría del intervalo
    
    xt = x * c
    yt = y * c
    zt = z / (1-t*z) * (1-k) + (-1) * k

    return xt, yt, zt

def dif2(x, y, z, t):

    t1 = lambda x : np.pi/2. * x                    # X : [-1,1]       -> [pi/2, pi/2]
    t2 = lambda x : np.tan(x)                       # X : [pi/2, pi/2] -> (-infty, +infty)
    aux = lambda x, t : x * (1-t) + t2(t1(x)) * t   # X : [-1,1]       ~> [1, +infinito)*sign(x)     // el factor t lo hace progresivo

    xt = aux(x, t)
    yt = aux(y, t)
    k = 2./np.pi*np.arctan(np.tan(np.pi*t/2.0)/20.) # [0,1] -> [0,1) de forma que se mantiene en 0 la mayoría del intervalo
    zt = z / (1-t*z) * (1-k) + (-1) * k
    return xt, yt, zt

def dif3(x, y, z, t):

    t1 = lambda x : np.pi/2. * (x + 1) /2.          # X : [-1,1]    -> [0, pi/2]
    t2 = lambda x : 10*np.tan(x)                    # X : [0, pi/2] -> [0, +infty)
    aux = lambda x, t : 1 + t2(t1(x)) * t           # X : [-1,1]    ~> [1, +infinito)     // el factor t lo hace progresivo

    c = aux(z, t)
    xt = x * c
    yt = y * c
    k = 2./np.pi*np.arctan(np.tan(np.pi*t/2.0)/20.) # [0,1] -> [0,1) de forma que se mantiene en 0 la mayoría del intervalo
    zt = z / (1-t*z) * (1-k) + (-1) * k
    return xt, yt, zt

def dif4(x, y, z, t):
    xt = np.tan(np.arctan(x/z)) * t + x * (1-t)
    yt = np.tan(np.arctan(y/z)) * t + y * (1-t)
    zt = z * (1-t) + (-1) * t
    return xt, yt, zt

def dif5(x, y, z, t):
    c = 1.0 / (1.0 - z*t)
    xt = x * c
    yt = y * c
    zt = z * (1-t) + (-1) * t
    return xt, yt, zt

def dif6(x, y, z, t):
    c = np.tan(np.pi/2 * (1+z)/2 * t + np.arctan(1) * (1-t))
    c = np.tan(np.pi/2 * (1+z)/2 * t + np.arctan(1) * (1-t))
    xt = x * c
    yt = y * c
    zt = z * (1-t) + (-1) * t
    return xt, yt, zt


# def esfera2cilindro(x, y, z, t):
#     norma = np.sqrt(x**2 + y**2)
#     xt = x + (x/norma - x)*t
#     yt = y + (y/norma - y)*t
#     return xt, yt, z
