## Listas

Las listas permiten almacenar valores en una sola variable. Los valores siempre se escriben entre corchetes `[...]` y perarados por comas `,`:
 ``` python 
listaEjemplo= [ 1, "string",  ['x', variables, 4, 7.5], True]

glifos = ["A","B","C","D","E","X","Y","Z"]
 ```

### Acceder a elementos de lista por índice

Para acceder a cualquier elemento de una lista debes poner el *index/índice* entre ``[]`` después del nombre de la variable de lista. Los índices comienzan desde 0, por lo que en el siguiente código ``glifos[0]``, es el primer elemento de la lista ``glifos``:

``` python

print('El primer Glifo es', glifos[0]) # A
print('El segundo Glifo es', glifos[1]) # B
print('El último Glifo es', glifos[-1]) # Z
print('El penúltimo Glifo es', glifos[-2]) # Y
```

### Determinar la longitud de una lista
Para obtener la longitud de una lista, utiliza la función `len()`:

``` python

cantidadGlifos = len(glifos)
print('En la fuente hay', number_of_planets, 'glifos')
# 'En la fuente hay 8 glifos'
```
### Agregar y quitar valores a listas
Las listas son manipulables, puedes agregar y eliminar elementos después de crearlos. Para agregar un elemento a una lista, utiliza el método ``.append(valor)``:


``` python

glifos = ["A","B","C","D","E","X","Y","Z"]
print(glifos) # A,B ,C ,D ,E ,X ,Y ,Z

glifos.append('One')
print(glifos)# A, B, C, D, E, X, Y, Z, One
```

Puedes eliminar el último elemento de una lista con el método ``.pop()`` de la variable de lista o un elemento especifoco pasando el *index* del valor ``.pop(index)``

``` python

glifos = ["A","B","C","D","E","X","Y","Z", "One"]
glifos.pop()  # Se elimina 'One'
print(glifos) # A, B, C, D, E, X, Y, Z
glifos.pop(2)  # Se elimina 'C'
print(glifos) # A, B, D, E, X, Y, Z
```

 ## Tuplas

Las Tuplas permiten almacenar valores que no serán manipulados. Los valores siempre se escriben entre paréntesis `(...)` y perarados por comas `,`:
 ``` python 
tuplaEjemplo= ( 1, "string",  ['x', variables, 4, 7.5], True)

coordenadas =(120,139, 145)
 ```

### Acceder a elementos de tupla por índice

Para acceder a cualquier elemento de una tupla debes poner el *index/índice* entre ``[]`` después del nombre de la variable de tupla. Los índices comienzan desde 0, por lo que en el siguiente código ``coordenadas[0]``, es el primer elemento de la tupla ``coordenadas``:

``` python
coordenadas =(120,139, 145, 167)
print(coordenadas[0]) # 120
print(coordenadas[1]) # 139
print(coordenadas[-1]) # 167
print(coordenadas[-2]) # 145
```

Para obtener la longitud de una tupla, utiliza la función `len()` similar a la forma de medir la longitud de las listas:

## Diccionario

Los diccionarios se declaran con llaves ``{ }`` y dos puntos ``:`` para indicar un diccionario. Cada **llave** y **valor** está separado por dos puntos y el nombre de cada llave se incluye entre comillas como  en una string. Los dicionarios también se pueden almacenar en variables, los diccionarios pueden contener cualquier tipo de valor:

``` python
font = {
    'name': 'Cemita',
    'masters': 2,
    'glifos' : { 
            'A' : {
                'nodes':[(120,189), (120,300),(120,890)],
                'LSB' : 100,
                'RSB' : 100,
                'width': 560
                },
            'B' : {
                'nodes':[(120,189), (120,300),(120,890)],
                'LSB' : 148,
                'RSB' : 156,
                'width': 660
                } 
    },
    'metrics': [123, 564, 900],
    'autor' : "Miguel"
    }
```

### Lectura de los valores de un diccionario
Los objetos de diccionario tienen un método llamado get que se usa para acceder a un valor mediante su llave, también puedes pasar la llave entre corchetes `[...]`
``` python
print(font.get('name')) # Cemita
print(font['name']) # Cemita
print(font['glifos']['A']['nodes'][0]) #(120,189)
print(font['glifos']['A']['LSB']) #100
```

### Modificación de valores de un diccionario
Puedes modificar valores dentro de un objeto de diccionario, con el método `update`, actualiza los valores existentes con los nuevos que proporciones. Al igual que se usa el acceso directo de corchetes `[ ]` para leer valores, se puede utilizar para actualizar valores. La principal ventaja de usar `update` es la capacidad de modificar varios valores en una operación.
```python
font.update({
    'name': 'Cemita Poblana',
    'metrics': [34, 344, 940],
    'autor' : "Miguel Angel"
})
print(font['name'])#Cemita Poblana
print(font['autor'])#Miguel Angel
#-----------Corchetes------------
font['name'] = 'Chile Poblano'
font['autor'] = 'Karla'
print(font['name'])#Chile Poblano
print(font['autor'])# Karla
```

### Adición y eliminación de llaves
Para crear una nueva llave, asígnala como si fuera una existente.
```python
font['version'] = 1.4
#------------------------------------------
font['glifos']['C'] = {
                'nodes':[(120,189), (120,300),(120,890)],
                'LSB' : 148,
                'RSB' : 156,
                'width': 660
                } 
print(font['glifos'])
#'A': {'nodes': [(120, 189), (120, 300), (120, 890)], 'LSB': 100, 'RSB': 100, 'width': 560},
#'B': {'nodes': [(120, 189), (120, 300), (120, 890)], 'LSB': 148, 'RSB': 156, 'width': 660}, 
#'C': {'nodes': [(120, 189), (120, 300), (120, 890)], 'LSB': 148, 'RSB': 156, 'width': 660}}
```
Para quitar una llave, similar a las listas, usa el metodo `pop` para eliminarla:
```python
font['glifos'].pop('C')
print(font['glifos'])
#'A': {'nodes': [(120, 189), (120, 300), (120, 890)], 'LSB': 100, 'RSB': 100, 'width': 560},
#'B': {'nodes': [(120, 189), (120, 300), (120, 890)], 'LSB': 148, 'RSB': 156, 'width': 660},
```

