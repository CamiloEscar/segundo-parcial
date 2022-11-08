class Pila (object):

    def __init__(self):
        self.__elementos = []

    def apilar (self, dato):
        self.__elementos.append(dato)

    def desapilar (self):
        return self.__elementos.pop()

    def pila_vacia(self):
        return len (self.__elementos) == 0  #si la pila esta vacia devuelve true, y sino false

    def tamanio (self):
        return len (self.__elementos)  

    def elemento_cima (self): #obtiene el valor que esta en la cima sin eliminarlo
        return self.__elementos [-1]