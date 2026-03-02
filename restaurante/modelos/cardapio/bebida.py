from item_cardapio import ItemCardapio

class Bebida(ItemCardapio):
    def __init__(self, nome, preco, descricao, tamanho):
        super().__init__(nome, preco, descricao, tamanho)

    def __str__(self):
        return f"{self.nome} | {self.preco}: | {self.descricao} | {self.tamanho}"

cafe = Bebida("Café", 5.00, "Quero cafe!!! meda cafe !!!)", "Médio")
print(cafe)