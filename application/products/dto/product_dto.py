from domain.products.entity.product import Product
from typing import Optional

class ProductDto(object):
    product_id: Optional[int]
    nome: str
    descricao: str
    valor: int

    def __init__(self, nome: str, descricao: str, valor: int):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor

    def to_domain(self):
        return Product(
            self.nome,
            self.descricao,
            self.valor
        )
    
    def to_dto(prd: Product):
        return ProductDto(
            prd.nome,
            prd.descricao,
            prd.valor
        )