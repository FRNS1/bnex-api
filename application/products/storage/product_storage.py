from abc import ABC, abstractclassmethod
from application.products.dto.product_dto import ProductDto

class ProductStorage(ABC):

    @abstractclassmethod
    def save_product(self, prd_dto: ProductDto):
        pass

    @abstractclassmethod
    def update_product(self, prd_id: int, prd_dto: ProductDto):
        pass

    @abstractclassmethod
    def get_product_by_id(self, prd_id: int):
        pass

    @abstractclassmethod
    def get_all_products(self):
        pass

    @abstractclassmethod
    def delete_product(self, prd_id: int):
        pass

