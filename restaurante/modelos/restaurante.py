class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.cardapio = []
        self.avaliacao = []
        Restaurante.restaurantes.append(self)

def __str__(self):
        return f"{self.nome} - {self.categoria}"

sushi = Restaurante("Japa food", "Japonesa")
print(sushi)