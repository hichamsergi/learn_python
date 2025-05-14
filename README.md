# APUNTES PYTHON:

Los tipos de datos en Python son los siguientes:

### 1. **Integer (int)**:
   - Números enteros positivos o negativos sin parte decimal.
   - Ejemplo: `5`, `-10`, `0`.
   - **`int()`**: Convierte un valor a entero si es posible.

   - **Operaciones**:
     - Suma: `a + b`.
     - Resta: `a - b`.
     - Multiplicación: `a * b`.
     - División (float): `a / b`.
     - División entera: `a // b`.
     - Potencia: `a ** b`.
     - Módulo: `a % b`.

### 2. **Float (float)**:
   - Números en coma flotante, es decir, que contienen una parte decimal.
   - Ejemplo: `3.14`, `-0.001`, `2.0`.
   - **`float()`**: Convierte un valor a flotante si es posible.


### 3. **String (str)**:
   - Cadenas de texto que se representan entre comillas simples o dobles.
   - Ejemplo: `"Hola"`, `'Mundo'`, `"123"`.
   - **Funciones útiles**:
     - **`len()`**: Devuelve la longitud de la cadena.
     - **`upper()`**: Convierte la cadena a mayúsculas.
     - **`lower()`**: Convierte la cadena a minúsculas.
     - **`split()`**: Divide la cadena en una lista según un delimitador.
     - **`join()`**: Une elementos de una lista en una cadena usando un delimitador.
     - **`find()`**: Encuentra el indice del primer elemento. ``name.find("world")``
     - **`replace()`**: Remplaza el primer elemento por el segundo. ``name.replace("Joan","Hicham")`` 

### 4. **Boolean (bool)**:
   - Valores lógicos que solo pueden ser `True` o `False`.
   - Ejemplo: `True`, `False`.

---   

### 5. **Listas (List)**
Una lista en Python es una colección ordenada, mutable y que permite elementos duplicados. Esto significa que podemos agregar, eliminar o modificar elementos en una lista después de haberla creado. Además, las listas pueden contener elementos de diferentes tipos.

#### Ejemplos:
```python
# Crear una lista
mi_lista = [1, 2, 3, "Python", True]

# Acceder a un elemento por su índice
print(mi_lista[0])  # Output: 1

# Modificar un elemento
mi_lista[1] = "Data Science"

# Añadir elementos
mi_lista.append(42)

# Eliminar elementos
mi_lista.remove("Python")

# Slice (subconjuntos)
print(mi_lista[1:3])  # Output: ['Data Science', 3]

# Comprobar si un elemento está en la lista
print(42 in mi_lista)  # Output: True
```

#### Funciones útiles:
- **`append()`**: Agrega un elemento al final de la lista.
- **`remove()`**: Elimina la primera ocurrencia de un elemento.
- **`pop()`**: Elimina y retorna el último elemento (o el que esté en el índice especificado).
- **`sort()`**: Ordena la lista en su lugar (puede ser ascendente o descendente).
- **`sorted()`**: Devuelve una lista con la secuencia de elementos ordenada, sin modificar la lista original.
- **`reverse()`**: Invierte el orden de los elementos.

#### Ejemplos de funciones:
```python
# Invertir una lista
mi_lista = [1, 2, 3, 4]
mi_lista.reverse()  # Output: [4, 3, 2, 1]

# Ordenar una lista de números
mi_lista = [4, 2, 1, 3]
mi_lista.sort()  # Output: [1, 2, 3, 4]
```

---

### 6. **Tuplas (Tuple)**
Una tupla es similar a una lista, pero es **inmutable**, lo que significa que no se puede modificar después de su creación. Se utilizan cuando no necesitamos cambiar los elementos una vez definidos.

#### Ejemplos:
```python
# Crear una tupla
mi_tupla = (1, 2, 3, "AI", False)

# Acceder a un elemento
print(mi_tupla[0])  # Output: 1

# Desempaquetar una tupla
a, b, c, d, e = mi_tupla
print(a)  # Output: 1

# Crear una tupla con un solo elemento (notar la coma)
una_tupla = (5,)
```

#### Funciones útiles:
- **`count()`**: Devuelve el número de veces que un valor aparece en la tupla.
- **`index()`**: Devuelve el índice de la primera aparición de un valor.

#### Ejemplo:
```python
# Contar cuántas veces aparece un valor
mi_tupla = (1, 2, 3, 2, 2)
print(mi_tupla.count(2))  # Output: 3

# Encontrar el índice de un valor
print(mi_tupla.index(3))  # Output: 2
```

---

### 7. **Conjuntos (Set)**
Un conjunto en Python es una colección **desordenada** de elementos **únicos**. Esto significa que no admite duplicados y no mantiene un orden específico.

#### Ejemplos:
```python
# Crear un conjunto
mi_conjunto = {1, 2, 3, 4}

# Añadir un elemento
mi_conjunto.add(5)

# Eliminar un elemento
mi_conjunto.remove(2)

# Convertir una lista a conjunto para eliminar duplicados
lista = [1, 2, 2, 3, 4, 4]
conjunto_unico = set(lista)  # Output: {1, 2, 3, 4}
```

#### Operaciones útiles:
- **`union()`**: Devuelve la unión de dos conjuntos.
- **`intersection()`**: Devuelve la intersección (elementos comunes).
- **`difference()`**: Devuelve la diferencia entre dos conjuntos.
- **`issubset()`**: Devuelve `True` si el conjunto es un subconjunto de otro.
- **`issuperset()`**: Devuelve `True` si el conjunto es un superconjunto de otro.

#### Ejemplo de operaciones:
```python
A = {1, 2, 3}
B = {3, 4, 5}

# Unión
print(A.union(B))  # Output: {1, 2, 3, 4, 5}

# Intersección
print(A.intersection(B))  # Output: {3}

# Diferencia
print(A.difference(B))  # Output: {1, 2}

# Comprobar si es un subconjunto
C = {1, 2}
print(C.issubset(A))  # Output: True
```

---

### 8. **Diccionarios (Dictionary)**
Un diccionario es una colección de pares **clave-valor** en la que cada clave debe ser única. Se accede a los valores a través de las claves, no por su posición como en listas o tuplas.

#### Ejemplos:
```python
# Crear un diccionario
mi_diccionario = {"nombre": "Juan", "edad": 25, "profesion": "Ingeniero"}

# Acceder a un valor por su clave
print(mi_diccionario["nombre"])  # Output: Juan

# Añadir una nueva clave-valor
mi_diccionario["pais"] = "España"

# Eliminar un par clave-valor
del mi_diccionario["edad"]

# Obtener solo las claves
print(mi_diccionario.keys())  # Output: dict_keys(['nombre', 'profesion', 'pais'])

# Obtener solo los valores
print(mi_diccionario.values())  # Output: dict_values(['Juan', 'Ingeniero', 'España'])
```

#### Funciones útiles:
- **`keys()`**: Devuelve una vista de las claves del diccionario.
- **`values()`**: Devuelve una vista de los valores del diccionario.
- **`items()`**: Devuelve una vista de pares clave-valor.
- **`get()`**: Obtiene el valor de una clave sin causar un error si la clave no existe.
- **`update()`**: Actualiza un diccionario con pares clave-valor de otro diccionario.

#### Ejemplo de uso:
```python
# Actualizar un diccionario con otro
mi_diccionario.update({"edad": 30, "ciudad": "Madrid"})

# Obtener un valor con get (evita errores si la clave no existe)
print(mi_diccionario.get("nombre", "No encontrado"))  # Output: Juan
```
----------------
### **Funciones**

Las funciones son bloques de código reutilizable que ejecutan ciertas operaciones descritas en el interior de dicha función. Hay dos tipos de funciones, **las predefinidas** y **las definidas por el usuario**.

#### Como definir una función:
```python
def add(a):
  """
  Sumar 1 a un número proporcionado, "a"
  """
  a += 1

  return(a)
```
Podemos obtener información del funcionamiento de la función, definido en el comentario previo al bloque de codigo, utilizando ``help(add)``. Esto nos mostrará:
```
Sumar 1 a un número proporcionado, "a"
```


----------------

### **Manejo de Excepciones**

Para manejar posibles errores, y administrar el codigo de una mejor forma, python permite el _manejo de excepciones_. De esta forma pretendemos que nuestro codigo identifique situaciones inesperadas durante su ejecución, para que estas no lo interrumpan accidentalmente:

#### **Errores vs. Excepciones**
- **Errores**: Son problemas serios del sistema, como problemas con el hardware o el sistema operativo, que suelen hacer que el programa deje de funcionar.

- **Excepciones**: Son problemas menos graves, causados por el código, que pueden manejarse para que el programa siga ejecutándose.

#### **Excepciones comunes en Python**
- **ZeroDivisionError**: Ocurre al intentar dividir entre cero.
  ```python
  result = 10 / 0  # Genera ZeroDivisionError
  ```
- **ValueError**: Se genera cuando se proporciona un valor incorrecto a una función.
  ```python
  num = int("abc")  # Genera ValueError
  ```
- **FileNotFoundError**: Se genera al intentar acceder a un archivo que no existe.
  ```python
  with open("no_existe.txt", "r") as file:  # Genera FileNotFoundError
  ```
- **IndexError**: Ocurre cuando se intenta acceder a un índice fuera del rango de una lista.
  ```python
  my_list = [1, 2, 3]
  missing = my_list[5]  # Genera IndexError
  ```
- **KeyError**: Ocurre al intentar acceder a una clave inexistente en un diccionario.
  ```python
  my_dict = {"name": "Alice"}
  missing = my_dict["age"]  # Genera KeyError
  ```
- **TypeError**: Ocurre cuando se usan tipos de datos de forma incompatible.
  ```python
  result = "hello" + 5  # Genera TypeError
  ```
- **AttributeError**: Ocurre al intentar acceder a un atributo o método inexistenten1 / (n1-5) de un objeto.
  ```python
  text = "ejemplo"
  missing = text.some_method()  # Genera AttributeError
  ```
- **ImportError**: Se genera al intentar importar un módulo inexistente.
  ```python
  import non_existent_module  # Genera ImportError
  ```

#### **Como manejar las excepciones?**
Python proporciona la estructura `try-except` para gestionar excepciones y evitar que el programa se detenga bruscamente.

- **`try`**: Se coloca el código que puede generar una excepción.
- **`except`**: Se maneja la excepción que haya ocurrido.
  
**Ejemplo:**
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: No se puede dividir por cero")
print("Continuamos con el programa")
```
Como forma complementaria a la estructura mencionada previamente existen las formas de ejecución `else` y `finally`:

 - **`else`**: Se ejecuta solo si no ocurre ninguna excepción.
 - **`finally`**: Se ejecuta siempre, ocurra o no una excepción, y es útil para tareas de limpieza, como cerrar un archivo o liberar memoria.

 **Ejemplo:**
 ```python
try:
    # Código que puede generar una excepción
    result = 10 / 2
except ZeroDivisionError:
    # Si ocurre una excepción, se maneja aquí
    print("Error: No se puede dividir por cero.")
else:
    # Si no ocurre ninguna excepción, se ejecuta este bloque
    print("La división fue exitosa:", result)

finally:
    # Este bloque siempre se ejecuta
    print("Bloque 'finally' ejecutado.")
 ```

---

### **Programación Orientada a Objetos (OOP):**

Es un paradigma de la programación que pretende organizar el codigo en **objetos**, los cuales representan elementos del mundo real. Los objetos tienen **atributos**, cualidades que contienen datos, los cuales son definidos en las **clases**, lo que podríamos definir como los moldes que estructuran los atributos de los objetos. Dentro de las clases, a parte de atributos, podemos definir funcionalidades para los objetos, llamadas **métodos**. Ejemplo:

```python

# Ejemplo de clase:
class Car(object):

    def __init__(self, color, velocidad): # Metodo constructor, definimos los atributos base
        self.color = color  # Atributo de modulo
        self.velocidad = velocidad

    def acelerar(self, incremento):
        self.velocidad += incremento
        print(f"Velocidad actual: {self.velocidad} km/h")

# Creando un objeto de la clase Car
mi_auto = Car("rojo", 50)

#Haciendo uso de la funcionalidad acelerar, para aumentar el atributo velocidad:
mi_auto.acelerar(20)
```

#### Atributos de clase *vs* Atributos de instancia:

* **Atributos de clase:** Se comparten con todos los demas objetos de una misma clase. Se tinen fuera de cualqueir método.

* **Atributos de instancia:** Son atributos unicos para cada y se definen en el método `__init__`.

```python
class Car(object):

  color = "rojo" #atributo de clase

  def __init__(self, color, velocidad):
      self.color = color  # atributo de instancia
      self.velocidad = velocidad

# Acceso directo al atributo de velocidad del objeto mi_auto asignandole una velocidad:
mi_auto.velocidad = 50
```

#### Método ```__init__```

El metodo `__init__` inicializa los atributos para crear un objeto, también es llamado metodo constructor. Podemos asignar valores por defecto a los atributos de instancia:

```python
class Car(object):

  # __init__ con valores por defecto:
  def __init__(self, color="red", velocidad=0):
      self.color = color
      self.velocidad = velocidad

#Objeto con valores asignados:
coche1 = Car("blue", 120)
#Objeto con valores por defecto, coche2 será de color rojo y tendrá velocidad 0:
coche2 = Car()
```

El resto de métodos que no sean `__init__` operan sobre los atributos que se le han asignado al objeto en dicho método inicial:

```python
class Car(object):

  def __init__(self, color="red", velocidad=0):
      self.color = color
      self.velocidad = velocidad
  
  #Método para acelerar el coche:
  def acelerar(self, acelerar):
      self.velocidad += acelerar
      

coche1 = Car("blue", 120)
#Uso del método acelerar:
coche1.acelerar(20)
```

Si queremos comprobar los atributos de un objeto, o de una *clase*, tambien podemos llamarlos de la misma forma, o si preferimos modificarlos también podemos hacerlo:

```python
atributos_clase = car.class_attribute
coche1.velocidad # Mostrará la velocidad actual del coche1
coche1.velocidad = 120 # Establece la velocidad del coche1 en 120 
```

---

### Lectura y Escritura de ficheros:

La lectura de ficheros es una parte esencial de Python que nos permite abrir, leer e interactuar con documentos utilizando funciones propias de Python. Para poder operar con documentos hay que seguir los siguientes pasos:


#### 1. Lectura:


  ##### 1.1 Abrir el documento:

  ```python
  with open('file.txt','r') as file:
  ```
  * `with`: Este metodo nos permite abrir el documento y **cerrarlo automaticamente**, una vez el codigo ejecutado bajo el haya sido completado.

  * `open()`: Esta funcion integrada en Python nos permite abrir `file.txt` com un objeto e interactuar con el.

  * `r`: Este parametro indica el modo en el que abrimos `file.txt`, en este caso lectura. Puede haber diferentes propositos para abrir un documento:

    * `r`: Lectura.
    * `w`: Escritura.
    * `a`: Anexión.

  ##### 2. Leer el contenido:

  ```python
  with open('file.txt','r') as file:

    contenido_file = file.read()
  ```
  Dado que tenemos abierto el documento, con el metodo `with`, ahora podemos leer el contenido con la función `file.read()`. En el caso de que solo queramos leer cierta cantidad de carácteres del documento, el mismo método `file.read(4)`, nos permite indicar la cantidad de carácteres a leer.

  ##### 3. Interactuar con el contenido:
  ```python
  with open('file.txt','r') as file:

    contenido_file = file.read()

    print(contenido_file)
  ```
   Al haber leido el contenido del documento, asignamos todo el contenido a una variable que lo almacenará. Ahora, `contenido_file` conteniene todo el texto que hay en `file.txt`, y podemos hacer con el lo que queramos, como mostrarlo.

  ##### 3.2 Leer el contenido linea a linea:

  Ahora mismo tenemos todo el contenido del documento `file.txt` almacenado en una variable. Pero ese contenido es enorme y podriamos necesitar leer, solo, el contenido línea a línea. Para poder hacer eso necesitariamos la función `readlines()`:

  ```python
  with open('file.txt','r') as file:

    line1 = file.readlines() # Almacenamos la línea 1.
  ```

  La función `readlines()` únicamente lee una línea a la vez. En el caso de querer leer el resto del contenido, tenemos que ser un poco más creativos:

  ```python
  with open('file.txt','r') as file:
    
    while True:
      line = file.readlines()

      if not line: #Esta condición nos indica que ya no hay mas líneas

        break #Devolviendo 'False'
      
      print(line)
  ```

  ##### 3.3 Leer carácteres específicos:

  Hay diferntes utilidades para hace esto:

  ```python
  file.seek(10) # Establecemos el cursor de leectura en la posición 10.
                # Empezará a leer a partir de la posición 10.

  file.read(5) #Lees solo 5 carácteres y finaliza la lectura.
  ```

#### 2. Escritura:

El uso que le podemos dar a este modo de documentos, sería el de crear o sobreescribir documentos con contenido. La forma en la que abrimos los documentos es la misma que el metodo de lectura, lo que cambia es nuestra interacción con el documento:

  ##### 1.2 Abrir el documento:

  ```python
  with open('file.txt','w') as file:
  ```

  * ``'w'``: De esta forma estamos indicando que lo que procede a hacer con file.txt es escribir en el documento.

  ##### 2. Escribir en el documento:
  ```python
  with open('file.txt','w') as file:

    file.write('This is a new line n1\n')
    file.write('This is a new line n2\n')
  ```

  El metodo `write` nos permite escribir contenido en el documentop. En el ejemplo superior lo que tenemos son dos nuevas líneas de texto en el documento file.txt:

  * `file.write('This is a new line n1\n')`: Esto añadirá una nueva linea con el contenido `This is a new line n1`.

  * `\n`: Añadimos la expresión regular a final de líne para hacer el salto a la siguiente línea.

  Sobre este principio podemos iterar en función del contenido que queramos añadir: 

  ```python

  Lines = ["This is line 1", "This is line 2", "This is line 3"] # Generamos una lista con datos

  with open('file.txt','w') as file:

    for line in Lines:
      
      file.write(line+'\n') # Iteramos sobre el contenido de la lista


  ```

#### EXTRA: Añadir datos a un documento:

En el caso de que ya exista el documento y solo queramos añadir contenido al mísmo, utilizamos el modo `a`, qué sería `append`. Ejemplo:
```python
with open('file.txt', 'a') as file:
    file1.write(new_data + "\n")
```

La cominación de uno o varios metodo también es posible, esto es muy practico en el caso de que queramos copiar el contenido de un documento a otro. Sería algo parecido a generar un bucle dentro de otro, ya que debemos de abrir primero de todo, un documento en modo de lectura. Posteriormente, sobre el mismo metodo de lectura, abrimos otro documento pero en metodo de escritura para poder recibir datos de un documento hacia el otro. Ejemplo:
```python
with open('source.txt', 'r') as source_file:

    with open('destination.txt', 'w') as destination_file:

        for line in source_file:
            
            destination_file.write(line)
```

Otros modos interesantes de conocer serían:

* `r+`: Lectura y escritura. No puede reducir el contenido del documento.
* `w+`: Escritura y lectura. Puede eliminar contenido del documento.
* `a+`: Añadir y leer. Si no existe el documento, lo crea.

-------------

### PANDAS:

Pandas es una libreria que contiene un conjunto de funciones predefinidas que son especialmente útiles para el *análisis de datos*. Para poder utilizar dichas funciones en nuestro código, debemos de improtar la libreria:

```python
import pandas as pd # Definimos el acceso a pandas con la abreviatura de "pd"
```

  #### Dataframes:

  Los *dataframes* son un conjunto de datos de dos dimensiones, filas y columnas, que genera Pandas almacenando la información en RAM. Con estas estructuras, podemos generar dataframes de documentos preexistentes, como *.csv* o *.xlsx*. Por ejemplo:

  ```python
  import pandas as pd

  path2_csv = 'text2dataframe.csv'

  new_df = pd.read_csv(path2_csv) # Para leer xlsx sería: pd.read_xlsx()

  new_df.head() # Veríamos las cabeceras de las columnas
  ```

  En cambio si lo que queremos es generar un *dataframe* de un diccionário propio descrito en nuestro código, la función de Pandas *DataFrame()* nos permitiria hacerlo. Ejemplo:

  ```python
  import pandas as pd

  songs_dicc = {'Album':['Thriller','Back in Black','Bat Out of Hell'],
                'Released':[1982,1980,1977],
                'Length':['00:42:19','00:42:11','00:46:33']}

  songs_dataframe = pd.DataFrame(songs_dicc)
  ```

  Ahora podríamos seccionar parte de la información de forma que solo quisieramos ver o mostrar los albumes contenidos en el dataframe descrito previamente. Podemos hacerlo con una simple función:
  
  ```python
  songs_dicc = {'Album':['Thriller','Back in Black','Bat Out of Hell'],
                'Released':[1982,1980,1977],
                'Length':['00:42:19','00:42:11','00:46:33']}

  album_songs = df[['Album']] # Si queremos mas que solo 1 columna bastaría con añadir mas columnas.
  ```

  El acceso a columnas o datos que un dataframe también nos lo permite hacer el metodo `.iloc[]`, *index location*. Con este metodo podemos indicarle el acceso a los datos como si fuera un indice de una lista, dando primero la fila y posteriormente la columna:

  ```python
  df.iloc[0,0] # El output sería Thriller
  df.iloc[0,1] # El output sería 1982
  df.iloc[1,0] # El output sería Back in Black
  ```

  `.loc` tambien es muy útil, ya que podemos poner el nombre de las columnas y filas como indice para buscar datos:

  ```python
  df.loc['a','Album'] # Accede a la posición 3 de la columna Album.
  ```

  ##### Atributos y metodos en Dataframes:

  Alguno de los atributos y datos de datafranes son los siguientes:

  * `shape`: Devuelve las dimensiones del dataframe, numero de filas y columnas. 
  * `info()`: Proporciona información general del dataframe.
  * `describe()`: Genera estadisticas genericas de los valores númericos.
  * `head() / tail()`: Muestra las *n* primeras/últimas filas del dataframe.
  * `mean() / sum() / min() / max()`: Calcula estadisticas de columnas, mediana, suma, mínimo y máximo.
  * `sort_values()`: Ordena el dataframe por una columna o varias columnas.
  * `groupby()`: Agrupa datos por una o mas columnas.
  * `fillna() / drop() / rename()`: Rellenar datos casillas de datos vacias. Elimina y renombra, columnas.

  #### Series:

  Esta estructura de datos de una unica dimensión, es algo similar a una unica columna de un *dataframe*, por lo que solo existe el indice de los datos.

  La forma que tenemos de interactuar con una *serie* es la misma que con los dataframes.

  ------------

### NumPy:

  Es una libreria de python que nos permite manipular datos numéricos de forma eficiente, tales como trabajar con arrays multidimensionales, realizar operaciones matemáticas y estadisticas muy rapidamente.

  #### Numpy array:

  Los *arrays de Numpy* es la estructura de datos esencial de dicha libreria, es muy similar a una lista basica de python, pero con la diferencia de que ejecuta calculos matemáticos potentes de forma rapida. También es importante puntualizar que contiene SOLO datos del mismo tipo, como podrían ser *int* o *float*.

  ```python
  import numpy as np

  e_lista = [1,2,3,4]

  a = np.array([[1,2],[3,4]])

  print(e_lista + e_lista): [1,2,3,4,1,2,3,4] # Devuelve la suma de las listas

  print(a + a): array([[2,4],
                       [6,8]]) # Suma los valores que contienen los arrays

  a.size: 4 # Devuelve la longitud del array
  a.ndim: 2 # Devuelve el número de arrays que contiene 'a'.
  a.shape: (2,2) # Devuelve la forma del arra, el numero de filas y columnas que tiene.
  ```

  #### Numpy index slicing:

  El slicing que podemos hacer, es el mismo que el de una lista ya que es muy similar a ese tipo de estructura de datos:
  
  ```python
  c = np.array([0,1,2,3,4])

  c[0] = 100

  c: array([100,1,2,3,4])

  c[0:2]: array([100,1,2])
  ```

  #### Funciones estadísticas de Numpy:

  Hay ciertas funciones de Numpy que nos permiten extraer datos estadísticos de los arrays que generamos:

  ```python

  import numpy as np

  a = ([1,2,3,4,5])

  a_deviation = a.std() # Nos muestra la desviación estandar del array indicado.

  ```
  ###### *¿Qué es la desviación estándar?*
  Nos indica el promedio de distancia de los diferentes componentes del array respecto a la media del mismo.
  

  #### Numpy basic operations:

  Estas son algunas funciones matemáticas basicas que podemos aplicar sobre arrays:

  ```python
  u = np.array([1,0])
  v = np.array([0,1])

  z = u + v
  z = np.add(u,v) # Es lo mismo que la operación anterior
  z: array([1,1]) # Vector addition

  z = u - v
  z = np.subtract(u,v) # Es lo mismo que la operación anterior
  z: array([1,-1]) # Vector substration
  ```

  ```python
  y = np.array([1,2])
  v = np.array([2,1])
  
  z = y * v
  z = np.multiply(y,v) # Es lo mismo que la operación anterior
  z: array([2,2]) # Vector multiply

  z = y / v
  z = np.divide(y,v) # Es lo mismo que la operación anterior
  z: array([2,2]) # Vector division

  result = np.dot(y,v)
  result: 4 # Doc product 
  ```
  ###### *¿Qué es el producto escalar?*
  Nos indica cuanto apunta un vector en la misma dirección que otro.

  #### Universal functions:

  ```python 

  a = np.array([1,-1,1,-1,5])

  a.mean(): 1 # Media
  a.max(): 5 # Valor máximo

  np.pi # Es el valor de pí, equivale a dicho número
  np.sin # Aplica la función de seno a un valor

  np.linspace(-2,2, num=5): -2 -1 0 1 2 # Nos devuelve la diferencia 
                          #entre dos números pero repartida entre 5 indices.
  ```

