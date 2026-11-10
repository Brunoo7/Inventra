import json

class Produto:
    def __init__(self, id, nome, preco, quantidade, categoria):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.categoria = categoria

    def to_dict(self):
        return {
            "ID": self.id,
            "Nome": self.nome,
            "Preço": self.preco,
            "Quantidade": self.quantidade,
            "Categoria": self.categoria
        }

class GerenciarProdutos:

    def __init__(self):
        try:

            with open("inventra_dados.json", "r", encoding="utf-8") as f:
                json.load(f)

        except FileNotFoundError:

            with open("inventra_dados.json", "w", encoding="utf-8") as f:
                json.dump([], f)

        except json.JSONDecodeError:

            with open("inventra_dados.json", "w", encoding="utf-8") as f:
                json.dump([], f)

    def cadastrar_produto(self):
        with open("inventra_dados.json", "r", encoding="utf-8") as f:
            produtos = json.load(f)

        maior_id = 0

        for produto in produtos:

            if maior_id < produto["ID"]:
                maior_id = produto["ID"]

        id = maior_id + 1

        while True:
            nome = input("Nome: ").strip()

            if nome != "":
                break

            print("O nome não pode ficar vazio!")

        while True:
            preco = float(input("Preço: "))

            if preco > 0:
                break

            print("Valor inválido! Digite um preço positivo.")

        while True:
            quantidade = int(input("Quantidade disponível: "))

            if quantidade >= 0:
                break
        
            print("Valor inválido! Digite uma quantidade positiva.")

        while True:
            categoria = input("Categoria: ").strip()

            if categoria != "":
                break

            print("Valor inválido! Digite uma quantidade maior ou igual a zero.")

        produto = Produto(id,nome, preco, quantidade, categoria)
        dados = produto.to_dict()
        produtos.append(dados)
        
        with open("inventra_dados.json", "w", encoding="utf-8") as f:
            json.dump(produtos, f, ensure_ascii=False, indent=4)

    def listar_produtos(self):
        with open("inventra_dados.json", "r", encoding="utf-8") as f:
            dados_lidos = json.load(f)
            for produto in dados_lidos:
                print(produto)

    def buscar_produto(self):
        busca_id = int(input("Qual o ID do produto que você quer buscar? "))
        with open("inventra_dados.json", "r", encoding="utf-8") as f:
            busca = json.load(f)

        encontrado = False

        for produto in busca:
            if busca_id == produto["ID"]:
                encontrado = True
                print(produto)
        if encontrado == False:
            print("Produto não encontrado")

    def atualizar_produto(self):
        busca_id = int(input("Qual o ID do produto que você quer atualizar? "))
        with open("inventra_dados.json", "r", encoding="utf-8") as f:
            busca = json.load(f)

        encontrado = False

        for produto in busca:
            if busca_id == produto["ID"]:
                encontrado = True
                print(produto)
                mod = input("Qual item do produto quer modificar? ")

                if mod in ["Nome", "Preço", "Quantidade", "Categoria"]:

                    if mod in ["Nome", "Categoria"]:
                        while True:
                            item = input("Digite a modificação: ").strip()

                            if item != "":
                                break
                            
                            print(f"{mod} não pode ficar vazio(a)!")

                    elif mod == "Preço":
                        while True:
                            item = float(input("Digite a modificação: "))
                        
                            if item > 0:
                                break
                            
                            print("Valor inválido! Digite um preço positivo.")

                    elif mod == "Quantidade":
                        while True:
                            item = int(input("Digite a modificação: "))

                            if item >= 0:
                                break
                            
                            print("Valor inválido! Digite uma quantidade maior ou igual a zero.")

                    produto[mod] = item

                    with open("inventra_dados.json", "w", encoding="utf-8") as f:
                        json.dump(busca, f, ensure_ascii=False, indent=4)
                else:
                    print("Item inválido")

        if encontrado == False:
            print("Produto não encontrado")

    def excluir_produto(self):
        busca_id = int(input("Qual o ID do produto que você quer excluir? "))
        with open("inventra_dados.json", "r", encoding="utf-8") as f:
            busca = json.load(f)

        encontrado = False

        for produto in busca:

            if busca_id == produto["ID"]:
                encontrado = True
                print(produto)
                decisao = input("Tem certeza que quer excluir esse produto? (s/n) ")

                if decisao == "s":
                    busca.remove(produto)

                    with open("inventra_dados.json", "w", encoding="utf-8") as f:
                        json.dump(busca, f, indent=4, ensure_ascii=False)
                    print("Produto excluido")

                    break

                else:
                    print("Produto NÃO excluido")

        if encontrado == False:
            print("Produto não encontrado")

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
            print("6 - Saindo...")
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
