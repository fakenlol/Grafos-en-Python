from practica1 import *

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
        aristasToSave = aristas
        pos = graph[0][0]
        cantAristas = len(aristas)

        def find_circuit(aristas,aristasToSave,pos):
            
            if len(aristasToSave) == cantAristas:
                print(aristasToSave)
                return True
            else:
                #aristas.append((arista[1],arista[0]))
                if aristas[][] == pos :
                    aristasToSave.append(arista + find_circuit(aristas,aristasToSave,arista[1]))

        find_circuit(aristas,aristasToSave,pos)
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