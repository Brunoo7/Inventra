from gerenciador import GerenciarProdutos

def menu():
    opcao = 0
    prod = GerenciarProdutos()

    while opcao != 6:

        try:
            print("\n======ARMAZEM======")
            print("1 - Cadastrar Produto")
            print("2 - Listar Produtos")
            print("3 - Buscar Produto Pelo ID")
            print("4 - Buscar Produto Pelo Nome")
            print("5 - Atualizar Produto")
            print("6 - Excluir Produto")
            print("7 - Sair")
            opcao = int(input("Escolha uma opção: "))

            match opcao:

                case 1:
                    print("Cadastrar Produto")
                    prod.cadastrar_produto()

                case 2:
                    print("Listar Produtos")
                    prod.listar_produtos()

                case 3:
                    print("Buscar Produto Pelo ID")
                    prod.buscar_produto()

                case 4:
                    print("Buscar Produto Pelo Nome")
                    prod.buscar_por_nome()

                case 5:
                    print("Atualizar Produto")
                    prod.atualizar_produto()

                case 6:
                    print("Excluir Produto")
                    prod.excluir_produto()

                case 7:
                    print("Saindo...")

                case _:
                    print("Opção inválida")

        except ValueError:
            print("Opção inválida, tente novamente")
menu()
