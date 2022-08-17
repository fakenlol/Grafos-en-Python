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
  print(grafo)
  return grafo
  
def cuenta_grado(grafo):
  count = 0
  diccionario = {}

  list = [item for elem in grafo[1] for item in elem]
  
  for vertice in grafo[0]:
    diccionario[vertice] = list.count(vertice)
  
  print(diccionario)
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

def componentes_conexas():
    componentes = []

    grafo = lee_grafo_stdin()

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
    print(componentes)

grafo1 = (["A","B","C","D","E"],[("A","B"),("B","C"),("D","E")])

#grafo = lee_grafo_stdin()
#cuenta_grado(grafo1)
componentes_conexas()