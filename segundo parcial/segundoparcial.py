# 1 - Desarrollar un algoritmo que permita implementar un árbol como índice para hacer consultas de personajes 
# de la saga de Star Wars, de los cuales se sabe su nombre, altura y peso. 
# Además deberá contemplar los siguientes requerimientos (debe cargar al menos 20 personajes):
from grafo import Grafo
from cola import Cola

from arbol import (
    nodoArbol,
    insertar_nodo,
    inorden_empieza_con,
    eliminar_nodo,
    inorden,
    postorden,
    busqueda,
    por_nivel
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
                {'nombre': 'Darth Sidious', 'altura': 1.80, 'peso' : 80 },]

for nombre, altura, peso in lista:
    datos = {'nombre': nombre,
             'altura': altura,
             'peso': peso}
    
    insertar_nodo(arbol, nombre, datos)

# a. se debe poder cargar un nuevo personaje, modificarlo (cualquiera de sus campos) y darlo de baja;

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

if pos:
    print(pos['info'])
    print(pos['datos'])
    print(pos['datos'])

pos = busqueda(arbol, 'Mandalorian')

if pos:
    print(pos['info'])
    print(pos['datos'])
    print(pos['datos'])

pos = busqueda(arbol, 'Luke Skywalker')

if pos:
    print(pos['info'])
    print(pos['datos'])
    print(pos['datos'])

# c. mostrar un listado ordenado alfabéticamente de los personajes que miden menos de 0.9 metro;

if pos:
    pos['datos']['altura'] < 0.90
    print(pos['info'])
    print(pos['datos'])

# d. mostrar un listado ordenado alfabéticamente de los personajes que pesan mas de 75 kilos;

if pos:
    pos['datos']['peso'] > 75
    print(pos['info'])
    print(pos['datos'])

# e. mostrar un listado por nivel de los personajes del árbol;

por_nivel(arbol)
print()

# f. determinar si Grogu esta en el árbol y responder lo siguiente:

# mostrar toda su información;
# en que tipo de nodo esta (hoja, intermedio o raíz);
# que altura tiene el nodo dentro del árbol.

pos = busqueda(arbol, 'Grogu')

if pos:
    print(pos['info'])
    print(pos['datos'])


# 2 - Dado un grafo no dirigido con personajes de la saga Star Wars, 
# implementar los algoritmos necesarios para resolver las siguientes tareas:
# a. cada vértice debe almacenar el nombre de un personaje, las aristas representan la cantidad de episodios 
# en los que aparecieron juntos ambos personajes que se relacionan;

# b. hallar el árbol de expansión mínimo desde el vértice que contiene a C-3PO, Yoda y la princesa Leia;

# c. determinar cuales personajes comparten con otro dos episodios o mas (mostrar el par de pesonajes);

# d. cargue al menos los siguientes personajes: Luke Skywalker, Darth Vader, Yoda, Boba Fett, 
# C-3PO, Leia, Rey, Kylo Ren, Chewbacca, Han Solo, R2-D2, Obi-Wan kenobi; BB-8;

# e.determinar que personaje es el que a compartido episodio con la mayor cantidad del resto de los personajes.

#2
g = Grafo(dirigido=False)

#D
g.insertar_vertice('T', datos={'nombre': 'Yoda'})
g.insertar_vertice('Z', datos={'nombre': 'Luke Skywalker'})
g.insertar_vertice('F', datos={'nombre': 'Han Solo'})
g.insertar_vertice('X', datos={'nombre': 'Mandalorian'})
g.insertar_vertice('R', datos={'nombre': 'Chewbacca'})
g.insertar_vertice('K', datos={'nombre': 'R2-D2'})
g.insertar_vertice('O', datos={'nombre': 'Obi-Wan kenobi'})
g.insertar_vertice('L', datos={'nombre': 'Darth Vader'})
g.insertar_vertice('J', datos={'nombre': 'Rey'})
g.insertar_vertice('I', datos={'nombre': 'Kylo Ren'})
g.insertar_vertice('M', datos={'nombre': 'C-3PO'})
g.insertar_vertice('S', datos={'nombre': 'Boba Fett'})
g.insertar_vertice('Y', datos={'nombre': 'Leia'})
g.insertar_vertice('P', datos={'nombre': 'Darth Sidious'})

#A
g.insertar_arista('L', 'J', 6)
g.insertar_arista('Z', 'T', 8)
g.insertar_arista('F', 'I', 3)
g.insertar_arista('X', 'M', 8)
g.insertar_arista('R', 'S', 2)
g.insertar_arista('K', 'Y', 2)
g.insertar_arista('O', 'P', 9)


#B
if g.existe_paso('T', 'M'):
    resultados1 = g.dijkstra('T')
    camino = g.camino(resultados1, 'T', 'M')
    print(camino)
else:
    print('no se puede llega de T a M')

if g.existe_paso('T', 'Y'):
    resultados1 = g.dijkstra('T')
    camino = g.camino(resultados1, 'T', 'Y')
    print(camino)
else:
    print('no se puede llega de T a Y')

#C
 
g.obtener_elemento_vertice()

#E 
g.adyacentes()
