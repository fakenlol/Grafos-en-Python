from practica1 import *
import random

def graph_has_eulerian_circuit(graph):
    if es_conexo(graph):
        vertices_grados = cuenta_grado(graph)
        for grado in vertices_grados.values():
            if grado % 2 != 0:
                print("No posee grado par en todos sus vertices => ∄ circuito euleriano")
                return False
    else:
        print("El grafo no es conexo, por lo tanto no posee circuito euleriano")
        return False
    return True


def find_eulerian_circuit(graph):

    if graph_has_eulerian_circuit(graph):

        aristas = graph[1]
        aristasToDelete = []
        pos = random.choice(graph[0])
        permCircuit = []
        tempGraph = graph
        grades = cuenta_grado(graph)

        while aristas != []:
            for arista in aristas:
                
                if arista[0] == pos or arista[1] == pos:
                    tempGraph[1].remove(arista)
                    if es_conexo(tempGraph):
                        aristasToDelete.append(arista)
                    else:
                        tempGraph[1].append(arista)
            for arista in aristasToDelete:
                aristas.remove(arista)
            aristasToDelete = []
        

    else:
        print("No posee circuito euleriano")

    """Obtiene un circuito euleriano en un grafo no dirigido, si es posible

    Args:
        graph (grafo): Grafo en formato de listas. 
                       Ej: (['a', 'b', 'c'], [('a', 'b'), ('b', 'c')])

    Returns:
        path (lista de aristas): ciclo euleriano, si existe
        None: si no existe un camino euleriano

    Raises:
        TypeError: Cuando el tipo del argumento es inválido
    """

    # Sugerencia: Usar el Algoritmo de Fleury
    # Recursos:
    # http://caminoseuler.blogspot.com.ar/p/algoritmo-leury.html
    # http://www.geeksforgeeks.org/fleurys-algorithm-for-printing-eulerian-path/    
    pass