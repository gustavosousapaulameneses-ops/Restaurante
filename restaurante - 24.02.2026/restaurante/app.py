import os
from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.item_cardapio import ItemCardapio

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_selecao():
    limpar_tela()
    print('bem vindo a seleçao de menu voce deseja entrar como restaurante ou como cliente?')
    print('1 - Restaurante')
    print('2 - Cliente')
    print('3 - Sair')

    escolha = input('Digite a opção desejada: ')
    if escolha == '1':
        menu_restaurante()
    elif escolha == '2':
        menu_cliente()
    else:
        print('Opção inválida. Por favor, tente novamente.')
        return

def menu_cliente():
    while True:
        limpar_tela()
        print('Bem-vindo ao sistema do cliente')
        print('1 - Listar restaurantes')
        print('2 - Avaliar um restaurante')
        print('3 - Ver cardápio')
        print('4 - Voltar menu de seleção')

        escolha = input('Digite a opção desejada: ')

        if escolha == '1':
            limpar_tela()
            Restaurante.listar_restaurantes()
            input('\nPressione ENTER para voltar...')

        elif escolha == '2':
            limpar_tela()
            nome = input('Nome do restaurante: ')
            nota = float(input('Nota (0-5): '))
            cliente = input('Seu nome: ')

            for i in Restaurante.restaurantes:
                if i.nome == nome.title():
                    i.receber_avaliacao(cliente, nota)
                    print('Avaliado com sucesso!')
                    break
            else:
                print('Restaurante não encontrado.')

            input('\nPressione ENTER para voltar...')

        elif escolha == '3':
            limpar_tela()
            nome = input('Nome do restaurante: ')

            for i in Restaurante.restaurantes:
                if i.nome == nome.title():
                    i.exibir_cardapio()
            else:
                print('Restaurante não encontrado.')

            input('\nPressione ENTER para voltar...')

        elif escolha == '4':
            menu_selecao()

        else:
            print('Opção inválida')
            input('ENTER...')
    
    

def menu_restaurante():
    while True:
        limpar_tela()
        print('Bem-vindo ao menu do restaurante!')
        print('1 - Listar restaurantes')
        print('2 - Cadastrar um restaurante')
        print('3 - Remover um restaurante')
        print('4 - Alterar um restaurante')
        print('5 - Adicionar item ao cardápio')
        print('6 - Remover item do cardápio')
        print('7 - Ver cardápio')
        print('8 - voltar para menu de seleção')

        escolha = input('Digite a opção desejada: ')
        
        if escolha == '1':
            limpar_tela()
            for i in Restaurante.restaurantes:
                if not Restaurante.restaurantes:
                    print('Nenhum restaurante cadastrado')
                    input('Pressione ENTER para voltar...')
                    return
            else:
                Restaurante.listar_restaurantes()

        elif escolha == '2':
            limpar_tela()
            nome = input('Digite o nome do restaurante: ')
            categoria = input('Digite a categoria do restaurante: ')
            Restaurante(nome, categoria)
            print('Restaurante cadastrado com sucesso!')

        elif escolha == '3':
            limpar_tela()
            nome = input('Digite o nome do restaurante que deseja remover: ')
            for i in Restaurante.restaurantes:
                if i.nome == nome.title():
                    Restaurante.restaurantes.remove(i)
                    print(f'restaurante removido com sucesso {i.nome}')
                    input('Pressione ENTER para voltar...')
                    
            else:
                print('Restaurante não encontrado.')
            
        elif escolha == '4':
            limpar_tela()
            nome = input('Digite o nome do restaurante que deseja alterar: ')
            for i in Restaurante.restaurantes:
                if i.nome == nome.title():
                    nova_categoria = input('Digite a nova categoria do restaurante: ')
                    i.categoria = nova_categoria.title()
                    novo_nome = input('Digite o novo nome do restaurante: ')
                    i.nome = novo_nome.title()
                    input_status = input('Digite o novo status do restaurante (ativado/desativado): ')
                    if input_status.lower() in ['ativado', 'desativado']:
                        i.status = input_status.lower()
                    print(f'restaurante {i.nome} alterado com sucesso!')
                    input('Pressione ENTER para voltar...')
                    
            else:
                print('Restaurante não encontrado.')

        elif escolha == '5':
            limpar_tela()
            nome_restaurante = input('Digite o nome do restaurante para adicionar um item ao cardápio: ')
            for i in Restaurante.restaurantes:
                if i.nome == nome_restaurante.title():
                    nome_item = input('Digite o nome do item: ')
                    preco_item = float(input('Digite o preço do item: '))
                    descricao_item = input('Digite a descrição do item: ')
                    item = ItemCardapio(nome_item, preco_item, descricao_item)
                    i.adicionar_no_cardapio(item)
                    print(f'Item adicionado com sucesso ao cardápio do restaurante {i.nome}!')
                    input('Pressione ENTER para voltar...')
                    
            else:
                print('Restaurante não encontrado.')

        elif escolha == '6':
            limpar_tela()
            nome_restaurante = input('Digite o nome do restaurante para remover um item do cardápio: ')
            for i in Restaurante.restaurantes:
                if i.nome == nome_restaurante.title():
                    nome_item = input('Digite o nome do item que deseja remover: ')
                    for item in i.cardapio:
                        if item.nome == nome_item.title():
                            i.cardapio.remove(item)
                            print(f'Item removido com sucesso do cardápio do restaurante {i.nome}!')
                            input('Pressione ENTER para voltar...')
                            return
                    else:
                        print('Item não encontrado no cardápio.')
                        input('Pressione ENTER para voltar...')
                        return
            else:
                print('Restaurante não encontrado.')

        elif escolha == '7':
            limpar_tela()
            nome_restaurante = input('Digite o nome do restaurante para ver o cardápio: ')
            for i in Restaurante.restaurantes:
                if i.nome == nome_restaurante.title():
                    i.exibir_cardapio()
                    input('Pressione ENTER para voltar...')
                    return
            else:
                print('Restaurante não encontrado.')
                input('Pressione ENTER para voltar...')
                return

        elif escolha == '8':
            menu_selecao()
        


menu_selecao()