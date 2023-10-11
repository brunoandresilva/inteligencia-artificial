from node import Node
from graph import Graph
from queue import Queue


def main():
    g = Graph()
    
    g.add_edge("s","a",2)
    g.add_edge("s","e",2)
    g.add_edge("a","b",2)
    g.add_edge("e","f",5)
    g.add_edge("b","c",2)
    g.add_edge("f","g",2)
    g.add_edge("c","d",3)
    g.add_edge("g","t",2)
    g.add_edge("d","t",3)

    saida = -1
    while saida != 0:
        print('1-Imprimir Grafo')
        print('2-Desenhar Grafo')
        print('3-Imprimir nodos do Grafo')
        print('4-Imprimir arestas do Grafo')
        print('5-DFS')
        print('6-BFS')
        print('0-Sair')
        saida = int(input("Introduza a sua opcao-> "))
        if saida == 0:
            print("Saindo...")
        elif saida == 1:
            print(g.m_graph)
            l = input("Prima enter para continuar")
        elif saida == 2:
            g.desenha()
        elif saida == 3:
            print(g.m_graph.keys())
            l = input("Prima enter para continuar")
        elif saida == 4:
            print(g.imprime_aresta())
            l = input("Prima enter para continuar")
        elif saida == 5:
            inicio = input("Start Node-> ")
            fim = input("End Node-> ")
            print(g.procura_DFS(inicio, fim, path=[], visited=set()))
            l = input("Prima enter para continuar")
        elif saida == 6:
            inicio = input("Start Node-> ")
            fim = input("End Node-> ")
            print(g.procura_BFS(inicio, fim))
            l = input("Prima enter para continuar")
        else:
            print("You didn't add anything")
            l = input("Prima enter para continuar")


if __name__ == '__main__':
    main()
