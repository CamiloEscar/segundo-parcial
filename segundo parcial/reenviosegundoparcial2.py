from arbol import (
    nodoArbol,
    arbol_vacio,
    insertar_nodo,
    inorden_empieza_con,
    eliminar_nodo,
    inorden,
    postorden,
    busqueda,
    por_nivel,
    inorden_estatura,
    inorden_kilogramos
)
from grafo import Grafo


arbol = nodoArbol()

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
g.insertar_arista('X', 'M', 1)
g.insertar_arista('R', 'S', 2)
g.insertar_arista('K', 'Y', 4)
g.insertar_arista('O', 'P', 9)

#D
g.barrido_lista2()

#B hallar el árbol de expansión mínimo desde el vértice que contiene a C-3PO, Yoda y la princesa Leia;
# se hace el recorrido kruskal y se pregunta si los tres estan en el mismo arbol, 
# si estan en el mismo se hace el recorrido

arbol_min = g.kruskal()

if 'T' in arbol_vacio[0] and 'M'in arbol[0] and 'Y'in arbol[0]:
    print('Están en el mismo arbol',arbol)
    arbol_min = arbol_min[0].split('-')
    peso_total = 0
    for nodo in arbol_min:
        nodo = nodo.split(';')
        peso_total += int(nodo[2])
        print(f'{nodo[0]}-{nodo[1]}-{nodo[2]}')
else:
    print('No estan en el mismo arbol')

# if g.existe_paso('T', 'M', 'Y'):
#     resultados1 = g.dijkstra('T')
#     camino = g.camino(resultados1, 'T', 'M', 'Y')
#     print(camino)
# else:
#     print('no se puede llega de T a M')


#C determinar cuales personajes comparten con otro dos episodios o mas

#barrido de lista de listas, en el barrido de aristas se filtra que el peso sea mayor a 2
g.barrido_lista()

#g.obtener_elemento_vertice()


#E recorrido por todas las aristas y se suman la cantidad de contactos, 
# cuando llega al max se va guardando y se modifica cuando pasa por todos
# busquedar vertice con mayor cantidad de aristas o buscar arista con mayor peso

print('el personaje:',g.mayor_cantidad_aristas ()[0],',compartió con:',g.mayor_cantidad_aristas ()[1],'personajes')


# g.adyacentes()
