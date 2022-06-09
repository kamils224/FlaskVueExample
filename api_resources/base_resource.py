from typing import Dict, Optional, Any

from flask_restful import Resource


class BaseResource(Resource):

    def success_response(self, data: Optional[Any] = None, status_code: int = 200):
        return {"response": data}, status_code

    def error_response(self, error: Optional[str] = None, status_code: int = 400):
        if error is None:
            error = "Invalid request"
        return {"error": error}, status_code

    def error_not_found(self, error: Optional[str] = None, status_code: int = 404):
        if error is None:
            error = "Not found"
        return {"error": error}, status_code