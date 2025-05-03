## Apuntes de python para certificacion de COURSERA:

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
* **String Slicing:** Obtención de multiples carácteres de un mismo string accediendo al rango que ocupan dichos carácteres. 
Ejemplos:

    ```
    name = "The Bodyguard"

    name[0:4] = "The "

    name[8:12] = "guar"
    ```
    En el *slicing* se excluye el último carácter del rango indicado.


* **String Stride:** Obtención de multiples carácteres de un mismo string indicando la periodicidad con la que se extraen dichos caracters. 
Ejemplos:

    ```
    name = "The Bodyguard"

    name[::2] = "TeBdgad"   #Obtenemos 1 carácter cada 2 carácteres

    name[::3] = "T dud"     #Obtenemos 1 carácter cada 3 carácteres
    ```
    En el *stride* se incluye por defecto el primer carácter del string total.

* **Secuencias de escape:** Combinación de ``\`` y un carácter, que genera algo especial. 
Ejemplos:
    
    - ``\n``: Salto de línea.
    - ``\t``: Tabulación.