from asyncio import Queue
import queue
import network as nx
import math
import matplotlib.pyplot as plt

from node import Node

class Graph:

    def __init__(self, directed=False):
        self.m_nodes = []
        self.m_directed = directed
        self.m_graph = {}
        self.m_h = {} # dicionario para posteriormente armazenar as heuristicas para cada nodo (pesquisa informada)


    # escrever o grafo como string
    def __str__ (self):
        out = " "
        for key in self.m_graph.keys():
            out = out + "node " + str(key) + ": " + str(self.m_graph[key]) + "\n"
        return out
    
    def get_node_by_name(self, name):
        search_node = Node(name)
        for node in self.m_nodes:
            if node == search_node:
                return node
            else:
                return None
            
    def imprime_aresta(self):
        listaA = ""
        lista = self.m_graph.keys()
        for nodo in lista:
            for(nodo2, custo) in self.m_graph[nodo]:
                listaA = listaA + nodo + "->" + nodo2 + " custo: " + str(custo) + "\n"
        return listaA
    
    
    # def add_node(self, name):
    #     new_node = Node(name)
    #     self.m_nodes.append(new_node)
    #     return
    
    def add_edge(self, node1, node2, weight):
        n1 = Node(node1)
        n2 = Node(node2)
        if (n1 not in self.m_nodes):
            n1_id = len(self.m_nodes) # numeraçao sequencial
            n1.setId(n1_id)
            self.m_nodes.append(n1)
            self.m_graph[node1] = []
        else:
            n1 = self.get_node_by_name(node1)

        if (n2 not in self.m_nodes):
            n2_id = len(self.m_nodes)
            n2.setId(n2_id)
            self.m_nodes.append(n2)
            self.m_graph[node2] = []
        else:
            n2 = self.get_node_by_name(node2)
        self.m_graph[node1].append((node2, weight))


    def getNodes(self):
        return self.m_nodes

    def get_arc_cost(self, node1, node2):
        custoT = math.inf
        a = self.m_graph[node1]  # lista de arestas para aquele nodo
        for (nodo, custo) in a:
            if nodo == node2:
                custoT = custo
        return custoT
    
    def calcula_custo(self, caminho):
        teste = caminho
        custo = 0
        i = 0
        while i+1 < len(teste):
            custo = custo + self.get_arc_cost(teste[i], teste[i+1])
            i = i + 1
        return custo
    
    def procura_DFS(self, start, end, path=[], visited=set()):
        path.append(start)
        visited.add(start)

        if start == end:
            # calcular o custo do caminho funçao calcula custo
            custoT = self.calcula_custo(path)
            return(path, custoT)
        
        for(adjacente, peso) in self.m_graph[start]:
            if adjacente not in visited:
                resultado = self.procura_DFS(adjacente, end, path, visited)
                if resultado is not None:
                    return resultado
        path.pop() # se nao encontra remover o que esta no caminho
        return None
    
    def procura_BFS(self, start, end):
        # definir nodos visitados para evitar ciclos
        visited = set()
        fila = Queue()
        custo = 0
        # adicionar o nodo inicial a fila e aos visitados
        fila.put(start)
        visited.add(start)

        # garantir que o node nao tem pais
        parent = dict()
        parent[start] = None

        path_found = False
        while not fila.empty() and path_found == False:
            nodo_atual = fila.get()
            if nodo_atual == end:
                path_found = True
            else:
                for (adjacente, peso) in self.m_graph[nodo_atual]:
                    if adjacente not in visited:
                        fila.put(adjacente)
                        parent[adjacente] = nodo_atual
                        visited.add(adjacente)
        # recontruir o caminho
        path = []
        if path_found:
            path.append(end)
            while parent[end] is not None:
                path.append(parent[end])
                end = parent[end]
            path.reverse()
            # função calcula custo caminho
            custo = self.calcula_custo(path)

        return (path, custo)
    
    