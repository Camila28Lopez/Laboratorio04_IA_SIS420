import time
import random

class Nodo:
    def __init__(self, datos, hijo=None):
        self.datos = datos
        self.hijos = []
        self.padre = None
        self.costo = None
        self.set_hijo(hijo)

    def set_hijo(self, hijo):
        if (hijo is not None):
            self.hijos.append(hijo)
            if self.hijos is not None:
                for h in self.hijos:
                    h.padre = self

    def get_hijos(self):
        return self.hijos

    def set_padre(self, padre):
        self.padre = padre

    def get_padre(self):
        return self.padre

    def set_datos(self, datos):
        self.datos = datos

    def get_datos(self):
        return self.datos

    def set_costo(self, costo):
        self.costo = costo

    def get_costo(self):
        return self.costo

    def equal(self, nodo):
        if self.get_datos() == nodo.get_datos():
            return True
        else:
            return False

    def en_lista(self, lista_nodos):
        enlistado = False
        for n in lista_nodos:
            if self.equal(n):
                enlistado = True
        return enlistado

    def __str__(self):
        return str(self.get_datos())


def Comparar(nodo):
    return nodo.get_costo()
def bpa(estado_inicio, estado_solucion):
    resuelto = False
    nodos_visitados = []
    nodos_frontera = []
    nodo_inicio = Nodo(estado_inicio)
    #tendremos el nodo inicio con un costo de 0 y se ira variando empezando en el
    nodo_inicio.set_costo(0)
    
    nodos_frontera.append(nodo_inicio)


    while resuelto == False and len(nodos_frontera) != 0:
        nodos_frontera = sorted(nodos_frontera, key=Comparar, reverse= True)
        #Despues de alamacenar los nodos en la lista frontera , se ordenara de mayor a menor con el reverse 
        #print(Comparar)
        nodo_actual = nodos_frontera[0]
        nodos_visitados.append(nodos_frontera.pop(0))
        if nodo_actual.get_datos() == estado_solucion:
            resuelto = True
            return nodo_actual
        else:
            

            for i in range(len(estado_inicial)-1):
                hijo_datos = nodo_actual.get_datos().copy()
                temp = hijo_datos[i]

                hijo_datos[i] = hijo_datos[i + 1]
                hijo_datos[i + 1] = temp
                hijo = Nodo(hijo_datos)
                #a la hora de hacer el movimiento y crear un nuevo hijo le incrementamos uns costo
                #dicho costo sera aleatoriodesde cero hasta la cantidad de fichas que tengamos
                costo = random.randrange(1,len(estado_inicial)) 
                # para que no se nos agrege doble costo a un hijo hacemos este if 
                # es decir que si um hijo tieme el costo 3 y vuelve a salir el mismo hijo se leera con el costo 3
                if hijo.get_costo() == None:  
                    hijo.set_costo(costo)
                #print(costo)
                if not hijo.en_lista(nodos_visitados) and not hijo.en_lista(nodos_frontera):
                    nodo_actual.set_hijo(hijo)
                    nodos_frontera.append(hijo)
            


if __name__ == "__main__":

    estado_inicial = [7,6,5,4,3,2, 1]
    solucion = [1, 2, 3,4,5,6,7]
    #cuando las fichas son mayores a 7 la busqueda es mas lenta aun con el costo tarda hasta 132 segundos .
    start = time.time()
    nodo_solucion = bpa(estado_inicial, solucion)
    end = time.time()


    resultado = []
    nodo_actual = nodo_solucion
    while nodo_actual.get_padre() is not None:
        resultado.append(nodo_actual.get_datos())
        nodo_actual = nodo_actual.get_padre()

    resultado.append(estado_inicial)
    resultado.reverse()

    for M in range(len(resultado)):
        print(resultado[M])
print("Tiempo : ", end - start, "seg")
print("............................")
#print("Costo: %s" % str(nodo_solucion.get_costo()))
"""comparando con el codigo que no tiene costos podemos llegar a la conclusion 
de que este es mas rapido en cunato al tiempo
"""