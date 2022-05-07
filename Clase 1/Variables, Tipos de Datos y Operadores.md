
## Variables y Tipos de Datos
Los datos se pueden almacenar en variables, una variable siempre se declara con un operador `=` por ejemplo: `variable = 'esta es una string'`.

Exiten varios tipos de datos 

| Tipo | Descripción | Ejemplo |
| :---:        |     :---:      |          :---: |
| int  | Número sin decimales     | 7  |
| float  | Número con decimales     | 7.6   |
| str  | Cadena de caracteres     | 'hola', "mundo"   |
| bool  | Booleano     | True, False   |

Para verificar el tipo de dato de una variable podemos usar la función `type()`:
``` python
numero = 7.5 
print(type(numero)) #El resultaro será <class 'float'>

numeroDos = 7
print(type(numeroDos)) #El resultaro será <class 'int'>

verdadero = True
print(type(numeroDos)) #El resultaro será <class 'bool'>

cadena = 'True'
print(type(cadena)) #El resultaro será <class 'str'>
```
## Operadores Aritméticos
También puedes almacenar operaciones en variables `suma = 3 + 3`, existen varios operadores aritméticos: 

|OPERADOR|	DESCRIPCIÓN	|USO|
| :---:         |     :---:      |          :---: |
|+	| Suma entre valores	| 23 + 4 = 27|
|-	| Resta entre valores	| 87 - 20 = 67|
|*	| Multiplicación entre valores	| 15 * 4 = 60|
|/	| División entre valores	| 21 / 3 = 7|
|//	| División con resultado de número entero	| 18 // 5 = 3|
|%	| Módulo entre valores	| 16 % 3 = 1|
|**	| Potencia de valores	| 2 ** 3 = 8|

## Operadores Relacionales
Se usan para comparar y establecer la relación entre valores.  un valor booleano (true o false).
|OPERADOR|	DESCRIPCIÓN|	USO|
| :---:         |     :---:      |          :---: |
|>|	 Verifica si el valor de la izquierda es mayor que el valor de la derecha	|5 > 1  True|
|<|	 Verifica si el valor la izquierda es mayor que el valor de la derecha	|11 < 4  False|
|==|	 Verifica si ambos valores son iguales	|45 == 44  False|
|>=|	 Verifica si el valor de la izquierda es mayor o igual que el valor de la derecha	|4 >= 2  True|
|<=|	 Verifica si el valor de la derecha es mayor o igual que el valor de la izquierda	|24 <= 4  False|
|!=|	 Verifica si ambos valores no son iguales	|10 != 0  True|

``` python
numeroUno = 7.5 
numeroDos = 74

print(numeroUno < numeroDos) #True
print(numeroUno == numeroDos) #False
print(numeroUno != numeroDos) #True
```

## Operadores Lógicos
Se utiliza un operador lógico para tomar una decisión basada en múltiples condiciones.
Por ejemplo: declaramos 4 variables, `a = 2 `, `b = 5` ,  `x= 6` y `z = 7`

|OPERADOR|	DESCRIPCIÓN|	USO| RESULTADO|
| :---:         |     :---:      |          :---: |          :---: |
|and|	Devuelve True si ambas condiciones son True|	a < b **and** z > x | True|
|or|	Devuelve True si alguna de las condiciones es True	| a > b **or** x == z | False|
|not|	Invierte True por False y False por True |	**not** a | False |


## Operadores de Pertenencia
`in` y `not in `se usan para identificar pertenencia en algun objeto (listas, strings, tuplas).

```python
lista = [1,2,3,4,5]

print(3 in lista) #  True 
print(6 not in lista) # True
  
cadena = "Hola Mundo"
print("Mundo" in cadena) # True
print("mundo" in cadena) # False  
print("mundo" not in cadena) # True
```

