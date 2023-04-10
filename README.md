# Deformación continua de la esfera


## Índice 

 - [Enunciado](#id0)
 - [Introducción](#id1)
 - [Material usado](#id2)
 - [Resultados y conclusiones](#id3)
      - [Difeomorfismo 1](#id3.1)
      - [Difeomorfismo 2](#id3.2)
      - [Difeomorfismo 3](#id3.3)
      - [Difeomorfismo 4](#id3.4)
      - [Difeomorfismo 5](#id3.5)
      - [Difeomorfismo 6](#id3.6)
          - [Demostración](#id3.6.1)

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
 

### Difeomorfismo 1 <a name=id3.1></a>

Para la transformación de $z$ la función más simple es una transformación lineal tal que $f(0) = z_0$ y $f(1) = -1$. Esta es,

$$
f : [-1,1) \times [0,1] \rightarrow [-1,1) : (z,t) \mapsto z \cdot (1-t) + (-1) \cdot t
$$

Para transformar las coordenadas $(x,y)$ podemos multiplicar (proporcionalmente según el $t$) por un factor dependiente de z. Como $(0,0,1)$ es el llamado punto del infinito, los más cercanos queremos multiplicarlos por un factor $k$ grande, tal que, $\lim_{z\rightarrow 1} = +\infty$. Por ejemplo,

$$
f : [-1,1) \rightarrow [1/2, +\infty) : (z,t) \mapsto \dfrac{1}{1 - z}
$$

<div style="text-align:center;">
  <image src="/images/f1.png" style="width:40%;">
</div>

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


### Difeomorfismo 2 <a name=id3.2></a>

De forma a similar a como hemos generado el difeomorfismo anterior, podemos hacer alguna pequeña modificación en cómo se mueve la coordenada $z$. Por ejemplo, 

$$ 
f(z) = \dfrac{z}{1-tz}(1-t) + (-1)t
$$

observamos que en este caso hacemos un cambio lineal de $f(z)=\dfrac{z}{1-tz} = z$ (en $t=0$) a $f(z)=-1$ (en $t=1$), al igual que antes. En esta ocasión se intenta aumentar la coordenada $z$ al comienzo de las primeras parametrizaciones y luego terminar disminuyendolo hasta $z=-1$ en vez de directamente bajar linealmente hasta $z=-1$ para evitar esa sensación de *aprastar* la esfera. Sin embargo, como podemos ver en la animación resultante, no conseguimos el efecto deseado pues para cuando $\dfrac{z}{1-tz}$ comienza a aumentar, el factor $(1-t)$ lo disminuye. 

<div style="text-align:center;">
  <image src="/images/difeomorfismo_2.gif" style="width:100%; height:12cm;">
</div>

Para evitar que esas dos funciones se contraresten podemos deformar el intervalo $[0,1]$ de tal forma que para cuando $\dfrac{z}{1-tz}$ comienze a aumentar el factor $(1-t)$ no lo cancele (temporalmente, pues está claro que al final dicho factor tiene que ser nulo).  

### Difeomorfismo 3 <a name=id3.3></a>

Como comentabamos al final del anterior apartado, generamos alguna deformación del intervalo $[0,1]$ tal que no mantengamos *cerca* del 0 gran parte del intervalo. Podemos pensar en las funciones tangente y arcotangente con algunas modificaciones como:

$$
f(t) = \dfrac{2}{\pi} \cdot arctg \left(\dfrac{1}{20}tg(\dfrac{\pi}{2}t) \right)
$$

<div style="text-align:center;">
  <image src="/images/f2.png" style="width:40%;">
</div>

Para entender mejor de dónde ha salido la función comento algunas observaciones (informales): 
 - $tg(\dfrac{\pi}{2}t)$ tiene como objetivo, pasar con $\dfrac{\pi}{2}t$ de $[0,1]$ a $[0,\dfrac{\pi}{2}]$ y así con la tangente pasar al intervalo $[0, +\infty)$.
 - $\dfrac{1}{20}$ es un factor para *aplastar* el intervalo (se pueden hacer modificaciones y pruebas con él), que al estar dentro de la arcontangente, tendrá mucho más efecto.
 - $arctg()$ permite devolvernos al intervalo $[0,\dfrac{\pi}{2}]$.
 - $\dfrac{2}{\pi}$ nos lleva finalmente al intervalo $[0,1]$.
 
Observación: razonando de forma análoga, podemos obtener resultados opuestos cambiando el factor $\dfrac{1}{20}$ por $20$ (por ejemplo), y así obtenemos el objetivo contrario, mantenernos cerca del 1 la mayor parte del intervalo.

<div style="text-align:center;">
  <image src="/images/f3.png" style="width:40%;">
</div>

Recuperando los resultados anteriores, conseguimos mantener mayor tiempo el factor $\dfrac{z}{1-tz}$ y apreciar dicho aumento temporal de la esfera. Agrupando estos resultados ($x$ e $y$ se modifican igual que en el primero), generamos $g_t$ tal que

$$
\begin{array}{rcl}
x &\mapsto & \dfrac{x}{1-tz} \\ \\
y &\mapsto & \dfrac{y}{1-tz} \\ \\
z &\mapsto & \dfrac{z}{1-tz}(1-k) + (-1)k
\end{array}
$$


donde 
 
$$
k = \dfrac{2}{\pi} \cdot arctg \left(\dfrac{1}{20}tg(\dfrac{\pi}{2}t) \right)
$$

Generando finalmente la siguiente deformación con los objetivos que queríamos,

<div style="text-align:center;">
  <image src="/images/difeomorfismo_3.gif" style="width:100%; height:12cm;">
</div>


### Difeomorfismo 4 <a name=id3.4></a>

Para esta nueva familia de parametrizaciones cambiaremos el factor multiplicativo $k$ de las coordenadas $x$ e $y$. Antes hemos utilizado $\dfrac{1}{1-tz}$ cuyo objetivo es comenzar en $k=1$ y terminar $k \rightarrow \infty$. Ahora utilizaremos la función tangente con el mismo objetivo. Para ello modificamos el intervalo $[-1,1)$ al intervalo $[0,\dfrac{\pi}{2})$ y luego lo pasamos por la tangente llevandolo al intervalo $[0, +\infty)$. Finalmente  sumamos 1 para comenzar el factor en 1. Para la actualización de $z$ utlizamos una de las anteriores como $\dfrac{z}{1-tz}(1-t) + (-1)t$. Puesto que la tangente da cambios muy extremos, es decir, su derivada tiende a infinito cuando se tiende a $\dfrac{\pi}{2}$ entonces observaremos en la animación que los valores se mantienen cerca de la esfera inicial hasta que se ven afectados por el cambio tangencial. Por ello podemos observar como poco a poco, los puntos con valores de $z$ superiores se han alejado rápidamente hacia el infito mientras que otros todavía se mantienen muy cerca de su punto original. 
 
$$
g_t (x,y,z) = (c_{t,z}x, c_{t,z}y, \dfrac{z}{1-tz}(1-t) + (-1)t)  
$$

 donde 
 
 $$
 c_{t,z} = 1 + w \cdot tg(\frac{\pi}{2}(z+1)/2) t
 $$

<div style="text-align:center;">
  <image src="/images/difeomorfismo_4.gif" style="width:100%; height:12cm;">
</div>


### Difeomorfismo 5 <a name=id3.5></a>
 
 Mediante un pequeño cambio de la función anterior, podemos hacer que el cambio tangencial tarde un poco más en afectar, es decir, modificar otra vez el intervalo $[0,1]$ de forma que nos mantengamos cerca del 0 más tiempo. Para ello utilizamos la función anterior: $\dfrac{2}{\pi} \cdot arctg \left(\dfrac{1}{20}tg(\dfrac{\pi}{2}t) \right)$. Con ella permitimos que el cambio se vea afectado más tarde, pero igualmente acabará afectando, por lo que la transformación queda similar. 

$$
g_t (x,y,z) = (c_{t,z}x, c_{t,z}y, \dfrac{z}{1-tz}(1-t) + (-1)t)  
$$

 donde 
 
 $$
 c_{t,z} = 1 + w \cdot tg(\frac{\pi}{2}(z+1)/2) \cdot \dfrac{2}{\pi} \cdot arctg \left(\dfrac{1}{20}tg(\dfrac{\pi}{2}t) \right)
 $$
 
<div style="text-align:center;">
  <image src="/images/difeomorfismo_5.gif" style="width:100%; height:12cm;">
</div>

A diferencia del difeomorfismo anterior (difeomorfismo 4), podemos observar la sensación de que la esfera se contrae, esto es devido a lo comentado anteriormente. Como el factor $\dfrac{2}{\pi} \cdot arctg \left(\dfrac{1}{20}tg(\dfrac{\pi}{2}t) \right)$ cancela durante mayor tiempo el valor $tg(\frac{\pi}{2}(z+1)/2)$, los puntos (en las coordenadas $x$ e $y$) se mantienen cerca del origen, mientras que la coordenada $z$ progresivamente se va acercando al plano $z = -1$, por lo que da la impresión de contracción en dicha parte de la esfera.

### Difeomorfismo 6 <a name=id3.6></a>

Por último, generamos una transformación similiar a las primeras pero con tangentes y arcotangentes. Construimos un factor en $[1,+\infty)$. Para ello introducimos la tangente, y en su interior hacemos una transformación lineal desde $arctg(1)$ hasta $\dfrac{\pi}{2}$. Finalmente conseguimos los siguientes resultados.

$$
g_t (x,y,z) = (c_{t,z}x, c_{t,z}y, z(1-t) + (-1)t)  
$$

 donde 
 
 $$
 c_{t,z} = tg(\dfrac{\pi}{2}\dfrac{1+z}{2}t + arctg(1)(1-t))
 $$
 
<div style="text-align:center;">
  <image src="/images/difeomorfismo_6.gif" style="width:100%; height:12cm;">
</div>
 
#### Demostración <a name=id3.6.1></a>
 
Para terminar esta serie de ejemplos, demostraremos (no con todos los detalles) que esta última función es un difeomorfismo.
 
 1) Primero de todo, las funciones tangente y arcotangente son diferenciables. Por composición de funciones diferenciables, $g_t$ lo es.
 2) Veamos que $g_t$ tiene inversa diferenciable, ambas inyectivas y por tanto $g_t$ biyectiva. Sean $(x_0, y_0, z_0) \in \mathcal{S}_1^2$ y
 
$$
(x_1, y_1, z_1) = g_t(x_0, y_0, z_0) = (c_{t,z_0} \ x_0, c_{t,z_0}\ y_0, z_0(1-t) + (-1)t)
$$

Queremos partir de un punto cualquiera $(x_1,y_1,z_1)$ y llegar al punto (único) $(x_0,y_0,z_0)$. Por lo que los valores $x_1,y_1,z_1,t\in \mathbb{R}$ son conocidos.
 
Despejando en la última coordenada tenemos: $z_1 = z_0(1-t) + (-1)t$ entonces:
 
   - Si $z_0 = -1$ entonces $(x_0,y_0,z_0) = (x_1,y_1,z_1) = (0,0,-1)$ y ya hemos terminado.
   - Si $t = 1$ estamos en la proyección completa $(c_{1,z_0} \ x_0, c_{1,z_0}\ y_0, -1)$ donde $c_{1,z_0} = tg(\dfrac{\pi}{2}\dfrac{1+z_0}{2})$. Así tenemos que $x_1 = c_{1,z_0} \ x_0$ e $y_1 = c_{1,z_0} \ y_0$, es decir, $y_0 = \dfrac{y_1}{c_{1,z_0}} = \dfrac{y_1}{x_1}x_0$. Por tanto teniendo en cuenta que $x_0^2 + y_0^2 + z_0^2 = 1$ tenemos que,

$$
\begin{array}{rcl}
x_1 & = & x_0 \ c_{1,z_0} \\
&=& x_0 \ tg(\dfrac{\pi}{2}\dfrac{1+z_0}{2}) \\
&=& x_0 \ tg(\dfrac{\pi}{4}(1+z_0)) \\
&=& x_0 \ tg(\dfrac{\pi}{4}(1 + \sqrt{1 - x_0^2 - y_0^2})) \\
&=& x_0 \ tg \left( \dfrac{\pi}{4} \left( 1 + \sqrt{1 - x_0^2 - (\dfrac{y_1}{x_1}x_0)^2} \right) \right) \\
&=& x_0 \ tg \left( \dfrac{\pi}{4} \left( 1 + \sqrt{1 - (1+\dfrac{y_1^2}{x_1^2})x_0^2} \right) \right) := f(x_0)
\end{array}
$$
 
donde el último término es una función de $x_0$ monótona por lo que $f(x_0) = x_1$ tiene una única solución. Así despejamos obtenemos $x_0 = k$ para cierto $k\in \mathbb{R}$ y de ahí obtenemos $y_0$ y $z_0$.

   - Si $z_0 \neq -1$ y $t \neq 1$ entonces $z_0 = \dfrac{z_1 - t}{1-t} \in \mathbb{R}$. Ahora el valor $c_{t,z_0} = tg(\dfrac{\pi}{2}\dfrac{1+z_0}{2}t + arctg(1)(1-t))$ es conocido por serlo $t$ y $z_0$. Así como $(x_1, y_1, z_1) = (c_{t,z_0} \ x_0, c_{t,z_0}\ y_0, z_0(1-t) + (-1)t)$, se tiene que 
 
 $$
 (x_0,y_0,z_0) = \left( \dfrac{1}{c_{t,z_0}} \ x_1, \dfrac{1}{c_{t,z_0}} \ y_1, \dfrac{z_1 - t}{1-t} \right)
 $$
 





