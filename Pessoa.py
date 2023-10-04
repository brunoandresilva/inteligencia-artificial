class Pessoa:
    populacao = 0
    def __init__(self, minhaIdade):
        self.idade = minhaIdade
        Pessoa.populacao += 1
    def get_populacao(self):
        return Pessoa.populacao
    def get_idade(self):
        return self.idade
    

p1 = Pessoa(22)
p2 = Pessoa(22)
p3 = Pessoa(22)
p4 = Pessoa(22)

print('População: ' + str(p1.populacao))