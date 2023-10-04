import network as nx

import matplotlib.pyplot as plt

from node import Node

class Graph:

    def __init__(self, directed=False):
        self.m_nodes = []
        self.m_directed = directed
        self.m_graph = {}


    # escrever o grafo como string
    def __str__ (self):
        out = " "
        for key in self.m_graph.keys():
            out = out + "node " + str(key) + ": " + str(self.m_graph[key]) + "\n"
        return out
