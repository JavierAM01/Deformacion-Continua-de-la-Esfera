import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
# import os
# import cv2



################## funciones para la deformacion de la esfera ###################

f  = lambda z, t : 1.0 / (1.0 - z*t)
g2 = lambda z, t : z * (1.0 - t)

def g(z, t):
    n1, n2 = z.shape
    for i in range(n1):
        for j in range(n2):
            zi = z[i][j]
            z[i][j] = (zi * (1.0 - t)) if zi <= 0 else zi * (1 + np.sin(3*np.pi*t/2))
    return z

def difeo1(x, y, z, t):
    xt = x * f(z, t)
    yt = y * f(z, t)
    zt = g2(z, t)
    return xt, yt, zt

def cilindro(x, y, z, t):
    norma = np.sqrt(x**2 + y**2)
    xt = x + (x/norma - x)*t
    yt = y + (y/norma - y)*t
    return xt, yt, z

def clase(x, y, z, t):
    C = 1/((1-t) + abs(-1-z)*t)
    xt = C * x
    yt = C * y
    zt = -t + z*(1-t)
    return xt, yt, zt

def tangentes(x, y, z, t):
    pass

######################### proyecciones directa y continua #########################
proyeccion = lambda x, y, z : difeo1(x,y,z,1)

def difeomorfismo(x, y, z, t, function, sphere=True):
    if sphere:
        x, y, z = createSphere(t)
    x, y, z = function(x, y, z, t)
    return x, y, z

################ función para crear los puntos de la esfera en R^3 ################
def createSphere(t=0):
    theta = np.linspace(0, 2*np.pi, 50)
    phi   = np.linspace(0, np.pi-0.01-t*np.pi/5, 50)
    theta, phi = np.meshgrid(theta, phi)
    r = 1
    x = r * np.cos(theta) * np.sin(phi)
    y = r * np.sin(theta) * np.sin(phi)
    z = r * np.cos(phi)
    return x, y, z

def createEspiral():
    t = np.linspace(0,1,200)
    rho = 1*t
    theta = 6*2*np.pi*t
    x = rho * np.cos(theta)
    y = rho * np.sin(theta)
    z = np.sqrt(1.1 - x**2 - y**2)  # + 0.001 por errores de redondeo, para que la raíz no se negativa
    return x, y, z


####################### crear una animación #######################
def update(t, x0, y0, z0, ax):

    xt, yt, zt = difeomorfismo(x0, y0, z0, t, clase) # difeo1, cilindro, clase
    # x2t, y2t, z2t = difeomorfismo(x2, y2, z2, t, clase, sphere=False) # 
    ax.clear()
    ax.set(xlim3d=(-1,1), ylim3d=(-1,1), zlim3d=(-1,1))
    ax.plot_surface(xt, yt, zt, cmap=plt.cm.viridis) #.magma)
    # ax.plot(x2t, y2t, z2t, "k-", zorder=1)#cmap=plt.cm.magma)


def main():
    n_frames = 50
    x, y, z = createSphere()
    #x2, y2, z2 = createEspiral()

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.view_init(elev=15, azim=-45)

    _ = animation.FuncAnimation(fig, update, frames=np.linspace(0,1,n_frames), fargs=[x,y,x,ax], interval=100)
    plt.show()


if __name__ == "__main__":
    main()