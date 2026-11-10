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
            with open("dados.json", "r", encoding="utf-8") as f:
                json.load(f)
        except FileNotFoundError:
            with open("dados.json", "w", encoding="utf-8") as f:
                json.dump([], f)
        except json.JSONDecodeError:
            with open("dados.json", "w", encoding="utf-8") as f:
                json.dump([], f)

    def cadastrar_produto(self):
        with open("dados.json", "r", encoding="utf-8") as f:
            produtos = json.load(f)
        maior_id = 0
        for produto in produtos:
            if maior_id < produto["ID"]:
                maior_id = produto["ID"]
        id = maior_id + 1
        nome = input("Nome: ")
        preco = float(input("Preço: "))
        quantidade = int(input("Quantidade disponível: "))
        categoria = input("Categoria: ")
        produto = Produto(id,nome, preco, quantidade, categoria)
        dados = produto.to_dict()
        produtos.append(dados)
        with open("dados.json", "w", encoding="utf-8") as f:
            json.dump(produtos, f, ensure_ascii=False, indent=4)

    def listar_produtos(self):
        with open("dados.json", "r", encoding="utf-8") as f:
            dados_lidos = json.load(f)
            for produto in dados_lidos:
                print(produto)

    def buscar_produto(self):
        busca_id = int(input("Qual o ID do produto que você quer buscar? "))
        with open("dados.json", "r", encoding="utf-8") as f:
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
        with open("dados.json", "r", encoding="utf-8") as f:
            busca = json.load(f)


        encontrado = False


        for produto in busca:
            if busca_id == produto["ID"]:
                encontrado = True
                print(produto)
                mod = input("Qual item do produto quer modificar? ")


                if mod in ["Nome", "Preço", "Quantidade", "Categoria"]:
                    item = input("Digite a modificação: ")


                    if mod == "Preço":
                        item = float(item)


                    elif mod == "Quantidade":
                        item = int(item)


                    produto[mod] = item


                    with open("dados.json", "w", encoding="utf-8") as f:
                        json.dump(busca, f, ensure_ascii=False, indent=4)
                else:
                    print("Item inválido")


        if encontrado == False:
            print("Produto não encontrado")
