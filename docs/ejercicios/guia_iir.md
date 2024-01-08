# Guía 6 - Filtros IIR (respuesta al impulso infinita)

1.  Dado un filtro analógico con la función transferencia $X(s)$, encontrar el filtro discreto correspondiente utilizando la invariancia al impulso para realizar la transformación. Observar cómo es el mapeo de los polos y de los ceros:

    $$ X(s) = \dfrac{s + 0.1}{(s + 0.1)^{2} + 9} $$

    Una vez encontrado el filtro digital $X(z)$, graficar la respuesta en frecuencia para valores de tiempo de muestreo $T_s$ de 0.1 y de 0.5.

1.  Repetir el ejercicio anterior utilizando el método de mapeo de polos y ceros (_Matched Z-transform_). Comparar con el método anterior.

1.  Dadas las siguientes especificaciones de un filtro discreto, diseñarlo utilizando un filtro analógico de tipo Butterworth y el método de la invariancia al impulso. Analizar el uso de distintos valores del parámetro $T$.

    $$ 0.89125 \leq |H(e^{jw})| \leq 1\hspace{36pt} 0\leq|\omega|\leq 0.2\pi $$

    $$ |H(e^{jw})| \leq 0.17783 \hspace{36pt} 0.3\pi \leq|\omega|\leq\pi $$

1.  Diseñe un filtro digital pasa bajos tipo Butterworth utilizando la transformación bilineal con _pre-warping_ que cumpla con las siguientes especificaciones:

    $$ 0.79 \leq |H(e^{jw})| \leq 1\hspace{36pt} 0\leq|\omega|\leq \dfrac{8\pi}{35} $$

    $$ |H(e^{jw})| \leq 0.2818 \hspace{36pt} \dfrac{15\pi}{35} \leq|\omega|\leq\pi $$

1.  Dado el siguiente filtro analógico caracterizado por su función de transferencia $H(s)$ y su respuesta al impulso $h(t)$, determinar usando el método de invariancia al impulso la respuesta al impulso discreta $h[n]$. Además, usando el método de la transformada bilineal, determinar la función de transferencia $H(z)$ del filtro digital. El periodo de muestreo en los dos casos es $T = 0,1 s$.

    $$ H(s) = \dfrac{10}{s+10} \hspace{36pt} h(t) = 10 e^{-10t} u(t) $$

1.  Considerando un filtro de Bessel representado por la siguiente función:

    $$ H(s) = \dfrac{3}{s^{2}+3s+3} $$

    Diseñar un filtro digital utilizando el método de la _Transformada Bilineal_ cuya magnitud a la frecuencia $f_0 =$ 3 $kHz$ sea equivalente a la magnitud de $H(s)$ a la frecuencia $\Omega_a =$ 4 $rad/s$, considerando como frecuencia de sampleo $fs =$ 12 $kHz$.

1.   El siguiente filtro _elimina banda_ o _notch_ posee una frecuencia de atenuación máxima o _notch frequency_ de $\Omega_0 =$ 1 $rad/s$:

    $$ H(s) = \dfrac{s^{2} + 1}{s^{2} + 4s + 1} $$

    Utilizando el método de la _Transformada Bilineal_, diseñar un filtro digital utilizando una frecuencia de sampleo de $fs =$ 240 $Hz$ y una frecuencia de atenuación máxima de $f =$ 60 $Hz$.

    ??? info "Nota"
        Uno de los diseños más comunes que se implementan en los filtros elimina banda es el denominado Twin-T notch filter o Parallel Tee. La función que se presenta en este ejercicio corresponde a ese tipo de diseño de filtro.

1.  Diseñar un filtro pasa bajos digital de primer orden que tenga una atenuación de $-3$ $dB$ en $1$ $kHz$ siendo la frecuencia de muestreo usada $8$ $kHz$. Usar para el diseño el método de la transformada bilineal y un filtro pasa bajos analógico cuya función de transferencia es $H(s)$, con una ganancia de $0$ $dB$ en $\Omega = 0$ y de $-3$ $dB$ en $\Omega = \Omega_c$.

    $$ H(s) = \dfrac{1}{1+\dfrac{s}{\Omega_c}} $$

1.  Dado un filtro analógico cuyos polos se muestran en plano $S$ de la figura, encontrar la ubicación de los polos del correspondiente filtro discreto utilizando el método de invariancia al impulso con un período de muestreo $T = 0,1$.

    ![Sistema ej 9](./img/ej9_g6.png "Sistema ejercicio 9")

    1.  En función de la posición de los polos ¿qué tipo de filtro representa?
    1.  Si el período de muestreo es ahora $T = 1$, ¿se modifica en algo la situación del punto anterior? Justificar.

1.  Programar un filtro pasa bajos de Butterworth utilizando transformación bilineal con _prewarping_ con las siguientes características:

    $$ |H(e^{jw})| \leq -1.5 dB\hspace{36pt} 0\leq|\omega|\leq 0.2\pi $$

    $$ |H(e^{jw})| \leq -25 dB \hspace{36pt} 0.6\pi \leq|\omega|\leq\pi $$

1.  Programar un filtro pasa banda de Butterworth utilizando transformación bilineal con _prewarping_ con las siguientes características:

    $$ |H(e^{jw})| \leq -2.1 dB\hspace{36pt} \dfrac{\pi}{10}\leq|\omega|\leq \dfrac{\pi}{5} $$

    $$ |H(e^{jw})| \leq -20 dB \hspace{36pt} \dfrac{45\pi}{1000} \leq|\omega|\leq \dfrac{5\pi}{2} $$

??? info "Nota"
    Python no tiene en alguna de sus librerías un algoritmo que les permita ver los polos y ceros en el plano Z (en MATLAB sería la función zplane), por lo que esto queda abierto a una implementación propia o a que puedan buscar alguna que les resulte cómoda de usar. Adicionalmente, les dejamos esta implementación a modo de ejemplo: https://www.dsprelated.com/showcode/244.php



