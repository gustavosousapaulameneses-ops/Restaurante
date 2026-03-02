from modelos.cardapio.item_cardapio import ItemCardapio
from modelos.avaliacao  import Avaliacao

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria, status='desativado'):
        self.nome = nome.title()
        self.categoria = categoria.upper()
        self.cardapio = []
        self.avaliacao = []
        self.status = status
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.categoria} | {self.status}'

    @classmethod
    def listar_restaurantes(cls):
        if not cls.restaurantes:
            print('Nenhum restaurante cadastrado.')
            return
        else:
            print(f'{"Nome do restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Avaliação".ljust(25)} | {"Status".ljust(25)}')
            for i in cls.restaurantes:
                print(f'{i.nome.ljust(25)} | {i.categoria.ljust(25)} | {str(i.media_avaliacao).ljust(25)} | {i.status.ljust(25)}')

    def receber_avaliacao(self, cliente, nota, ):
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self.avaliacao.append(avaliacao)
 
    @property
    def media_avaliacao(self):
        if not self.avaliacao: 
            return 0.0

        soma_das_notas = 0
        for i in self.avaliacao:
            soma_das_notas = soma_das_notas + i.nota
        quantidade_de_notas = len(self.avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media
    
        round('Valor ou o calculo','quantidade de numeros após a virgula')
        
        round(calculo, 1)

    def adicionar_no_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self.cardapio.append(item)

    def exibir_cardapio(self):
        print(f'Cardápio do restaurante {self.nome}')
        print(f'{"Nome do item".ljust(25)} | {"Preço".ljust(25)} | {"Descrição".ljust(25)}')
        for i in self.cardapio:
            print(f'{i.nome.ljust(25)} | {str(i.preco).ljust(25)} | {i.descricao.ljust(25)}')
