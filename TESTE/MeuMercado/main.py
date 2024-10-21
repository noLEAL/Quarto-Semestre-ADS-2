from mercado_db import *


# Menu principal
def menu():
    """Função de menu para interagir com o usuário através de um loop"""
    loop = 0
    while loop == 0 :

        print("\nMenu:")
        print("1 - Listar produtos")
        print("2 - Busca de produtos (nome)")
        print("3 - Busca de produtos (tipo)")
        print("4 - Cadastrar produtos")
        print("5 - Excluir produto")
        print("6 - Alterar valor de produto")
        print("7 - Alterar estoque de produto")
        print("Sair - Encerrar o programa")

        opcao = input("\nEscolha uma opção: ").upper()

        try:
            match opcao:

                case 'ESC':
                    sistema.basedate()

                case '1':
                    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
                    print("Opção 1 Listar produtos ")
                    sistema.view_products()
                    print("Produtos Listados acima ^")
                    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
                case '2':
                    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
                    print("Opção 2 Busca de produtos (nome)")
                    local_product = input("Digite o nome do produto que você gostaria de pesquisar?")
                    sistema.search_product_name(local_product)
                    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
                case '3':
                    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
                    print("Opção 3 Busca de produtos (tipo)")
                    local_product = input("Digite o tipo de produto que você gostaria de pesquisar?")
                    sistema.search_product_name(local_product)
                    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
                case '4':
                    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
                    print("Opção 4 Cadastrar produtos")
                    ##
                    ##Necessario colocar senha para seguir os requisitos
                    ##
                    local_nome = input("Digite o nome do produto que deseja cadastrar:")
                    local_tipo = input("Digite o tipo do produto que deseja cadastrar:")
                    local_valor = input("Digite o valor do produto que deseja cadastrar:")
                    local_estoque = input("Digite o estoque do produto que deseja cadastrar:")
                    sistema.register_product(local_nome, local_tipo, local_valor, local_estoque)
                    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
                case '5':
                    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
                    print("Opção 5 Excluir produto")
                    ##
                    ##Necessario colocar senha para seguir os requisitos
                    ##
                    codigo = input(id("Digite o codigo do produto que deseja excluir:"))
                    sistema.delete_product(codigo)
                    print("Produto excluido acima ^")
                    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
                case '6':
                    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
                    print("Opção 6 Alterar valor de produto")
                    ##
                    ##Necessario colocar senha para seguir os requisitos
                    ##
                    local_id = input("Digite o codigo do produto que deseja alterar:")
                    local_valor = input("Digite o valor que você deseja para o produto em questão:")
                    local_op = "valor"
                    sistema.update_product(local_id, local_valor,local_op)
                    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
                case '7':
                    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
                    print("Opção 7 Alterar estoque de produto")
                    ##
                    ##Necessario colocar senha para seguir os requisitos
                    ##
                    local_id = input("Digite o codigo do produto que deseja alterar:")
                    local_valor = input("Digite o valor que você deseja para o produto em questão:")
                    local_op = "estoque"
                    sistema.update_product(local_id, local_valor,local_op)
                    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
                case 'SAIR':
                    print("\nEncerrando o programa...")
                    loop = 1

                case _:
                    print("Opção inválida")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

# Iniciar o programa
sistema = Sistemaderegistro()
menu()
