from enum import Enum

class SuccessCodes(Enum):
    SUCCESS = 'Success'
    UPDATED = 'UPDATED'
    DELETED = 'DELETED'

class ErrorCodes(Enum):
    PRODUCT_NOT_FOUND = 'Não foi encontrado nenhum produto com este id'
    ERROR = 'O valor do produto deve ser maior do que R$2,00'