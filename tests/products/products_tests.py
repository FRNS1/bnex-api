import unittest
from domain.products.entity.product import Product
from application.products.dto.product_dto import ProductDto

class ProductInstantiateTest(unittest.TestCase):
    def test_instantiate_product_not_valid(self):
        product = Product("Teste", "Teste", 1)
        self.assertFalse(product.is_valid())

    def test_instatiante_product_valid(self):
        product = Product("Teste", "Teste", 500)
        self.assertTrue(product.is_valid())

class ProductApplicationLayerTests(unittest.TestCase):
    def test_instantiate_dto(self):
        dto = ProductDto("Teste", "Teste", 500)
        self.assertIsInstance(ProductDto, dto)

    def test_to_domain(self):
        dto = ProductDto("Teste", "Teste", 500)
        product = dto.to_domain()
        self.assertIsInstance(Product, product)

    def test_to_dto(self):
        product = Product("Teste", "Teste", 500)
        dto = ProductDto.to_dto(product)
        self.assertIsInstance(ProductDto, dto)