from gerenciador import GerenciarProdutos

def menu():
    opcao = 0
    prod = GerenciarProdutos()

    while opcao != 6:

        try:
            print("\n======ARMAZEM======")
            print("1 - Cadastrar Produto")
            print("2 - Listar Produtos")
            print("3 - Buscar Produto")
            print("4 - Atualizar Produto")
            print("5 - Excluir Produto")
            print("6 - Sair")
            opcao = int(input("Escolha uma opção: "))

            match opcao:

                case 1:
                    print("Cadastrar Produto")
                    prod.cadastrar_produto()

                case 2:
                    print("Listar Produtos")
                    prod.listar_produtos()

                case 3:
                    print("Buscar Produto")
                    prod.buscar_produto()

                case 4:
                    print("Atualizar Produto")
                    prod.atualizar_produto()

                case 5:
                    print("Excluir Produto")
                    prod.excluir_produto()

                case 6:
                    print("Saindo...")

                case _:
                    print("Opção inválida")

        except ValueError:
            print("Opção inválida, tente novamente")
menu()
