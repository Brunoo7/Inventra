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
