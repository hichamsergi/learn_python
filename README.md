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

### **Lectura de ficheros:**

La lectura de ficheros es una parte esencial de Python que nos permite abrir, leer e interactuar con documentos utilizando funciones propias de Python. Para poder operar con documentos hay que seguir los siguientes pasos:

  #### 1. Abrir el documento:

  ```python
  with open('file.txt','r') as file:
  ```
  * `with`: Este metodo nos permite abrir el documento y **cerrarlo automaticamente**, una vez el codigo ejecutado bajo el haya sido completado.

  * `open()`: Esta funcion integrada en Python nos permite abrir `file.txt` com un objeto e interactuar con el.

  * `r`: Este parametro indica el modo en el que abrimos `file.txt`, en este caso lectura. Puede haber diferentes propositos para abrir un documento:

    * `r`: Lectura.
    * `w`: Escritura.
    * `a`: Anexión.

  #### 2. Leer el contenido:

  ```python
  with open('file.txt','r') as file:

    contenido_file = file.read()
  ```
  Dado que tenemos abierto el documento, con el metodo `with`, ahora podemos leer el contenido con la función `file.read()`.

  #### 3. Interactuar con el contenido:
  ```python
  with open('file.txt','r') as file:

    contenido_file = file.read()

    print(contenido_file)
  ```
   Al haber leido el contenido del documento, asignamos todo el contenido a una variable que lo almacenará. Ahora, `contenido_file` conteniene todo el texto que hay en `file.txt`, y podemos hacer con el lo que queramos, como mostrarlo.

  #### 3.2 Leer el contenido linea a linea:

  Ahora mismo tenemos todo el contenido del documento `file.txt` almacenado en una variable. Pero ese contenido es enorme y podriamos necesitar leer, solo, el contenido línea a línea. Para poder hacer eso necesitariamos la función `readline()`:
  ```python
  with open('file.txt','r') as file:

    line1 = file.readline # Almacenamos la línea 1.
  ```

  La función `readline()` únicamente lee una línea a la vez. En el caso de querer leer el resto del contenido, tenemos que ser un poco más creativos:
  ```python
  with open('file.txt','r') as file:
    
    while True:
      line = file.readline()

      if not line: #Esta condición nos indica que ya no hay mas líneas

        break #Devolviendo 'False'
      
      print(line)
  ```

  #### 3.3 Leer carácteres específicos:

  Hay diferntes utilidades para hace esto:

  ```python
  file.seek(10) # Lee solo los carácteres de una posición especifica.
                # 10, es la posición en byte de los carácteres a leer.

  file.read(5) #Lees solo 5 carácteres y finaliza la lectura.
  ```

