# Deformación continua de la esfera


## Índice 

 - [Enunciado](#id0)
 - [Introducción](#id1)
 - [Material usado](#id2)
 - [Resultados y conclusiones](#id3)

## Enunciado <a name=id0></a>


## Introducción <a name=id1></a>

La deformación continua de la esfera se refiere a la capacidad de deformar suavemente una esfera sin rasgarla ni romperla. Este concepto está estrechamente relacionado con la topología, que es la rama de las matemáticas que se ocupa de las propiedades que se conservan bajo deformaciones continuas. La esfera es un ejemplo importante en topología, ya que cualquier dos esferas son homeomorfas, lo que significa que pueden deformarse continuamente una en la otra.

La proyección estereográfica es un ejemplo de una deformación continua de la esfera. Esta transformación mapea los puntos de una esfera a un plano complejo extendido mediante una línea recta que conecta cada punto en la esfera con el punto de proyección en el polo norte. La proyección estereográfica es un difeomorfismo suave y biyectivo entre la esfera excluyendo su polo norte y el plano complejo extendido, con una inversa suave.

Las deformaciones continuas de la esfera tienen muchas aplicaciones en matemáticas, física e ingeniería. Por ejemplo, la proyección estereográfica se utiliza en cartografía para mapear la superficie esférica de la Tierra a un mapa plano. También se utiliza en la teoría de funciones complejas para estudiar las propiedades de las funciones holomorfas en el plano complejo. En ingeniería, la deformación continua de la esfera se utiliza en el diseño de estructuras y materiales que deben soportar cargas y deformaciones sin romperse o rasgarse.

## Material usado <a name=id2></a>

## Resultados y conclusiones <a name=id3></a>

Primero de todo recalcar que el punto que extraeremos de la esfera, $\mathcal{S}_1^2$, para hacer posible su proyección, es el polo norte, $e_3 = (0,0,1)$. Una vez sabemos esto podemos jugar con distintas funciones para obtener diferentes familias paramétricas tales que la primera nos conduzca a la identidad y la última a la proyección final en el plano, que en este caso hemos tomado como $\lbrace z = -1 \rbrace$. Es decir, queremos generar la familia $\mathcal{F} = \lbrace g_t : \mathcal{S}_1^2 \rightarrow \mathbb{R}^3 \rbrace$ tales que $g_0 \equiv identidad$ y $g_1\equiv \Pi$ donde $\Pi$ es la proyección en el plano.

El problema lo podemos dividir en dos partes:
 
 1) En $\mathbb{R}^2$, tenemos que pasar los puntos de la esfera a todo el plano, es decir, la proyección final nos tiene que llevar los puntos $A = \lbrace (x,y) \in \mathbb{R}^2 \ | \ x^2+y^2 \leq 1 \rbrace$ en $\mathbb{R}^2$. En este punto tenemos un problema pues para cada $(x_0,y_0)\in A$ existen dos valores $z_1$ y $z_2$ tales que $(x_0,y_0,z_1), (x_0,y_0,z_2) \in \mathcal{S}_1^2$. Por lo que para que la función sea biyectiva tendremos que distinguir ambos conjuntos.
 
    - $A_1 = \lbrace (x,y,z) \in \mathbb{R}^3 \ | \ x^2+y^2+z^2 = 1 \ y \ z > 0 \rbrace \subset \mathcal{S}_1^2$
    - $A_2 = \lbrace (x,y,z) \in \mathbb{R}^3 \ | \ x^2+y^2+z^2 = 1 \ y \ z < 0 \rbrace \subset \mathcal{S}_1^2$
 
 Para ello en la transformación de $x$ e $y$ tendremos que tener en cuenta el valor $z$ para obtener distintos resultados.
 
 2) La coordenada $z$ la movemos de alguna forma desde el punto actual $z = z_0$ hasta el punto de destino $z=-1$. Para ello podemos utilizar una simple función lineal, u otras más complejas para distintas visualizaciones.
 

### Difeomorfismos 1

Para la transformación de $z$ la función más simple es una transformación lineal tal que $f(0) = z_0$ y $f(1) = -1$. Esta es,

$$
f : [-1,1) \times [0,1] \rightarrow [-1,1) : (z,t) \mapsto z \cdot (1-t) + (-1) \cdot t
$$

Para transformar las coordenadas $(x,y)$ podemos multiplicar (proporcionalmente según el $t$) por un factor dependiente de z. Como $(0,0,1)$ es el llamado punto del infinito, los más cercanos queremos multiplicarlos por un factor $k$ grande, tal que, $\lim_{z\rightarrow 1} = +\infty$. Por ejemplo,

$$
f : [-1,1) \rightarrow [1/2, +\infty) : (z,t) \mapsto \dfrac{1}{1 - z}
$$

Ahora introducimos $t$ para conseguir una transformación continua,

$$
f : [-1,1) \times [0,1] \rightarrow [1/2, +\infty) : (z,t) \mapsto \dfrac{1}{1 - zt}
$$

Finalmente podemos definir la familia $\mathcal{F} = \lbrace g_t : \mathcal{S}_1^2 \rightarrow \mathbb{R}^3 \rbrace$ como

$$
g_t : [-1,1] \rightarrow \mathbb{R}^3 : (x,y,z) \mapsto \left(\dfrac{x}{1 - zt}, \dfrac{y}{1 - zt}, z(1-t) + (-1)t\right) 
$$

generando el siguiente resultado:

<div style="text-align:center;">
  <image src="/images/difeomorfismo_1.gif" style="width:100%; height:12cm;">
</div>

<div style="text-align:center;">
  <image src="/images/difeomorfismo_1.gif" style="width:100%; height:12cm;">
  <image src="/images/difeomorfismo_2.gif" style="width:100%; height:12cm;">
  <image src="/images/difeomorfismo_3.gif" style="width:100%; height:12cm;">
  <image src="/images/difeomorfismo_4.gif" style="width:100%; height:12cm;">
  <image src="/images/difeomorfismo_5.gif" style="width:100%; height:12cm;">
  <image src="/images/difeomorfismo_6.gif" style="width:100%; height:12cm;">
</div>

