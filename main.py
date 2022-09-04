from practica1 import *
from practica2 import *

grafo1 = (["A","B","C","D"],[("A","B"),("B","D"),("D","C")])
grafo2 = (["A","B","C","D","E"],[("A","B"),("B","D"),("D","C"),("A","E")])
grafo3 = (["A","B","C","D","E"],[("A","B"),("C","D")])


def main():
    grafo = lee_grafo_stdin()
    print("Grafo en forma de lista: " + str(grafo))

    print("\nGrados de cada vertice del grafo: " + str(cuenta_grado(grafo)))

    lista_a_adyacencia(grafo)

    print("\nComponentes conexas del grafo: " + str(componentes_conexas(grafo)))

    if es_conexo(grafo):
        print ("Es un grafo conexo")
    else:
        print ("No es un grafo conexo")
    pass

if __name__ == '__main__':
    main()