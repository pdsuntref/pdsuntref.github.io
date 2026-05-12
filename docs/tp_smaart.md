# Filtrado e identificación de sistemas

Un analizador de doble canal es un dispositivo que analiza en simultáneo dos señales, generalmente la entrada y la salida de un sistema a caracterizar. Su respuesta en frecuencia $H(\omega)$ se puede obtener mediante la ecuación

$$H(\omega) = \frac{Y(\omega)}{X(\omega)}$$

en donde $Y(\omega)$ es la transformada de Fourier de la señal de salida, $y[n]$, mientras que $X(\omega)$ corresponde a la transformada de Fourier de la señal de entrada, $x[n]$.

Si nuestro sistema se puede considerar lineal e invariante en el tiempo, conocer su respuesta en frecuencia implica que lo tenemos completamente caracterizado, ya que su antitransformada corresponde a su respuesta al impulso. A través de esta caracterización es muy simple conocer el efecto que el sistema tendrá mediante la convolución entre la señal de entrada y la respuesta al impulso $h[n]$:

$$y[n] = \sum_{k=-\infty}^{\infty}x[k]*h[n-k]$$

o, en frecuencia:

$$Y(\omega) = X(\omega)H(\omega)$$

El trabajo práctico se divide en dos partes. La primera consiste en el desarrollo mediante código de un sistema que permita realizar las siguientes tareas:

* Graficar una o varias señales temporales.

* Graficar uno o varios espectros de Fourier.

* Determinar la respuesta en frecuencia de un sistema $H(\omega)$ dado un par de señales de entrada y salida $X(\omega)$ e $Y(\omega)$.

* Generar respuestas al impulso para los siguientes filtros: media móvil con una, dos y tres pasadas, filtro peine, filtro de respuesta al impulso finita. Las ecuaciones para los distintos filtros propuestos son:

  - Filtro media móvil: $h[n]=\frac{1}{M}$, siendo $M$ el largo de la ventana.
  - Filtro peine: $h[n] = b_0 + b_1\,\delta[n-1] + b_2\,\delta[n-2]$, donde $b_0$, $b_1$ y $b_2$ son coeficientes constantes.
  - Filtro de respuesta al impulso finita: coeficientes provistos por la cátedra.

* Caracterizar en frecuencia los filtros (módulo y fase). Analizar y discutir los comportamientos encontrados y las diferencias entre los distintos casos.

* Variar los parámetros de los filtros de la familia de media móvil y del filtro peine, ¿qué relaciones se encuentran entre sus valores y los comportamientos resultantes en frecuencia?

* Generar las siguientes señales temporales:
  
  - Suma de tonos puros + ruido blanco de distintas amplitudes.
  - Señal musical + ruido blanco de distintas amplitudes.

* Filtrar las señales con los filtros diseñados y analizar los resultados. Hacerlo mediante convolución en el dominio del tiempo y mediante convolución circular en frecuencia (usar propiedades).

* Truncar la cantidad de coeficientes del filtro FIR y evaluar los efectos del truncado.

La segunda parte consiste en la identificación de sistemas desconocidos usando las herramientas desarrolladas en la primera parte. A partir de los pares de señales de entrada y salida provistas por la cátedra, identificar las características en frecuencia del sistema que está procesando la señal de entrada. Evaluar su comportamiento, estudiar la coherencia de la medición y en base a esos resultados analizar la linealidad del mismo en distintas partes del espectro. La coherencia viene dada por la siguiente ecuación:

$$\gamma_{xy}^2(\omega)=\frac{|G_{xy}(\omega)|^2}{G_{xx}(\omega)\,G_{yy}(\omega)}$$

donde $\gamma_{xy}^2(\omega)$ es la coherencia cuadrática, $G_{xy}(\omega)$ es la densidad espectral de potencia cruzada entre las señales de entrada y salida, $G_{xx}(\omega)$ es la densidad espectral de potencia de la señal de entrada y $G_{yy}(\omega)$ es la densidad espectral de potencia de la señal de salida. Las densidades espectrales de potencia se calculan corresponden a las transformadas de Fourier de las correlaciones cruzadas o autocorrelaciones, dependiendo del caso.

La coherencia toma valores entre 0 y 1. Si la coherencia vale 1 para alguna frecuencia en particular, la relación entre las señales de entrada y salida a esa frecuencia es perfectamente lineal. En cambio, si este parámetro vale 0 para alguna frecuencia en particular, significa que no existe relación lineal en esa parte del espectro. ¿Por qué consideran que se cumplen esas relaciones dada la forma en la que se calcula la coherencia? Para el caso de los pares de señales que deben analizar, ¿cómo es la linealidad del sistema en distintas partes del espectro? ¿Qué tipos de sistemas reales podrían dar lugar a ese tipo de comportamientos?


## Condiciones para la entrega

El trabajo puede realizarse en grupos de hasta 4 personas. Además de la entrega del trabajo completo se les pide una pre-entrega, que corresponde a una versión parcial del trabajo (parte 1 como mínimo). El formato de entrega, tanto para la entrega parcial como para la entrega final, será un notebook de Jupyter y un archivo de python. En el archivo de python se deberán escribir las funciones que permiten cumplir los distintos requerimientos del trabajo, mientras que en el notebook de Jupyter deberán usar las funciones que escribieron y acompañar los resultados del código con explicaciones escritas de los fenómenos que vayan descubriendo.

La fecha de la pre-entrega es el **3 de junio**, mientras que la fecha de la entrega final es el **1 de julio**. No se aceptarán entregas finales fuera de esta fecha (recuerden que el trabajo práctico es condición de aprobación de la cursada)

