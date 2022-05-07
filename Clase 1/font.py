from multiprocessing.sharedctypes import Value
from re import A
from turtle import width


font ={
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
    'autor' : "Miguel" }


# for glifo , valores in font['glifos'].items():
#     #print(glifo, valores)
#     print(f'{glifo} LSB = {valores["LSB"]}')

# print(font['glifos']['A']['nodes'][0][1])
# print(font['glifos']['A']['LSB'])

# font['glifos']['C'] = {
#                 'nodes':[(120,189), (120,300),(120,890)],
#                 'LSB' : 148,
#                 'RSB' : 156,
#                 'width': 660
#                 } 
# print(font['glifos'])

# font['glifos'].pop('C')
# print(font['glifos'])

print(font.items())
print(font.keys())
print(font.values())

# for glifo , valores in font['glifos'].items():
#     #print(glifo, valores)
#     valores['LSB']= 120
#     print(f'{glifo} LSB = {valores["LSB"]}')