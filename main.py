import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import time

from difeomorfismos import *


################ función para crear los puntos de la esfera en R^3 ################
def createSphere(t=0):
    theta = np.linspace(0, 2*np.pi, 50)
    phi   = np.linspace(0+0.001, np.pi, 50) # -t*np.pi/5
    theta, phi = np.meshgrid(theta, phi)
    r = 1
    x = r * np.cos(theta) * np.sin(phi)
    y = r * np.sin(theta) * np.sin(phi)
    z = r * np.cos(phi)
    return x, y, z

def createEspiral():
    t = np.linspace(0,1,1000)
    rho = 1*t
    theta = 6*2*np.pi*t
    x = rho * np.cos(theta)
    y = rho * np.sin(theta)
    z = np.sqrt(1.01 - x**2 - y**2)  # + 0.01 por errores de redondeo, para que la raíz no se negativa
    return x, y, z


####################### crear una animación #######################
def update(t, x0, y0, z0, x02, y02, z02, ax, dif):

    if t == 0: time.sleep(1) # para observar la figura plana cuando llegue al final de la proyección

    xt, yt, zt = dif(x0, y0, z0, t) 
    # x2t, y2t, z2t = difeomorfismo(x02, y02, z02, t, clase)

    # settings
    ax.clear()
    ax.set(xlim3d=(-1,1), ylim3d=(-1,1), zlim3d=(-1,1))
    ax.set(xticks=[-1,1], yticks=[-1,1], zticks=[-1,1])
    ax.set_title("Deformación continua de la esfera")

    # Crear filtro:
    # quedarnos solo con los puntos menores a X radio 
    # (teniendo en cuenta que la proyección lleva puntos al infinito, acotamos de alguna manera el dibujo) 
    filter = np.apply_along_axis(all, 1, (xt**2 + yt**2 + zt**2 < 4**2))
    
    # plot
    ax.plot_surface(xt[filter], yt[filter], zt[filter], cmap=plt.cm.viridis, alpha=0.8)
    #ax.scatter(x2t, y2t, z2t, s=2, c=plt.cm.ScalarMappable(cmap='magma').to_rgba(z2t), zorder=1)


def main():
    n_frames = 50
    x, y, z = createSphere()
    x2, y2, z2 = createEspiral()

    midif = dif6

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.view_init(elev=15, azim=-45)
    _ = animation.FuncAnimation(fig, update, frames=np.linspace(0,1,n_frames), fargs=[x, y, z, x2, y2, z2, ax, midif], interval=100)
    plt.show()


if __name__ == "__main__":
    main()