class Node:

    def __init__(self, name):
        self.m_name = str(name)
        # Posteriormente colocar o objeto que o nodo vaireferenciar

    # devolve a representação na forma de string do node por forma a ser de leitura 'amigavel'
    def __str__(self):
        return "node " + self.m_name
    
    # devolve a representação 'oficial' do objeto, neste caso particular pode ser igual a __str__
    def __repr__(self):
        return "node " + self.m_name
    
    # obter um nome de um nodo
    def getName(self):
        return self.m_name
    
    # atualizar o nome 
    def setName(self, name):
        self.m_name = name
    
    def setId(self, id):
        self.id = id

    # metodo utilizado para comparar 2 nodos
    def __eq__(self, other):
        return self.m_name == other.m_name
    
    # devolve o hash de um nodo. Ao implementar o metodo __eq__ 
    # torna-se tambem necessario definir __hash__. Caso 
    # contrário o objeto torna-se unhashable
    def __hash__(self):
        return hash(self.m_name)
    
