# Guía 0 - Programación

1.  Evalúe las siguientes operaciones en la consola interactiva, dándole especial atención al tipo de dato resultante en cada caso

    ??? info "Consola interactiva"

        Con **consola interactiva** nos referimos a la ventana interactiva de Jupyter, donde se puede ejecutar código
        Python y ver el resultado de las operaciones.
        
        Para acceder a la consola interactiva, en VS Code se debe presionar la combinación de teclas `Ctrl + Shift + P` (o `Cmd + Shift + P` en Mac) y seleccionar `Jupyter: Create Interactive Window`.
        ***Nota:*** *Si no se tiene instalada la extensión de Python y Jupyter, se debe instalar desde la tienda de extensiones de VS Code.*
    ??? info "Ojo"

        Algunas de las operaciones pueden resultar en errores de ejecución, investigue por qué (vale para toda la guía).



    1. `1 + 3`
    1. `1.0 + 3`
    1. `'Procesamiento ' + ' de' + ' Señales'`
    1. `'Procesamiento' * 3`
    1. `0.1 + 0.5`
    1. `4 * 5`
    1. `5 / 2`
    1. `5 // 2`
    1. `'a' == 'A'`
    1. `10 == '10'`
    1. `25 == True`
    1. `0 == False`
    1. `'PDS' == True`
    1. `'' == False`

1.  Evalúe los siguientes pares de operaciones en la consola interactiva, dándole especial atención al tipo de dato resultante en cada caso. 

    ```python
       numeros = [1,2,4,5]
       numeros[2] = 1
    ```
    ```python
       numeros = [1,2,4,5]
       numeros[30] = 1
    ```
    ```python
       numeros = [1,2,4,5]
       numeros[:2] = 0
    ```
    ```python
       numeros = [1,2,4,5]
       numeros[2:] = 1
    ```
    ```python
       numeros = [1,2,4,5,6,7,8,9,10]
       numeros[::2]
    ```
    ```python
       numeros = [1,2,4,5,6,7,8,9,10]
       numeros[0::2]
    ```
    ```python
       numeros = [1,2,4,5,6,7,8,9,10]
       numeros[0:-1:2]
    ```
    ```python
       numeros = [1,2,4,5,6,7,8,9,10]
       numeros[0:8:2]
    ```
    ```python
       numeros = [1,2,4,5,6,7,8,9,10]
       numeros[::-1]
    ```
    ```python
       numeros = [1,2,4,5,6,7,8,9,10]
       numeros[4]
    ```
    ```python
       numeros = [1,2,4,5,6,7,8,9,10]
       numeros[-5]
    ```

1.  Evalúe los siguientes pares de operaciones en la consola interactiva, dándole especial atención al tipo de dato resultante en cada caso. 

    ```python
       numeros = (1,2,4,5)
       numeros[2] = 1
    ```
    ```python
       numeros = (1,2,4,5)
       numeros[30] = 1
    ```
    ```python
       numeros = (1,2,4,5)
       numeros[:2] = 0
    ```
    ```python
       numeros = (1,2,4,5)
       numeros[2:] = 1
    ```
    ```python
       numeros = (1,2,4,5,6,7,8,9,10)
       numeros[::2]
    ```
    ```python
       numeros = (1,2,4,5,6,7,8,9,10)
       numeros[0::2]
    ```
    ```python
       numeros = (1,2,4,5,6,7,8,9,10)
       numeros[0:-1:2]
    ```
    ```python
       numeros = (1,2,4,5,6,7,8,9,10)
       numeros[0:8:2]
    ```
    ```python
       numeros = (1,2,4,5,6,7,8,9,10)
       numeros[::-1]
    ```
    ```python
       numeros = (1,2,4,5,6,7,8,9,10)
       numeros[4]
    ```
    ```python
       numeros = (1,2,4,5,6,7,8,9,10)
       numeros[-5]
    ```

1.  Los siguientes bloques de código no se ejecutan correctamente. Identifiqe y corrija los errores guiándose por las alertas que aparecen en la consola.

    1.  Se requiere imprimir en consola cada medición de 20 muestras que está dentro de la matriz *mediciones*, las cuales corresponden a las **filas** de la matriz.
    ```python
    import numpy as np
    
    mediciones = np.random.random(size = (5,20))    
    
    for i in 5:
        print(f'Medicion nº: {i}')
        print(mediciones[:,i])
    ```

    1.  Se requiere guardar el valor máximo y mínimo de cada medición en las variables *mediciones_max* y *mediciones_min* respectivamente.  
  
    ??? info "Opcional"
        Se puede resolver sin necesidad de usar un ciclo *for* utilizando el parámetro **axis** en las funciónes de máximo y mínimo

    ```python
    import numpy as np
    
    mediciones = np.random.random(size = (5,20))    
    n_mediciones = '5'
    
    for i in n_mediciones:
        mediciones_max[i] = mediciones[i].max
        mediciones_min[i] = mediciones[i].min
    ```

1.  Escriba funciones que:

    1.  Dado un tiempo en segundos devuelva el tiempo equivalente en horas, minutos y segundos en el formato hh: mm :ss. La variable de salida debe ser un string.

    ??? info "Opcional"
        Mediante un argumento opcional en la función, permita que se pueda elegir el tipo de dato de la variable de salida, que podrá ser un string (siguiendo el formato descripto) o una lista, en donde cada elemento corresponda a uno de los campos de interés.

    1.  Asumiendo que se tiene una variable que contiene un tiempo en horas, minutos y segundos siguiendo el formato de la función anterior, devuelva el tiempo equivalente en segundos. La variable de salida debe ser de tipo float.

1.  Escriba una función que reciba como parámetro de entrada el directorio en donde está almacenado un archivo de audio en formato WAV. Si el archivo en cuestión está en formato estéreo (dos canales), la función debe convertirlo a mono y devolver dicha señal como parámetro de salida. El método de pasaje de un formato a otro queda a su criterio, pero debe ser claramente explicado en la documentación de la función. En el caso en el que el archivo de audio a cargar ya esté en formato mono, se debe imprimir por consola un mensaje de aviso y la función debe devolver la señal tal cual se cargó.

    ??? info "Opcional"
        Proponer varios métodos de pasaje de estéreo a mono, y permitir al usuario elegir qué método utilizar mediante un parámetro opcional.

    A continuación se deja un bloque de código a modo de ejemplo de cuales deberían ser los pasos para desarrollar la función. En las secciones punteadas (...) deberán escribir las sentencias correspondientes. Al inicio de la función se escribe la documentación de la función, también llamado _docstring_, en donde se explica qué hace la función, sus variables de entrada y salida, indicando de qué tipo son.

    ```python
    def stereo_to_mono(audio_path, mode):
    """_summary_

    Parameters
    ----------
    audio_path : _type_
        _description_
    mode : _type_
        _description_

    Returns
    -------
    _type_
        _description_
    """

    # Audio loading
    audio_array, fs = (...)
    
    # Check if audio is stereo
    if (...):
        # Stereo-to-mono conversion
        (...)
        audio_array = (...)
    
    else:
        print(...)
    
    return audio_array
    ```

1.  Escriba tres funciones distintas (con sus correspondientes documentaciónes) que permitan calcular los siguientes parámetros estadísticos en función de un vector de entrada.

    ??? info "Opcional"
        Para mejorar la legibilidad del código puede usar el resultado de una función dentro de otra (por ejemplo, en el cálculo del desvío estandar, se requiere el valor medio de la señal)

    1. Valor medio: $\mu = \frac{1}{N}\sum_{n=0}^{N-1}x[n]$
    1. Desvío estandar: $\sigma = \sqrt{\frac{1}{N-1}\sum_{n=0}^{N-1}|(x[n]-\mu|)^2}$
    1. Valor RMS: $rms = \sqrt{\frac{1}{N}\sum_{n=0}^{N-1}|(x[n])^2|}$


1.  Integre las funciones del punto anterior a la clase **AudioStats()**, donde ahora la variable de entrada **audio_array** será un atributo de la clase, mientras que las funciones que calculen los parámetros estadísticos serán sus métodos. Además, se debe añadir un nuevo método que calcule todos los parámetros estadísticos, y devuelva un diccionario cuyas claves sean los nombres de los parámetros mientras que los valores asociados sean los resultados obtenidos.

    En el siguiente bloque se deja un ejemplo de la estructura de la clase solicitada para completar en los espacios punteados (...) con su código.

    ```python
    class AudioStats():
    ### Attributes
    def __init__(self, audio_array):
        
        self.audio_array = (...)
    
    ### Methods
    def mean(self):
        (...)
    
    def std_desv(self):
        (...)
    
    def rms(self):
        (...)
        
    def get_stats(self):
        (...)
        
        stats = {
            'mean': (...),
            'std_desv': (...),
            'rms': (...)
        }
        
        return stats
    ```

1.  Escriba un script que genere secuencias de números aleatorios de media nula y desvío unitario (puede usar funciones incluidas en paquetes). Genere 5 secuencias, de largo 5, 10, 100, 1000 y 10000. Mediante las funciones escritas en el punto 9, verifique que los requerimientos que impuso durante la generación de las señales referidas a la media y al desvío se cumplan. En los casos en donde esto no suceda, intente explicar qué está pasando.

1.  Escriba una función que genere la siguiente secuencia discreta de largo N:

    $$ x[n] = a_0 - a_1 \cos{\left(\frac{2\pi n}{N-1}\right)} +a_2 \cos{\left(\frac{4\pi n}{N-1}\right)}$$

    en donde $a_0 = 0.42$, $a_1 = 0.5$ y $a_2 = 0.08$. La función debe tener un parámetro opcional que indique mediante un booleano (verdadero o falso) si la señal debe graficarse o no cuando se invoque la función. El gráfico debe tener títulos en los ejes.

1.  Escriba un script que genere las siguientes secuencias de 44000 muestras:

    $$ y_1[n] = 2 $$

    $$ y_2[n] = \cos{(2\pi f_2 n)}e^{-\frac{(t-\mu_2)^2}{2\sigma_{2}^2}} \;\;f_2 = 10000 \; \mu_2 = 0.2 \; \sigma_2 = 0.05 $$

    Graficar ambas señales en un mismo entorno de figura, utilizando un par de ejes distinto para cada secuencia (puede servir el concepto de subplots para esto). Por otro lado, en otro entorno de figura, graficar las dos señales juntas. Este último gráfico tiene que tener la leyenda que identifique a cada secuencia.

1.  Escriba una función que tome como parámetros de entrada a una secuencia numérica y a un string que represente un directorio, y guarde dicha señal como un archivo de audio en formato .wav.

1.  Escriba una función que convolucione linealmente dos señales y guarde el resultado como un archivo .wav en un directorio determinado por el usuario. Para probar, invoque a su función usando las señales $y_2$ del punto 12 y $x[n]$ del punto 11. 

1.  Escriba una función que reciba una señal de audio y la divida en segmentos de un largo definido por el usuario. Cada uno de estos segmentos puede o no estar solapado con los contiguos. Opcionalmente se debe poder ingresar una segunda secuencia, de largo igual al de cada bloque, que se utilizará para multiplicar punto a punto segmentos conseguidos. Esta operación se denomina _ventaneo_.

1.  Escriba una función que calcule la relación señal a ruido de una señal según la siguiente expresión:

    $$SNR = \frac{A}{\sigma_{ruido}}$$

    en donde $A$ corresponde a la amplitud de la señal, mientras que $\sigma_{ruido}$ es el desvío estandar del ruido presente en la señal. Proponga un método para detectar sectores de la secuencia de entrada en donde el ruido sea preponderante (para poder calcular su desvío). Evalúe su función sobre el archivo de audio. Una buena idea sería que el audio corresponda a una conversación, aprovechando los silencios.

1.  Cree una clase llamada *FeatureExtractor()*, la cual se deba inicializar con un vector de audio o con el path del audio a analizar, y que tenga como atributos el vector de la señal, su frecuencia de muestreo y su largo en cantidad de muestras. Sus métodos deben ser funciones que calculen parámetros temporales de la señal, como por ejemplo: _Short Time Energy_, _Zero Crossing Rate_ y _Energy Entropy_.

    ```python
    class FeatureExtractor():
    ### Attributes
    def __init__(self, audio_array = None, fs = None,  audio_path = None):
        
        if audio_path is not None:
            self.audio_array, self.fs = (...)
        else:
            self.audio_array = audio_array
            self.fs = fs
        
        self.len = (...)
    
    ### Methods
    def short_term_energy(self):
        (...)
    
    def zero_crossing_rate(self):
        (...)
    
    def energy_entropy(self):
        (...)
    ```
