from heapq import merge
import sys

def lee_grafo_stdin():

  vertices=[]
  aristas=[]
  
  print("Ingrese la cantidad de vertices:")

  cantVertices = int(input())

  for i in range(0,cantVertices):
    vertices.append(input())
  
  ch = ''
  b = 0
  while ch != "-1":
    ch = input()
    tupla = tuple(ch.split())
    for tup in tupla:
      a = tup in vertices
      b += a
    if b == 2:
      b = 0
      aristas.append(tupla)
  grafo = (vertices, aristas)
  return grafo
  
def cuenta_grado(grafo):
  count = 0
  diccionario = {}

  list = [item for elem in grafo[1] for item in elem]
  
  for vertice in grafo[0]:
    diccionario[vertice] = list.count(vertice)
  
  print("Grados de todos los vertices: " + str(diccionario))
  return diccionario

def lista_a_adyacencia(grafo_lista):

  matriz = []
  ady = []

  ady = ady + [0]*(len(grafo_lista[0]))
  print("Matriz de adyacencia:")
  for vert1 in grafo_lista[0]:
    for vert2 in grafo_lista[0]:
      tup = (vert1,vert2)
      tup1 = (vert2,vert1)
      if tup in grafo_lista[1] or tup1 in grafo_lista[1]:
        ady[grafo_lista[0].index(vert2)] = 1
    matriz.append(ady)
    print(ady)
    ady = [0]*(len(grafo_lista[0]))
  return (grafo_lista[0], matriz)

def componentes_conexas(grafo):
    componentes = []

    for tupla in grafo[1]:
      
      list = [tupla[0],tupla[1]]
      revlist = [tupla[1],tupla[0]]

      if not list in componentes and not revlist in componentes:
        componentes.append(list)

    for tupla in componentes:
      for rTupla in componentes:
        if rTupla[0] in tupla and not rTupla[1] in tupla:
          tupla.append(rTupla[1])
          componentes.remove(rTupla)
        elif rTupla[1] in tupla and not rTupla[0] in tupla:
          tupla.append(rTupla[0])
          componentes.remove(rTupla)
    status = 0

    for vertice in grafo[0]:
        for tupla in componentes:
            if vertice in tupla:
              status = 1
        if status == 0:
            componentes.append([vertice])
        status = 0
    return(componentes)

def es_conexo(grafo_lista):
    grafo = []
    grafo = componentes_conexas(grafo_lista)
    cant_comps = len(grafo)
    
    if cant_comps:
        return True
        
#grafo1 = (["A","B","C","D","E"],[("A","B"),("B","C"),("D","E")])

def main():
    grafo = lee_grafo_stdin()
    print("Grafo en forma de lista: " + str(grafo))

    print("\nGrados de cada vertice del grafo: " + str(cuenta_grado(grafo)))

    print("\nLista de adyacencias: " + str(lista_a_adyacencia(grafo)))

    print("\nComponentes conexas del grafo: " + str(componentes_conexas(grafo)))

    if not es_conexo(grafo):
        print ("Es un grafo conexo")
    else:
        print ("No es un grafo conexo")
main()

