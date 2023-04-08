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
    ax.plot_surface(xt[filter], yt[filter], zt[filter], cmap=plt.cm.viridis, alpha=1)
    #ax.scatter(x2t, y2t, z2t, s=2, c=plt.cm.ScalarMappable(cmap='magma').to_rgba(z2t), zorder=1)


def animate_sphere(difeomorfismo, save=False, savepath="ani.gif"):

    n_frames = 50
    x, y, z = createSphere()
    x2, y2, z2 = createEspiral()

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.view_init(elev=15, azim=-45)
    ani = animation.FuncAnimation(fig, update, frames=np.linspace(0,1,n_frames), fargs=[x, y, z, x2, y2, z2, ax, difeomorfismo], interval=100)
    if save:
        ani.save(f"images/{savepath}")
    plt.show()

def plot_interval(function, a=0, b=1):
    c, d = int(np.round(function(a))), int(np.round(function(b)))
    x = np.linspace(a, b, 100)
    y = function(x)
    fig = plt.figure(figsize=(5,5))
    ax = fig.add_subplot(111)
    ax.set_title(f"Conversión de intervalos:\n[{a},{b}] -> [{c},{d}]")
    ax.plot(x, y, "k-")
    ax.set_xticks([a,b])
    ax.set_yticks([c, d])
    plt.show()


if __name__ == "__main__":
    for i, dif in enumerate([dif1, dif2, dif3, dif4, dif5, dif6]):
        animate_sphere(dif, save=True, savepath=f"difeomorfismo_{i+1}.gif")
    # plot_interval(f1)
    # plot_interval(f2)