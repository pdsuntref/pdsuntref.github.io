#Guía 4 - Transformada Z (señales)

1.  Calcular la transformada Z de las siguientes funciones.
    
    1.  $x[n] = \sqrt[]{3} \delta [n]$
    1.  $x[n] = u[n]$
    1.  $x[n] = cos [\beta n] u[n]$
    1.  $x[n] = u[n] - u[n-5]$
    1.  $x[n] = n\{u[n] - u[n-6]\}$
    1.  $x[n] = \left(\dfrac{1}{3}\right)^{n} u[n] - \left(\dfrac{1}{2}\right)^{n} u[-n-1]$
    1.  $x[n] = \begin{cases}a^{n-1} & n = 1,2,3,... \\ 0, & n \leq 0 \end{cases}$

1.  Calcular la transformada inversa de la siguiente función para las siguientes regiones de convergencia:

    $$ X(z) = \dfrac{3 - \dfrac{5}{6}z^{-1}}{\left(1 - \dfrac{1}{4}z^{-1}\right)\left(1 - \dfrac{1}{3}z^{-1}\right)} $$

    1.  _ROC_: $|z| > \dfrac{1}{3}$
    1.  _ROC_: $\dfrac{1}{4} < |z| < \dfrac{1}{3}$
    1.  _ROC_: $|z| < \dfrac{1}{4}$

1.  Calcular la transformada inversa de las siguientes funciones:

    1.  $X(z) = \dfrac{8z -19}{(z-2)(z-3)}$
    1.  $X(z) = \dfrac{z(2z^2-11z+12)}{(z-2)^3(z-1)}$
    1.  Para $X(z) = \dfrac{z}{(z-1)(z-2)}$, en las siguientes regiones de convergencia:
        1.  $|z|<1$
        1.  $1<|z|<2$
        1.  $|z|>2$

1.  Resolver las siguientes ecuaciones en diferencias:
    
    1.  $y[n] - \dfrac{1}{2}y[n-1] = x[n]$, siendo $x[n] = \left(\dfrac{1}{3}\right)^n u[n], y[-1] = 1$
    1.  $y[n+2]- 5y[n+1]+6y[n] = x[n]$, siendo $x[n] = u[n], y[0] = 1, y[1] = 0$. Comparar con el resultado de la Guía 2, Ej. 5.
    1.  $y[n]-0.25y[n-1] = x[n] - x[n-2]$, siendo $x[n] = \delta[n]$. Condiciones iniciales nulas. Comparar con el resultado de la Guía 2, Ej.7.

1.  Hallar la respuesta al impulso del sistema discreto, lineal y causal. Encontrar la salida $y[n]$ cuando se aplica al mismo la señal $x[n] = 2^{-n}u[n]$:
    
    ![Señal ej 5](./img/ej5_g4.png "Señal ejercicio 5")

1.  Considere la ecuación en diferencias:

    $$ f[k+2] = f [k+1] + f[k] $$

    donde $f[0] = 0$ y $f[1] = 1$. Observe que $f[2] = 1$, $f[3] = 2$, $f[4] = 3$,...La serie 0,1,1,2,3,4,5,8,13,... se conoce como _serie de Fibonacci_.

    1.  Obtenga la solución general $f[k]$ en una forma cerrada.
    1.  Muestre que el valor límite de $\dfrac{f[k+1]}{f[k]}$ a medida que $k$ se aproxima a infinito es $\dfrac{(1+\sqrt[]{5})}{2}$.

1.  Considere la ecuación en diferencias:

    $$ f[n+1] + 2f[n] = u[n]  $$

    donde $f[0] = 1$ y $n = 0,1,2,...$, siendo $u[n]$ la secuencia escalón unitario. Obtener $f[n]$ para $n>0$.

1.  Considere la ecuación en diferencias:

    $$ h[n+1] + 2h[n] = \delta[n] $$

    donde $h[0] = 0$. Determinar la respuesta del sistema al impulso.

1.  Resuelva y grafique la posición de polos y ceros en los ejercicios anteriores.
