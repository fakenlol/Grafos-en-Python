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
    aristas = []
    verts = grafo[0]

    for tupla in grafo[1]:
      list = [tupla[0],tupla[1]]
      revlist = [tupla[1],tupla[0]]
      if not list in aristas and not revlist in aristas:
        aristas.append(list)

    aristas_sup = aristas
    componentsToDelete = []

    for t in aristas:
      for st in aristas:
        if st[0] in t and not st[1] in t:
          componentsToDelete.append(st)
          t.append(st[1])
        elif st[1] in t and not st[0] in t:
          componentsToDelete.append(st)
          t.append(st[0])
        elif st[0] in t and st[1] in t and st != t:
          componentsToDelete.append(st)
      for toDelete in componentsToDelete:
        if toDelete in aristas:
          aristas.remove(toDelete)
      componentsToDelete = []

    status = 0

    for v in verts:
      for comps in aristas:
        if v in comps:
          status += 1
      if status == 0:
        aristas.append([v])
      status = 0

    return(aristas)

def es_conexo(grafo_lista):
    grafo = []
    grafo = componentes_conexas(grafo_lista)
    cant_comps = len(grafo)
    
    if cant_comps == 1:
        return True