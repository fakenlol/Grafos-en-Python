from math import perm
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
        pos = random.choice(graph[0])
        permCircuit = []
        tempGraph = graph
        while aristas != []:
            for arista in aristas:
                grados = cuenta_grado(graph)
                if arista[0] == pos:
                    tempGraph[1].remove(arista)
                    if es_conexo(tempGraph):
                        permCircuit.append(pos)
                        pos = arista[1]
                    else:
                        if grados[pos] == 1:
                            permCircuit.append(pos)
                            graph[0].remove(pos)
                            grados = cuenta_grado(graph)
                            pos = arista[1]
                        else:
                            tempGraph[1].append(arista)
                elif arista[1] == pos:
                    tempGraph[1].remove(arista)
                    if es_conexo(tempGraph):
                        permCircuit.append(pos)
                        pos = arista[0]
                    else:
                        if grados[pos] == 1:
                            permCircuit.append(pos)
                            graph[0].remove(pos)
                            grados = cuenta_grado(graph)
                            pos = arista[0]
                        else:
                            tempGraph[1].append(arista)
        permCircuit.append(permCircuit[0])
        print(permCircuit)

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