from django.views import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from application.products.manager.product_manager import ProductManager
from application.products.dto.product_dto import ProductDto
import json

class ProductsView(View):
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        data = json.loads(request.body)
        dto = ProductDto(
            data.get("nome"),
            data.get("descricao"),
            int(data.get("valor"))
        )
        manager = ProductManager()
        response = manager.save_product(dto)
        try:
            if response['code'] == 'ERROR':
                return JsonResponse(response, status=200)
        except:
            response_dict = vars(response)
            return JsonResponse(response_dict, status=201)

    def get(self, request):
        manager = ProductManager()
        response = manager.get_all_products()
        response_data = [vars(product) for product in response]
        return JsonResponse(response_data, status=200, safe=False)

class ProductsIdFnView(View):
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def put(self, request, id):
        data = json.loads(request.body)
        dto = ProductDto(
            data.get('nome'),
            data.get('descricao'),
            data.get('valor')
        )
        manager = ProductManager()
        response = manager.update_product(id, dto)
        return JsonResponse(response, status=200)

    def delete(self, request, id):
        manager = ProductManager()
        response = manager.delete_product(id)
        return JsonResponse(response, status=200)

    def get(self, request, id):
        manager = ProductManager()
        response = manager.get_product_by_id(id)
        response_dict = vars(response)
        return JsonResponse(response_dict, status=200)

