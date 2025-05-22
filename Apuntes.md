## Apuntes de python para certificacion de COURSERA:

### MODULOS:

* **Modulo ``sys``**: Importa funciones y variables específicas del Sistema. Algunos ejemplos pueden ser:

    - ``sys.argv``: Lee los argunmentos de la línea de comandos.
    - ``sys.stdout``: Controla salida estándar. Utilizado para redirigir salida a archivos o logs.
    - ``sys.stin``: Da acceso a entrada estándar.
    - ``sys.sterr``: Muestra los errores en un flujo separado.
    - ``sys.exit``: Terminar un programa de forma inmediata.
    - ``sys.path``: Da una lista de rutas en las que poder buscar módulos. Ejemplo: ``sys.path.append("/ruta/a/modulos")``.

* **Modulo ``re``**: Modulo de Python referente a expresiones regulares, es necesario importarlo. Una expresión regular es una secuencia de carácteres que definen un patrón de busqueda.
Ejemplos:


``search``: Busca un patron de carácteres especificos dentro de un string. Hay algunas secuencias de carácteres que pueden utilizarse como patrones comodín:

| Special Sequence | Meaning                 | 	Example             |
| -----------  | ----------------------- | ----------------------|
| \d|Matches any digit character (0-9)|"123" matches "\d\d\d"|
|\D|Matches any non-digit character|"hello" matches "\D\D\D\D\D"|
|\w|Matches any word character (a-z, A-Z, 0-9, and _)|"hello_world" matches "\w\w\w\w\w\w\w\w\w\w\w"|
|\W|Matches any non-word character|	"@#$%" matches "\W\W\W\W"|
|\s|Matches any whitespace character (space, tab, newline, etc.)|"hello world" matches "\w\w\w\w\w\s\w\w\w\w\w"|
|\S|Matches any non-whitespace character|"hello_world" matches "\S\S\S\S\S\S\S\S\S\S\S"|
|\b|Matches the boundary between a word character and a non-word character|"cat" matches "\bcat\b" in "The cat sat on the mat"|
|\B|Matches any position that is not a word boundary|"cat" matches "\Bcat\B" in "category" but not in "The cat sat on the mat"|

``group``: Regagrupa conjuntos de carácteres que han coincidido con la expresión regular. Se suele utilizar despues de haber utilizado la función ``search`` para agrupar el conjunto de carácteres, si ha habido alguna coincidencia:
```
agrupation = matched_string.group()
```

``findall``: Encuentra todas las concurrencias que pueda tener un patrón especifico que queremos encontrar dentro de un string:
```
all_found = re.findall("st",total_tring)
```

``split``: Fracciona un string en un array, o substring, basandose en un patron indicado:
```
splited_str = re.split(r"\s",total_tring)
```

``sub`` : Remplaza patrones de carácteres por otros dentro de un string:
```
corrected_str = re.sub("To be corrected","correction",total_string)
```

----

**String Stride:** Obtención de multiples carácteres de un mismo string indicando la periodicidad con la que se extraen dichos caracters. 
Ejemplos:

    ```
    name = "The Bodyguard"

    name[::2] = "TeBdgad"   #Obtenemos 1 carácter cada 2 carácteres

    name[::3] = "T dud"     #Obtenemos 1 carácter cada 3 carácteres
    ```
    En el *stride* se incluye por defecto el primer carácter del string total.

**Secuencias de escape:** Combinación de ``\`` y un carácter, que genera algo especial. 
Ejemplos:
    
    - ``\n``: Salto de línea.
    - ``\t``: Tabulación.

----

### OOP:

Hay ciertas diferencias en la forma de llamar a un **modulo** de una clase y a un **atributo** de un objeto:
```python
object_from_class.module() # Así llamamos a un módulo

object_from class.attribute # Así llamamos a un atributo
```

De igual forma, la referencia `self` dentro de una misma clase se utiliza cuando queremos almacenar un atributo, o metodo, generado dentro de otro metodo, o para poder referenciar a otro metodo definido en el exterior del metodo desde el que pretendemos referenciarlo. Un ejemplo:

```python
class Persona(object):
    def __init__(self, nombre):
        self.nombre = nombre  # atributo de instancia

    def saludar(self):
        print("Hola, soy", self.nombre)  # accede al atributo con self.nombre
```

---

### **Analisis de Texto:**

Entendemos `Analisis de texto` como la forma de extraer información relevante de textos. Como ejemplo de este proceso, hay un *Jupyter Notebook* en el repositorio, se puede encontrar en la ruta `Jupyter_Notebook/TextAnalysis_Task.ipynb`.

Aclarar que el analisis de texto se compone de 3 pasos:

  1. **Eliminación de carácteres extraños**, carácteres no alfanumericos.
  2. **Normalización del texto**, estandarizar el contenido de dicho texto, dejandolo todo igual para que no haya errores de identificación por mayusculas o minúsculas.
  3. **Analisis del texto**. Una vez ya se ha normalizado todo, podemos proceder.


### PANDAS:

Utilidades en pandas:

```python
import pandas as pd

page_data.columns = range(page_data.shape[1]) 
                                      # Así quitamos posibles nombres raros nombres a las columnas,
                                      # y pasan a tener números:
                                      # 
                                      # data = {'A': [1, 2], 'B': [3, 4], 'C': [5, 6]}
                                      # df = pd.DataFrame(data)
                                      #
                                      # df.shape              # (2, 3) → 2 filas, 3 columnas
                                      # df.shape[1]           # 3
                                      # range(df.shape[1])    # range(0, 3) → [0, 1, 2]
                                      #
                                      # df.columns            #    1  2  3
                                      #                       #  0 1  3  5
                                      #                       #  1 2  4  6


# Rename the column header from 'GDP (Million USD)' to 'GDP (Billion USD)':
df.rename(columns = {'GDP (Million USD)' : 'GDP (Billion USD)'})
```

