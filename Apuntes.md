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

* **Equivalencia ASCII de letras:**

<table class="tg">
<thead>
  <tr>
    <th class="tg-1cln">Char.</th>
    <th class="tg-xozw">ASCII</th>
    <th class="tg-xozw">Char.</th>
    <th class="tg-xozw">ASCII</th>
    <th class="tg-xozw">Char.</th>
    <th class="tg-xozw">ASCII</th>
    <th class="tg-xozw">Char.</th>
    <th class="tg-xozw">ASCII</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-7geq">A</td>
    <td class="tg-baqh">65</td>
    <td class="tg-7geq">N</td>
    <td class="tg-baqh">78</td>
    <td class="tg-7geq">a</td>
    <td class="tg-baqh">97</td>
    <td class="tg-7geq">n</td>
    <td class="tg-baqh">110</td>
  </tr>
  <tr>
    <td class="tg-7geq">B</td>
    <td class="tg-baqh">66</td>
    <td class="tg-7geq">O</td>
    <td class="tg-baqh">79</td>
    <td class="tg-7geq">b</td>
    <td class="tg-baqh">98</td>
    <td class="tg-7geq">o</td>
    <td class="tg-baqh">111</td>
  </tr>
  <tr>
    <td class="tg-7geq">C</td>
    <td class="tg-baqh">67</td>
    <td class="tg-7geq">P</td>
    <td class="tg-baqh">80</td>
    <td class="tg-7geq">c</td>
    <td class="tg-baqh">99</td>
    <td class="tg-7geq">p</td>
    <td class="tg-baqh">112</td>
  </tr>
  <tr>
    <td class="tg-7geq">D</td>
    <td class="tg-baqh">68</td>
    <td class="tg-7geq">Q</td>
    <td class="tg-baqh">81</td>
    <td class="tg-7geq">d</td>
    <td class="tg-baqh">100</td>
    <td class="tg-7geq">q</td>
    <td class="tg-baqh">113</td>
  </tr>
  <tr>
    <td class="tg-7geq">E</td>
    <td class="tg-baqh">69</td>
    <td class="tg-7geq">R</td>
    <td class="tg-baqh">82</td>
    <td class="tg-7geq">e</td>
    <td class="tg-baqh">101</td>
    <td class="tg-7geq">r</td>
    <td class="tg-baqh">114</td>
  </tr>
  <tr>
    <td class="tg-7geq">F</td>
    <td class="tg-baqh">70</td>
    <td class="tg-7geq">S</td>
    <td class="tg-baqh">83</td>
    <td class="tg-7geq">f</td>
    <td class="tg-baqh">102</td>
    <td class="tg-7geq">s</td>
    <td class="tg-baqh">115</td>
  </tr>
  <tr>
    <td class="tg-7geq">G</td>
    <td class="tg-baqh">71</td>
    <td class="tg-7geq">T</td>
    <td class="tg-baqh">84</td>
    <td class="tg-7geq">g</td>
    <td class="tg-baqh">103</td>
    <td class="tg-7geq">t</td>
    <td class="tg-baqh">116</td>
  </tr>
  <tr>
    <td class="tg-7geq">H</td>
    <td class="tg-baqh">72</td>
    <td class="tg-7geq">U</td>
    <td class="tg-baqh">85</td>
    <td class="tg-7geq">h</td>
    <td class="tg-baqh">104</td>
    <td class="tg-7geq">u</td>
    <td class="tg-baqh">117</td>
  </tr>
  <tr>
    <td class="tg-7geq">I</td>
    <td class="tg-baqh">73</td>
    <td class="tg-7geq">V</td>
    <td class="tg-baqh">86</td>
    <td class="tg-7geq">i</td>
    <td class="tg-baqh">105</td>
    <td class="tg-7geq">v</td>
    <td class="tg-baqh">118</td>
  </tr>
  <tr>
    <td class="tg-7geq">J</td>
    <td class="tg-baqh">74</td>
    <td class="tg-7geq">W</td>
    <td class="tg-baqh">87</td>
    <td class="tg-7geq">j</td>
    <td class="tg-baqh">106</td>
    <td class="tg-7geq">w</td>
    <td class="tg-baqh">119</td>
  </tr>
  <tr>
    <td class="tg-7geq">K</td>
    <td class="tg-baqh">75</td>
    <td class="tg-7geq">X</td>
    <td class="tg-baqh">88</td>
    <td class="tg-7geq">k</td>
    <td class="tg-baqh">107</td>
    <td class="tg-7geq">x</td>
    <td class="tg-baqh">120</td>
  </tr>
  <tr>
    <td class="tg-7geq">L</td>
    <td class="tg-baqh">76</td>
    <td class="tg-7geq">Y</td>
    <td class="tg-baqh">89</td>
    <td class="tg-7geq">l</td>
    <td class="tg-baqh">108</td>
    <td class="tg-7geq">y</td>
    <td class="tg-baqh">121</td>
  </tr>
  <tr>
    <td class="tg-7geq">M</td>
    <td class="tg-baqh">77</td>
    <td class="tg-7geq">Z</td>
    <td class="tg-baqh">90</td>
    <td class="tg-7geq">m</td>
    <td class="tg-baqh">109</td>
    <td class="tg-7geq">z</td>
    <td class="tg-baqh">122</td>
  </tr>
</tbody>
</table>