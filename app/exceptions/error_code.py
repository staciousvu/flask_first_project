from enum import Enum
from http import HTTPStatus


class ErrorCode(Enum):
    PRODUCT_NOT_FOUND = (1000,"Product not found",HTTPStatus.NOT_FOUND)
    CATEGORY_NOT_FOUND = (1001,"Category not found",HTTPStatus.NOT_FOUND)

    def __init__(self,code:int,message:str,http_status_code:HTTPStatus):
        self.code = code
        self.message = message
        self.http_status_code=http_status_code
