import json
from produto import Produto

class GerenciarProdutos:

    def __init__(self):
        try:
            with open("inventra_dados.json", "r", encoding="utf-8") as f:
                dados = json.load(f)

            if not isinstance(dados, list):
                dados = []

            produtos_validos = []
            for produto in dados:
                if isinstance(produto, dict) and all(chave in produto for chave in ["ID", "Nome", "Preço", "Quantidade", "Categoria"]):
                    if type(produto["ID"]) == int and isinstance(produto["Nome"], str) and isinstance(produto["Preço"], (float, int)) and type(produto["Quantidade"]) == int and isinstance(produto["Categoria"], str):
                        if not produto["Nome"].strip() == "" and not produto["Categoria"].strip() == "":
                            if produto["Preço"] > 0 and produto["ID"] > 0:
                                if produto["Quantidade"] >= 0:
                                    produtos_validos.append(produto)
                        
            with open("inventra_dados.json", "w", encoding="utf-8") as f:
                    json.dump(produtos_validos, f, ensure_ascii=False, indent=4)

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
            try:
                preco = float(input("Preço: "))

                if preco > 0:
                    break

                print("Valor inválido! Digite um preço positivo.")
                
            except ValueError:
                print("Digite apenas números")

        while True:
            try:
                quantidade = int(input("Quantidade disponível: "))

                if quantidade >= 0:
                    break
            
                print("Digite uma quantidade maior ou igual a zero.")

            except ValueError:
                print("Digite apenas números")

        while True:
            categoria = input("Categoria: ").strip()

            if categoria != "":
                break

            print("A categoria não pode ficar vazia!")

        produto = Produto(id,nome, preco, quantidade, categoria)
        dados = produto.to_dict()
        produtos.append(dados)
        
        with open("inventra_dados.json", "w", encoding="utf-8") as f:
            json.dump(produtos, f, ensure_ascii=False, indent=4)

    def listar_produtos(self):
        with open("inventra_dados.json", "r", encoding="utf-8") as f:
            dados_lidos = json.load(f)
            if dados_lidos == []:
                print("Nenhum produto cadastrado!")
            else:
                for produto in dados_lidos:
                    print(produto)

    def buscar_produto(self):
        while True:
            try:
                busca_id = int(input("Qual o ID do produto que você quer buscar? "))
                if busca_id > 0:
                    break

                print("O ID tem que ser um número positivo")

            except ValueError:
                print("O ID tem que ser um número inteiro!")

        with open("inventra_dados.json", "r", encoding="utf-8") as f:
            busca = json.load(f)

        encontrado = False

        for produto in busca:

            if busca_id == produto["ID"]:
                encontrado = True
                print(produto)

        if encontrado == False:
            print("Produto não encontrado")

    def buscar_por_nome(self):
        while True:
            busca_nome = input("Qual o nome do produto que você quer buscar? ").strip().lower()
            encontrado = False

            if busca_nome != "":

                with open("inventra_dados.json", "r", encoding="utf-8") as f:
                    busca = json.load(f)

                for produto in busca:

                    if busca_nome in produto["Nome"].lower():
                        encontrado = True
                        print(produto)

                if encontrado == False:
                    print("Produto não encontrado")
                break

            else:
                print("O nome não pode ficar vazio!")

    def filtrar_por_categoria(self):
        while True:
            busca_categoria = input("Qual categoria você quer buscar? ").strip().lower()
            encontrado = False
            if busca_categoria != "":

                with open("inventra_dados.json", "r", encoding="utf-8") as f:
                    busca = json.load(f)

                for produto in busca:
                    if busca_categoria == produto["Categoria"].lower():
                        encontrado = True
                        print(produto)

                if encontrado == False:
                    print("Categoria não encontrada")
                break

            else:
                print("A categoria não pode ficar vazia!")

    def atualizar_produto(self):
        while True:
            try:
                busca_id = int(input("Qual o ID do produto que você quer atualizar? "))
                if busca_id > 0:
                    break

                print("O ID tem que ser um número positivo")

            except ValueError:
                print("O ID tem que ser um número inteiro!")

        with open("inventra_dados.json", "r", encoding="utf-8") as f:
            busca = json.load(f)

        encontrado = False

        for produto in busca:
            if busca_id == produto["ID"]:
                encontrado = True
                print(produto)
                mod = input("Qual item do produto quer modificar? ").strip().capitalize()

                if mod in ["Nome", "Preço", "Quantidade", "Categoria"]:

                    if mod in ["Nome", "Categoria"]:
                        while True:
                            item = input("Digite a modificação: ").strip()

                            if item != "":
                                break
                            
                            print(f"{mod} não pode ficar vazio(a)!")

                    elif mod == "Preço":
                        while True:
                            try:
                                item = float(input("Digite a modificação: "))
                            
                                if item > 0:
                                    break
                                
                                print("Valor inválido! Digite um preço positivo.")
                            except ValueError:
                                print("Digite apenas números")

                    elif mod == "Quantidade":
                        while True:
                            try:
                                item = int(input("Digite a modificação: "))

                                if item >= 0:
                                    break
                                
                                print("Valor inválido! Digite uma quantidade maior ou igual a zero.")

                            except ValueError:
                                print("Digite apenas números")

                    produto[mod] = item

                    with open("inventra_dados.json", "w", encoding="utf-8") as f:
                        json.dump(busca, f, ensure_ascii=False, indent=4)
                else:
                    print("Item inválido")

        if encontrado == False:
            print("Produto não encontrado")

    def excluir_produto(self):
        while True:
            try:
                busca_id = int(input("Qual o ID do produto que você quer excluir? "))
                if busca_id > 0:
                    break

                print("O ID tem que ser um número positivo")

            except ValueError:
                print("O ID tem que ser um número inteiro!")

        with open("inventra_dados.json", "r", encoding="utf-8") as f:
            busca = json.load(f)

        encontrado = False

        for produto in busca:

            if busca_id == produto["ID"]:
                encontrado = True
                print(produto)
                while True:
                    decisao = input("Tem certeza que quer excluir esse produto? (s/n) ").strip().lower()
                    if decisao not in ["s", "n"]:
                        print("Digite apenas s ou n")
                    else:
                        break

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

    def alerta_estoque_baixo(self):
        while True:
            try:
                limite = int(input("Digite o limite de estoque: "))
                encontrado = False
                if limite < 0:
                    print("Digite um limite maior ou igual a zero.")

                else:
                    with open("inventra_dados.json", "r", encoding="utf-8") as f:
                        busca = json.load(f)

                    for produto in busca:
                        if limite >= produto["Quantidade"]:
                            encontrado = True
                            print(produto)
                            
                    if encontrado == False:
                        print("Não tem produtos com o estoque igual ou menor do que o limite selecionado!")    
                    break

            except ValueError:
                print("O limite deve ser um número")