def graph_has_eulerian_circuit(graph):
    """Comprueba si un grafo no dirigido tiene un circuito euleriano.

    Args:
        graph (grafo): Grafo en formato de listas. 
                       Ej: (['a', 'b', 'c'], [('a', 'b'), ('b', 'c')])

    Returns:
        boolean: graph tiene un circuito euleriano

    Raises:
        TypeError: Cuando el tipo del argumento es inválido
    """
    pass


def find_eulerian_circuit(graph):
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