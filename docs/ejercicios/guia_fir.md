# Guía 7 - Filtros FIR (respuesta al impulso finita)

1.  Dadas las siguientes especificaciones de un filtro discreto FIR con fase lineal, diseñarlo por el método de las ventanas utilizando al menos dos tipos diferentes y comparar los resultados.

    $$ 0.89 \leq |H(e^{jw})| \leq 1\hspace{36pt} 0\leq|\omega|\leq 0.2\pi $$

    $$ |H(e^{jw})| \leq 0.01 \hspace{36pt} 0.3\pi \leq|\omega|\leq\pi $$

1.  Dadas las siguientes especificaciones de un filtro discreto FIR pasa bajos con fase lineal, diseñarlo utilizando el método de Kaiser.

    $$ 0.89 \leq |H(e^{jw})| \leq 1\hspace{36pt} 0\leq|\omega|\leq 0.4\pi $$

    $$ |H(e^{jw})| \leq 0.001 \hspace{36pt} 0.6\pi \leq|\omega|\leq\pi $$

1.  Dadas las siguientes especificaciones de un filtro discreto FIR pasa altos con fase lineal, diseñarlo utilizando el método de Kaiser.

    $$ 0.89 \leq |H(e^{jw})| \leq 1\hspace{36pt} 0.5\pi\leq|\omega|\leq \pi $$

    $$ |H(e^{jw})| \leq 0.021 \hspace{36pt} 0 \leq|\omega|\leq 0.3\pi $$

1.  Dadas las siguientes especificaciones de un filtro discreto FIR pasa banda con fase lineal, diseñarlo utilizando el método de Kaiser.

    $$ 0.89 \leq |H(e^{jw})| \leq 1\hspace{36pt} 0.3\pi \leq|\omega|\leq 0.6\pi $$

    $$ |H(e^{jw})| \leq -80 dB \hspace{36pt} 0.2 \pi \geq|\omega|\geq 0.8\pi $$

1.  Se hace una grabación digital de voz, con una frecuencia de muestreo de 8000 Hz, en
un ambiente ruidoso. Se determina que la máxima frecuencia de interés es 1800 Hz. Se pide diseñar por el método de las ventanas un filtro FIR con fase lineal que remueva el ruido más allá de la banda interés. El ancho máximo de la banda de transición es de
hasta 200 Hz y la atenuación en la banda de detención de al menos 50 dB.

    1.  Elegir el tipo de ventana y determinar el mínimo número de muestras que satisfagan las condiciones de diseño.
    1.  ¿Qué tipo de filtro representa (I, II, III o IV)? Justificar.
    1.  Escribir la respuesta al impulso del filtro FIR causal de fase lineal correspondiente.
