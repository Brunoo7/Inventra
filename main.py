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
