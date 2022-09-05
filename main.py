from practica1 import *
from practica2 import *

grafo1 = (["A","B","C","D","E","F"],[("A","B"),("B","C"),("D","E")])
grafo2 = (["A","B","C","D","E"],[("A","B"),("B","D"),("D","C"),("A","E")])
grafo3 = (["A","B","C","D","E"],[("A","B"),("C","D")])

#GRAFOS COMPLETOS DE PRUEBA
grafoK3 = (["A","B","C"],[("A","B"),("B","C"),("C","A")])
grafoK4 = (["A","B","C","D"],[("A","B"),("A","C"),("A","D"),("B","D"),("B","C"),("C","D")])
grafoK5 = (["A","B","C","D","E"],[("A","B"),("A","C"),("A","D"),("A","E"),("B","C"),("B","D"),("B","E"),("C","D"),("C","E"),("D","E")])

def main(grafo):
    #grafo = lee_grafo_stdin()

    print("Grafo en forma de lista: " + str(grafo))

    print("\nGrados de cada vertice del grafo: " + str(cuenta_grado(grafo)))

    lista_a_adyacencia(grafo)

    print("\nComponentes conexas del grafo: " + str(componentes_conexas(grafo)))

    if es_conexo(grafo):
        print ("Es un grafo conexo")
    else:
        print ("No es un grafo conexo")
    pass
    find_eulerian_circuit(grafo)

if __name__ == '__main__':
    main(grafoK5)