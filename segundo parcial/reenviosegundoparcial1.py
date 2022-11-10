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


lista = [{'nombre': 'Yoda', 'altura': 0.60, 'peso' : 50 },
                {'nombre': 'Mandalorian', 'altura': 2.00, 'peso' : 150 },
                {'nombre': 'Luke Skywalker', 'altura': 1.75, 'peso' : 100 },
                {'nombre': 'Darth Vader', 'altura': 1.90, 'peso' : 120 },
                {'nombre': 'Chewbacca', 'altura': 1.95, 'peso' : 150 },
                {'nombre': 'R2-D2', 'altura': 0.4, 'peso' : 30 },
                {'nombre': 'Anakin Skywalker', 'altura': 1.70, 'peso' : 80 },
                {'nombre': 'Obi-Wan Kenobi', 'altura': 1.70, 'peso' : 90 },
                {'nombre': 'Luke Skywalker', 'altura': 1.80, 'peso' : 85 },
                {'nombre': 'C3PO', 'altura': 0.60, 'peso' : 40 },
                {'nombre': 'Han Solo', 'altura': 1.70, 'peso' : 83 },
                {'nombre': 'Leia', 'altura': 1.60, 'peso' : 60 },
                {'nombre': 'BB8', 'altura': 1.50, 'peso' : 70 },
                {'nombre': 'Kylo Ren', 'altura': 1.80, 'peso' : 80 },
                {'nombre': 'Rey', 'altura': 1.90, 'peso' : 90 },
                {'nombre': 'Qui-Gon Jinn', 'altura': 1.40, 'peso' : 60 },
                {'nombre': 'Padme Amidala', 'altura': 1.60, 'peso' : 60 },
                {'nombre': 'Darth Maul', 'altura': 1.90, 'peso' : 90 },
                {'nombre': 'Boba Fett', 'altura': 1.30, 'peso' : 50 },
                {'nombre': 'Grogu', 'altura': 1.80, 'peso' : 80 },]

for nombre, altura, peso in lista:
    datos = {'altura': altura,
             'peso': peso}
    
    insertar_nodo(arbol, nombre, datos)

# a. se debe poder cargar un nuevo personaje, modificarlo (cualquiera de sus campos) y darlo de baja;
preorden(arbol)
clave = input('ingrese parte de lo que desea buscar ')
inorden_empieza_con(arbol, clave)
print()
clave = input('ingrese nombre que desea modificar ')
pos = eliminar_nodo(arbol, clave)
if pos:
    name = input('ingrese nuevo nombre ')
    insertar_nodo(arbol, name, False)
else:
    print('valor no encontrado en el arbol')

inorden(arbol)
print()

# b. mostrar toda la información de Yoda, Mandalorian y Luke Skywalker

postorden(arbol)

pos = busqueda(arbol, 'Yoda')
# if pos:
#     print(pos['nombre'])
#     print(pos['altura'])
#     print(pos['peso'])

pos = busqueda(arbol, 'Mandalorian')
# if pos:
#     print(pos['nombre'])
#     print(pos['altura'])
#     print(pos['peso'])

pos = busqueda(arbol, 'Luke Skywalker')
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

if pos:
    print(pos['nombre'])
    print(pos['altura'])
    print(pos['peso'])

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


