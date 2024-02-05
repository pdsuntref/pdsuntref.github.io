# Generación de audio de violín mediante síntesis FM y técnicas de procesamiento de señales diferenciable

## Breve introducción a la síntesis FM

La síntesis FM es una técnica de generación de audio surgida en la década de los 60's basada, como su nombre lo indica, en técnicas de modulación en frecuencia. A grandes rasgos, esta técnica está basada en dos grandes bloques: un oscilador que funciona como modulador, y un segundo oscilador que funciona como señal portadora. La idea del método consiste en que la frecuencia instantánea de la señal portadora es modificada según la amplitud de la señal modulante, como se puede ver en la figura:

[DIAGRAMA ESQUEMATICO MODULACIÓN FM - TIEMPO]

En frecuencia, dependiendo de cómo sea la relación entre los períodos de las dos señales con las que estamos operando, los armónicos generados respetarán, valga la redundancia, una relación armónica. Si en cambio los períodos de las señales propuestas no cumplen esta proporción, se generarán sonidos inarmonicos, lo cual permite la síntesis de sonidos percusivos.

[GRÁFICOS DE LOS ESPECTROS EN FRECUENCIA PARA CADA CASO]

Información más detallada sobre el método está disponible en las referencias [1] y [2] (capítulo sobre síntesis FM únicamente).

## Breve introducción a redes neuronales artificiales

Una red neuronal es, a grandes rasgos, un sistema compuesto por distintos bloques, llamados neuronas. Estas neuronas están compuestas por una serie de parámetros (los coloquialmente llamados *pesos* de la red) y una función no lineal, que se llama función de activación. Las neuronas se conectan entre sí, en muchos casos variando la dimensión de los datos sobre los que operan (un vector de 100 muestras se puede reducir a uno de 50, por ejemplo). Lo interesante de modelos de este tipo es su capacidad de adaptarse a cuerpos de datos propuestos por el usuario, con el objetivo de cumplir una tarea determinada. Esto se logra buscando la minimización de una función, que llamaremos función de costo. Podemos pensar a esta última como un error que hay que minimizar, lo cual implica que nuestro modelo está *aprendiendo* satisfactoriamente la tarea que le propusimos. Un ejemplo muy sencillo de una red neuronal se puede ver en la siguiente figura:

![Perceptrón multi capa](./imgs/mlp.png "Red neuronal básica de tres capas de neuronas, tomado de [3]")

Para entrenar una red de este tipo se debe recurrir al algoritmo de propagación del error hacia atrás (o *backpropagation*, como se lo conoce por su nombre en inglés). Este algoritmo consiste en pasarle a la red una instancia de entrenamiento, realizar una predicción, medir el error cometido, luego ir capa por capa en reversa midiendo la contribución de cada conexión al error y finalmente hacer ligeras correcciones a los pesos de conexión de las distintas neuronas a fin de minimizar el error cometido.

Con estos conceptos presentados muy por arriba debería alcanzarles para entender los temas de aprendizaje automático que se tratan en el trabajo, pero si tienen curiosidad por aprender más sobre el tema, un libro muy bueno es el de la referencia [3].

## El Yamaha DX7

En los 80's Yamaha puso en práctica las ideas de síntesis FM que repasamos antes. Quizás el equipo más representativo de esta camada y uno de los ¿culpables? del sonido de esta década es el Yamaha DX7. Discos como Parte de la Religión y Piano Bar, la banda sonora de Twin Peaks o canciones como Take on me, Never gonna give you up o Out of touch usaron este sintetizador y suenan como suenan gracias a él. 

![Yamaha DX7 y dos amateurs](./imgs/dx7_charly.jfif "Yamaha DX7 en uso")

El Yamaha DX7 tiene 6 osciladores y un usuario genera sonidos combinándolos de distintas formas (en cascada o en paralelo), en lo que se conoce como un *patch*. Además, también se puede modificar la envolvente de la señal mediante generadores de envolvente, y se pueden seleccionar las relaciones de frecuencia entre los distintos osciladores. Entre los patch más clásicos, podemos mencionar los de violín, trompeta y flauta, que se muestran a continuación:

![Patches para violín, trompeta y flauta](./imgs/patches_dx7.png "Patches de un DX7, los cuadrados representan osciladores y los números son los ratios de frecuencia")

## El TP (por fin)

La idea del trabajo práctico que les proponemos es emular los resultados del trabajo de Franco Caspe [4], en donde se sintetiza audio usando una red neuronal que aprende los parámetros óptimos de un patch de síntesis FM como los que vimos antes. La técnica en la que está basada este trabajo se llama Procesamiento de Señales Diferenciable (DDSP, por sus siglas en inglés) [5], y tiene varios beneficios sobre otras técnicas de generación de audio basadas en redes neuronales, que les dejamos a ustedes para investigar.

El esquema general del modelo propuesto por Caspe se puede ver a continuación:

![Arquitectura del modelo DDX7, en rojo el cálculo de pitch, loudness, el algorítmo de síntesis FM y la función de costo](./imgs/arquitectura.png "Arquitectura del modelo DDX7 y bloques sobre los que se trabajará (en rojo)")

de todo el modelo, solo deben modificar los bloques sombreados en rojo. Además de este enunciado les proporcionamos un esqueleto del código [LINK AL ESQUELETO], con la parte relacionada a la parte de aprendizaje automático resuelta (no es necesario que sepan nada de ese campo para realizar este trabajo, solo conceptos a gran escala como los que mencionamos anteriormente).

En el caso de este trabajo nos concentraremos en la emulación de sonidos de violín únicamente, les dejamos los datos necesarios para el entrenamiento del modelo [LINK A DATASET].

La idea del trabajo es que completen los distintos scripts siguiendo las ideas del trabajo de Caspe, variaciones de ellas o ideas propias. Es muy importante que respeten los tipos de dato y las cantidades de variables de entrada y salida que se especifican en cada parte del esqueleto; todo está documentado, pero ante la duda consulten antes de dar cosas por sentado.

El orden de las tareas que deberían llevar a cabo es:

    - 
    -
    -

El desarrollo de su trabajo tiene que verse en un informe que siga el formato propuesto [LINK AL FORMATO], cumpliendo con todas las secciones que en él se detallan. 

Es muy importante que hagan este trabajo con mucho tiempo, además de la dificultad que presenta el problema planteado, muchas de las etapas son computacionalmente intensas, por lo que el proceso de pruebas va a ser largo y algo tedioso. Definitivamente no es un trabajo para hacer en un par de días (es literalmente imposible).

## Condiciones para la entrega

El trabajo puede realizarse en grupos de hasta 4 personas. Además de la entrega del trabajo completo se les pide una pre-entrega, que corresponde a una versión parcial del trabajo (secciones de Introducción, Marco teórico y Desarrollo experimental). No es necesario adjuntar código en esta etapa.

La fecha de la pre-entrega es el **xx de xxxx**, mientras que la fecha de la entrega final es el **xx de xxxx**. No se aceptarán entregas finales fuera de esta fecha y entregas parciales fuera de término serán penalizadas con **x** puntos cada **x** días de entrega tarde.

## Referencias

[1] Chowning, J. M. (1977). The Synthesis of Complex Audio Spectra by Means of Frequency Modulation. Computer Music Journal, 1(2), 46–54. http://www.jstor.org/stable/23320142 [LINK]
[2] Sean L. (2021). Computational Music Synthesis, first edition, available for free at http://cs.gmu.edu/∼sean/book/synthesis/ [LINK]
[3] Géron, A. (2019). Hands-on machine learning with Scikit-Learn, Keras and TensorFlow: concepts, tools, and techniques to build intelligent systems (2nd ed.). O’Reilly. 
[4] Caspe, F., McPherson, A., & Sandler, M. (2022). DDX7: Differentiable FM Synthesis of Musical Instrument Sounds. Proceedings of the 23rd International Society for Music Information Retrieval Conference. [LINK]
[5] Engel, J, Hantrakul, L.H., Gu, C. & Roberts, A. (2020). DDSP: Differentiable Digital Signal Processing. Proceedings of the 8th International Conference on Learning Representations. [LINK]



