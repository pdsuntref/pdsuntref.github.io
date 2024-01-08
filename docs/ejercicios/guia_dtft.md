#Guía 2 - Transformada de Fourier en tiempo discreto

1.  Sea $h[n]$ la respuesta al impulso unitario de un sistema LIT, encontrar la respuesta en frecuencia para:

    1.  $h[n] = \delta[n]+6\delta[n-1]+3\delta[n-2]$
    1.  $h[n] = \frac{1}{3}^{(n+2)}u[n-2]$

1.  Encontrar la Transformada de Fourier (DTFT) de las siguientes señales:
    1.  $x[n] = (0.5)^{n}u[n+3]$
    1.  $x[n] = \alpha^{n}sen(n\omega_0)u[n]$
    1.  $x[n] = \alpha^{n}u[n-5]$
    1.  $x[n]= 
    \begin{cases}
    \left(\dfrac{1}{2}\right)^{n}       & \quad n = \text{0,2,4,...}\\
    \hspace{10pt} 0 		 & \quad \text{} \text{resto}
    \end{cases}$

1.  Calcular la respuesta al impulso unitario del filtro pasa bajos ideal, de amplitud unitaria y frecuencia de corte $\omega_c$.

1.  Sea $h[n]$ la respuesta al impulso unitario del filtro pasa bajos calculado en el problema anterior, ¿qué tipo de filtro tiene como respuesta al impulso unitario $g[n]=(-1)^{n}h[n]$?

1.  Considerando un filtro pasa altos con una frecuencia de corte $\omega_c = \frac{3\pi}{4}$, calcular la respuesta al impulso unitario $h[n]$.

1.  Dados dos filtros ideales definidos a partir de sus respuestas en frecuencia, encontrar la respuesta en frecuencia de un nuevo sistema que tenga las respuestas $H_1$ y $H_2$:
    1.  En cascada.
    1.  En paralelo.

    $$ H_1({e^{j\omega}}) = 
    \begin{cases}
      1      & \quad  |\omega| > \dfrac{\pi}{3}\\
      0 		 & \quad \text{} \text{resto}
    \end{cases}$$ 
    
    $$H_2({e^{j\omega}}) = 
    \begin{cases}
    1       & \quad \dfrac{\pi}{4} < |\omega| < \dfrac{3\pi}{4}\\
    0 		 & \quad \text{} \text{resto}
    \end{cases} 
    $$

1.  Encontrar la respuesta en frecuencia $H(e^{jw})$ de un sistema que retarda la entrada en $n_r$ muestras.
    
    $$ y[n] = x[n-n_r] $$

1.  Indicar cuáles de las siguientes señales de tiempo discreto son autofunciones de sistemas discretos LTI estables:
    1.  $e^{j(2\pi)n/3}$
    1.  $3^{n}$
    1.  $2^nu[-n-1]$
    1.  $cos(\omega_0n)$
    1.  $(1/4)^n$
    1.  $(1/4)^nu[n]+4^nu[-n-1]$

1.  Encontrar la respuesta del sistema dado por la siguiente ecuación en diferencias con coeficientes constantes.

    $$ y[n] = 1.3433y[n-1] - 0.9025y[n-2] + x[n] - 1.4142x[n-1] + x[n-2] $$

1.  Calcular la solución de la siguiente ecuación en diferencias con condiciones iniciales nulas, considerando $x[n] = \delta [n]$.

    $$ y[n] - 0.25y[n-1] = x[n] - x[n-2] $$

1.  Dado un sistema LIT que representa a un filtro digital ideal cuya entrada es $x[n]$, su salida $y[n]$ y su respuesta en frecuencia $H(e^{jw})$, encontrar:

    1.  La respuesta en frecuencia de la señal de entrada $X(e^{jw})$.
    1.  La respuesta al impulso $h[n]$ del filtro ideal $H(e^{jw})$.
    1.  La salida del sistema $y[n]$.
    1.  Graficar la magnitud de la respuesta en frecuencia de la salida del sistema $Y(e^{jw})$.

    Datos del sistema:

    $$ x[n]= e^{j0.55\pi n} + 2 cos \left(\dfrac{3}{4}\pi n\right) $$

    $$ \begin{cases}
H({e^{j\omega}}) = 0 \hspace{12pt}     & 0 \leq |\omega| \leq 0.5\pi \\
H({e^{j\omega}}) = 1 \hspace{12pt}     & 0.5 \pi < |\omega| \leq 0.6\pi \\
H({e^{j\omega}}) = 0.5 \hspace{12pt}     & 0.6 \pi < |\omega| \leq \pi \\
\end{cases} $$

1.  Siendo la Transformada de Fourier de una señal $x[n] \leftrightarrow X(e^{jw})$, se puede demostrar que la transformada de su conjugada es $x^\ast [n] \leftrightarrow X^\ast (e^{-jw})$. Usando este resultado, determinar si la transformada de las siguientes señales es conjugada Simétrica/Asimética, e indicar qué tipo de paridad tiene el módulo y la fase de la transformada para los siguientes casos:

    1.  $x[n]$ real.
    1.  $x[n]$ imaginaria.

1.  Calcular la DTFT de las siguientes ventanas. Indicar cuáles de ellas son _causales_.

    1.  Ventana rectangular, 
    $w_1[n]=
    \begin{cases}
    1       & \quad 0 \leq n \leq M\\
    0 		 & \quad \text{} \text{resto}
    \end{cases}$
    1.  Ventana rectangular (centrada en 0),
    $w_2[n] = 
    \begin{cases}
    1       & \quad \dfrac{-M-1}{2} \leq n \leq \dfrac{M-1}{2}\\
    0 		 & \quad \text{} \text{resto}
    \end{cases}$
    1.  Ventana triangular (_Bartlett_),
    $w_3[n]=
    \begin{cases}
    1 - \left | \dfrac{n - M/2}{M/2}\right |      & \quad 0 \leq n \leq M\\
    0 		 & \quad \text{} \text{resto}
    \end{cases}$

1.  Implementar en algún lenguaje de programación de su elección las siguientes ventanas. Las mismas deben cumplir con la propiedad de causalidad.
    1.  Ventana rectangular.
    1.  Ventana triangular.
    1.  Ventana de Hann(ing).

    Graficar la magnitud de sus respuestas en frecuencia a partir de:

      1.  Utilizar un número de muestras $M = 50$.
      1.  Utilizar un número de muestras $M = 140$.
      1.  Utilizar un número de muestras $M = 250$.

    Para todos los casos:

      1.  ¿De qué manera varía el ancho del lóbulo principal para cada caso?
      1.  ¿Qué cambios se observan en la amplitud relativa entre el lóbulo principal y el lóbulo secundario?
