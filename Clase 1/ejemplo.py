# Esta seccion es de ejemplo no la peles 
# print("Hola Mundo")
# print('Hola "Mundo"')
# print('Hola ''Mundo')

# PI = 3.1416
# cadenaUno = "Hola Python"

# print(type(numeroUno))
# print(type(PI))

# potencia = numeroUno ** numeroDos
# suma = numeroUno + numeroDos
# operacion = (numeroUno + numeroDos) * numeroDos

# print(potencia)
# print(suma)

# if numeroUno != numeroDos:
#     print(numeroUno,'es diferente', numeroDos)

# elif numeroUno > numeroDos:
#     print(numeroUno,'es mayor que', numeroDos)

# elif numeroUno < numeroDos:
#     print(numeroUno,'es menor que',numeroDos)

# else:
#     print('No se que pasa XD')

# numeroUno = 6
# numeroDos = 5 

# if numeroUno < numeroDos and numeroUno <= 3 :
#     print('Se cumple la primera condicion')

# elif numeroUno > numeroDos or numeroUno <= 6 :
#     print('Se cumple la segunda condicion')


# variableUno = 14

# print(listaUno[-1])
# print(f'La longitud de la listaUno es de {len(listaUno)}')

# listaUno = ["A","B","C","D","E","X","Y","Z", 12, 3.5, True, [1,2,3,4]]
# print(listaUno)

# listaUno.pop(-2)
# print(listaUno)

# tuplaUno = (120, 1500)


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

    }

print(font['glifos']['B']['nodes'][-1])
font['glifos']['C'] = {
                'nodes':[(120,189), (120,300),(120,890)],
                'LSB' : 148,
                'RSB' : 156,
                'width': 660
                } 
print(font['glifos'])















