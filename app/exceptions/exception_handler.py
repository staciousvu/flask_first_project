from app.exceptions.app_exception import AppException
from flask import Flask
from app.utils.response_api import ApiResponse

def register_error_handlers(app: Flask):
    @app.errorhandler(AppException)
    def handler_app_exception(error: AppException):
        response = ApiResponse.error_response(error.message)
        return response, 400