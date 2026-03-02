class ItemCardapio:
    def __init__(self, nome, descricao, preco, tamanho):
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.tamanho = tamanho

    def __str__(self):
        return f"{self.nome}  {self.descricao}: R$ {self.preco:.2f} | {self.tamanho}"
