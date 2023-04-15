class BinaryTree:
    def __init__(self):
        self.root = None
        self.size = 0
        
    def inserir_30(self):
        for i in range(1, 31):
            self.inserir(i)

    def inserir(self, valor):
        if self.root is None:
            self.root = Node(valor)
            self.size += 1
        else:
            self._inserir(valor, self.root)

    def _inserir(self, valor, node_atual):
        if valor < node_atual.valor:
            if node_atual.esquerda is None:
                node_atual.esquerda = Node(valor)
                self.size += 1
            else:
                self._inserir(valor, node_atual.esquerda)
        elif valor > node_atual.valor:
            if node_atual.direita is None:
                node_atual.direita = Node(valor)
                self.size += 1
            else:
                self._inserir(valor, node_atual.direita)
        else:
            # Ignorar valores duplicados
            pass

    def quantidade(self):
        return self.size

class Node:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None
