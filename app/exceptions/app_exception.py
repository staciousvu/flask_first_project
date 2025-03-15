
# from werkzeug.exceptions import HTTPException
from app.exceptions.error_code import ErrorCode

class AppException(Exception):
    def __init__(self,error_code:ErrorCode):
        self.error_code = error_code.code
        self.message = error_code.message
        self.status_code = error_code.http_status_code.value
        super().__init__(error_code.message)
