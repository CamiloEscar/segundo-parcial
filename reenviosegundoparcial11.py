# 1 - Desarrollar un algoritmo que permita implementar un árbol como índice para hacer consultas de personajes 
# de la saga de Star Wars, de los cuales se sabe su nombre, altura y peso. 
# Además deberá contemplar los siguientes requerimientos (debe cargar al menos 20 personajes):
from cola import Cola

from arbol import (
    nodoArbol,
    insertar_nodo,
    inorden_empieza_con,
    eliminar_nodo,
    inorden,
    preorden,
    postorden,
    busqueda,
    por_nivel,
    inorden_altura,
    inorden_peso
)

arbol = nodoArbol()


lista = [
    ['Yoda',0.60, 50 ],
    ['Mandalorian',2.00, 150 ],
    ['Luke Skywalker',1.75, 100 ],
    ['Darth Vader',1.90, 120 ],
    ['Chewbacca',1.95, 150 ],
    ['R2-D2',0.4, 30 ],
    ['Anakin Skywalker',1.70, 80 ],
    ['Obi-Wan Kenobi',1.70, 90 ],
    ['Luke Skywalker',1.80, 85 ],
    ['C3PO',0.60, 40 ],
    ['Han Solo',1.70, 83 ],
    ['Leia',1.60, 60 ],
    ['BB8',1.50, 70 ],
    ['Kylo Ren',1.80, 80 ],
    ['Rey',1.90, 90 ],
    ['Qui-Gon Jinn',1.40, 60 ],
    ['Padme Amidala',1.60, 60 ],
    ['Darth Maul',1.90, 90 ],
    ['Boba Fett',1.30, 50 ],
    ['Grogu',1.80, 80 ],
]

for nombre, altura, peso in lista:
    datos = {'altura': altura,
             'peso': peso}
    
    insertar_nodo(arbol, nombre, datos)
#print(arbol)

# a. se debe poder cargar un nuevo personaje, modificarlo (cualquiera de sus campos) y darlo de baja;
#preorden(arbol)

print('cargar datos del personaje')
nombre_per=input('Ingrese el Nombre:')
altura_per=input('Ingrese la altura:')
peso_per=input('Ingrese el peso:')
datos=(altura_per,peso_per)

insertar_nodo(arbol, nombre_per, datos)

print()

print('modificar personaje')
clave = input('ingrese el nombre:')
dato = arbol['datos']
pos = eliminar_nodo(arbol, clave)
if pos:
    nombre_mod = input('ingrese nuevo nombre: ')
    insertar_nodo(arbol, nombre_mod, dato)
else:
    print('valor no encontrado en el arbol')
print()

print('dar de baja persojanje')
personaje_baja = input('ingrese el nombre: ')
print()
eliminar_nodo(arbol, personaje_baja)

inorden(arbol)
print()

# b. mostrar toda la información de Yoda, Mandalorian y Luke Skywalker

postorden(arbol)

pos = (busqueda(arbol, 'Yoda'))
# if pos:
#     print(pos['nombre'])
#     print(pos['altura'])
#     print(pos['peso'])

pos = (busqueda(arbol, 'Mandalorian'))
# if pos:
#     print(pos['nombre'])
#     print(pos['altura'])
#     print(pos['peso'])

pos = (busqueda(arbol, 'Luke Skywalker'))
# if pos:
#     print(pos['nombre'])
#     print(pos['altura'])
#     print(pos['peso'])

# c. mostrar un listado ordenado alfabéticamente de los personajes que miden menos de 0.9 metro;

print('mostrar un listado ordenado alfabéticamente de los personajes que miden menos de 0.9 metro;')
print()
inorden_altura(arbol)

# if pos:
#     pos['nombre']['altura'] < 0.90
#     print(pos['info'])
#     print(pos['nombre'])

# d. mostrar un listado ordenado alfabéticamente de los personajes que pesan mas de 75 kilos;

print('mostrar un listado ordenado alfabéticamente de los personajes que pesan mas de 75 kilos;')
print()
inorden_peso(arbol)

# if pos:
#     pos['nombre']['peso'] > 75
#     print(pos['info'])
#     print(pos['nombre'])

# e. mostrar un listado por nivel de los personajes del árbol;

print('mostrar un listado por nivel de los personajes del árbol')
print()
por_nivel(arbol)
print()

# f. determinar si Grogu esta en el árbol y responder lo siguiente:

# mostrar toda su información;
# en que tipo de nodo esta (hoja, intermedio o raíz);
# que altura tiene el nodo dentro del árbol.


print('determinar si Grogu esta en el árbol')
print()
pos = busqueda(arbol, 'Grogu')

print('mostrar toda su información'
        'en que tipo de nodo esta (hoja, intermedio o raíz)'
        'en que tipo de nodo esta (hoja, intermedio o raíz)'
        'que altura tiene el nodo dentro del árbol')

# if pos:
#     print(pos['nombre'])
#     print(pos['altura'])
#     print(pos['peso'])

personaje_buscado='Grogu'

if (busqueda(arbol, personaje_buscado)):
    print('Grogu está')
    buscado=(busqueda(arbol, personaje_buscado))
    print(buscado)
    if arbol['info']==personaje_buscado:
        print('Es Raíz')
    elif buscado['der'] is None and buscado['izq'] is None:
        print('Es hoja')
    else:
        print ('Esta en una posición intermedio')
else:
    print('Grogu no está')

altura_arbol=(altura(arbol))
altura_buscado=(buscado['altura'])
print('el nodo tiene la altura:',altura_arbol-altura_buscado)


