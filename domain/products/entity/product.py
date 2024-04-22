from domain.products.exceptions.product_exceptions import PriceUnderMinException

class Product(object):
    nome: str
    descricao: str
    valor: int

    def __init__(self, nome: str, descricao: str, valor: int):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor

    def is_valid(self):
        if self.valor < 200:
            return False
        return True
