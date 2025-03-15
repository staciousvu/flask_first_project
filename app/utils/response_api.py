from flask import jsonify
class ApiResponse:
    def success_response(message:str,data):
        return {
            "is_success":True,
            "message":message,
            "data":data
        }
    def error_response(message:str):
        return {
            "is_success":False,
            "message":message
        }
