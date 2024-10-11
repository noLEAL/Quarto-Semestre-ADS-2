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
                print("Opção 2 Busca de produtos (nome)")

            case '3':
                print("Opção 3 Busca de produtos (tipo)")

            case '4':
                print("Opção 4 Cadastrar produtos")

            case '5':
                print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
                print("Opção 5 Excluir produto")
                codigo = input(id("Digite o codigo do produto que deseja excluir:"))
                sistema.delete_product(codigo)
                print("Produto excluido acima ^")
                print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")

            case '6':
                print("Opção 6 Alterar valor de produto")

            case '7':
                print("Opção 7 Alterar estoque de produto")

            case 'SAIR':
                print("\nEncerrando o programa...")
                loop = 1

            case _:
                print("Opção inválida")

# Iniciar o programa
sistema = Sistemaderegistro()
menu()
