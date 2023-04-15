from main import BinaryTree

def test_quantidade_arvore():
    arvore = BinaryTree()
    arvore.inserir_30()
    assert arvore.quantidade() == 30
