from fastapi.responses import JSONResponse

class CustomResponse:
    @staticmethod
    def success(data=None, message="Success", status_code=200):
        return JSONResponse(
            status_code=status_code,
            content={
                "success": True,
                "message": message,
                "data": data,
            },
        )
    @staticmethod
    def failure(data=None, message="Request failed", status_code=400):
        return JSONResponse(
            status_code=status_code,
            content={
                "success": False,
                "message": message,
                "data": None,
            },
        )
    @staticmethod
    def error(error=None, message="Internal server error", status_code=500):
        return JSONResponse(
            status_code=status_code,
            content={
                "success": False,
                "message": message,
                "error": error,
            },
        )