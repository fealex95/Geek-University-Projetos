from typing import List, Dict
from time import sleep

from models.produto import Produto
from utils.helper import formatar_real_moeda

produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = []

def main() -> None:
    menu()

def menu() -> None:
    print('============================================')
    print('=============== Bem Vindo(a) ===============')
    print('================ Geek Shop =================')
    print('============================================')

    print('Escolha uma opção abaixo: ')
    print('[1] - Cadastrar produto')
    print('[2] - Listar produto')
    print('[3] - Comprar produto')
    print('[4] - Visualizar carrinho')
    print('[5] - Fechar pedido')
    print('[6] - Sair do sistema')

    opcao: int = int(input())

    if opcao == 1: 
        cadastrar_produto()
    elif opcao == 2: 
        listar_produtos()
    elif opcao == 3: 
        comprar_produto()
    elif opcao == 4: 
        visualizar_carrinho()
    elif opcao == 5: 
        fechar_pedido()
    elif opcao == 6: 
        print('Volte sempre!')
        exit()
    else:
        print("Opção Inválida")
        sleep(2)
        menu()

def cadastrar_produto() -> None:
    print('Cadastro de Produto')
    print('-------------------')

    nome: str = input('Informe o nome do produto: ')
    preco: float = float(input('Informe o valor do produto: '))

    produto: Produto = Produto(nome, preco)

    produtos.append(produto)

    print(f'Produto {produto.nome} com valor de {formatar_real_moeda(produto.preco)} foi cadastrado com sucesso!')

    sleep(2)
    menu()

def listar_produtos() -> None:
    if len(produtos) > 0:
        print('Listagem de Produtos')
        print('--------------------')

        for produto in produtos:
            print(produto)
            print('---------------------------------')
            sleep(1)

    else:  
        print('Ainda não existe produtos cadastrados')

    sleep(2)
    menu()

def comprar_produto() -> None:
    if len(produtos) > 0:
        print('Escolha um produto abaixo e digite o código para adicionar no carrinho: ')
        print('------------------------------------------------------------------------')
        print('========================= Produtos Disponiveis =========================')

        for produto in produtos:
            print(produto)
            sleep(1)
        
        codigo: int = int(input())

        produto: Produto = get_produto_id(codigo)

        if produto:
            if len(carrinho) > 0:
                tem_no_carrinho: bool = False

                for item in carrinho:
                    quant: int = item.get(produto)
                    if quant:
                        item[produto] = quant + 1
                        print(f'O produto {produto.nome} foi atualizado para quantidade {quant + 1} unidades!')
                        tem_no_carrinho = True
                        sleep(2)
                        menu()
                    
                if not tem_no_carrinho:
                    prod = {produto: 1}
                    carrinho.append(prod)
                    print(f'O produto {produto.nome} foi adicionado ao carrinho!')
                    sleep(2)
                    menu()

            else:
                item = {produto: 1}
                carrinho. append(item)
                print(f'O Produto {produto.nome} for adicionado ao carrinho!')
                sleep(2)
                menu()
        else:
            print(f'O Produto com código {codigo} não foi encontrado')
            sleep(2)
            menu()
    else:
        print('Não existe produtos a venda!')
        sleep(2)
        menu()

def visualizar_carrinho() -> None:
    if len(carrinho) > 0:
        print('Produtos no carrinho: ')
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Qtde: {dados[1]}')
                print('-----------------')
                sleep(1)

    else:
        print('Ainda não existe produtos no carrinho')
    
    sleep(2)
    menu()

def fechar_pedido() -> None:
    if len(carrinho) > 0:
        valor_total: float = 0
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Qtde.: {dados[1]}')
                valor_total += dados[0].preco * dados[1]
                print('----------------------------------')
                sleep(1)
        
        print(f'Sua compra totaliza {formatar_real_moeda(valor_total)}')
        print('Volte Sempre!')
        carrinho.clear()
        sleep(5)
    else:
        print('Você ainda não comprou nada!')
    
    sleep(2)
    menu()

def get_produto_id(codigo: int) -> Produto:
    p: Produto = None
    for produto in produtos:
        if produto.codigo == codigo:
            p = produto
    return p

if __name__ == '__main__':
    main()