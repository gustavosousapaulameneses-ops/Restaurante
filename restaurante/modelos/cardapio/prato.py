from item_cardapio import ItemCardapio

class Prato(ItemCardapio):
    def __init__(self, nome, preco, descricao, tamanho):
        super().__init__(nome, preco, descricao, tamanho)

    def __str__(self):
        return f"{self.nome} | {self.preco}: | {self.descricao} | {self.tamanho}"

arroz = Prato("Arroz", 10.00, "Arroz branco soltinho", "Grande")
print(arroz)
