from application.products.storage.product_storage import ProductStorage
from application.products.dto.product_dto import ProductDto
from domain.products.enums.product_enums import ErrorCodes, SuccessCodes
from products.models import Product

class ProductManager(object):

    def save_product(self, prd_dto: ProductDto):
        product = prd_dto.to_domain()
        if not product.is_valid():
            return {'message': ErrorCodes.ERROR.value, 'code': ErrorCodes.ERROR.name}
        product = Product.objects.create(
            nome=product.nome,
            descricao=product.descricao,
            valor=product.valor
        )
        final_dto = ProductDto.to_dto(product)
        return final_dto
    
    def update_product(self, prd_id: int, prd_dto: ProductDto):
        try:
            prd = Product.objects.get(pk=prd_id)
        except Product.DoesNotExist:
            return {'message': ErrorCodes.PRODUCT_NOT_FOUND.value, 'code': ErrorCodes.PRODUCT_NOT_FOUND.name}
        prd.nome = prd_dto.nome
        prd.descricao = prd_dto.descricao
        prd.valor = prd_dto.valor
        prd.save()
        return {'message': SuccessCodes.UPDATED.value, 'code': SuccessCodes.UPDATED.name}
    
    def delete_product(self, prd_id: int):
        try:
            prd = Product.objects.get(pk=prd_id)
        except Product.DoesNotExist:
            return {'message': ErrorCodes.PRODUCT_NOT_FOUND.value, 'code': ErrorCodes.PRODUCT_NOT_FOUND.name}
        prd.delete()
        return {'message': SuccessCodes.DELETED.value, 'code': SuccessCodes.DELETED.name}
    
    def get_all_products(self):
        products = Product.objects.all()
        list = []
        for product in products:
            dto = ProductDto(
                product.nome,
                product.descricao,
                product.valor
            )
            dto.product_id = product.product_id
            list.append(dto)
        return list
    
    def get_product_by_id(self, prd_id: int):
        try:
            prd = Product.objects.get(pk=prd_id)
        except Product.DoesNotExist:
            return None
        dto = ProductDto.to_dto(prd)
        dto.product_id = prd.product_id
        return dto
