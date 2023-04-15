class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None
        
class BinaryTree:
    def __init__(self):
        self.raiz = None
        self.qtd_nos = 0
        
    def inserir(self, valor):
        novo_no = No(valor)
        
        if self.raiz is None:
            self.raiz = novo_no
        else:
            atual = self.raiz
            
            while True:
                if valor < atual.valor:
                    if atual.esquerda is None:
                        atual.esquerda = novo_no
                        break
                    else:
                        atual = atual.esquerda
                else:
                    if atual.direita is None:
                        atual.direita = novo_no
                        break
                    else:
                        atual = atual.direita
        
        self.qtd_nos += 1
        
    def quantidade(self):
        return self.qtd_nos

