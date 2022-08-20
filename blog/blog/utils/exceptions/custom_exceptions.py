
from blog.utils.error_response import ErrorResponse
from rest_framework import status
from rest_framework.views import exception_handler as func_exception_handler


def not_allowed(request, exception, *args, **kwargs):
    """
    405 error handler.
    """
    data = {
        'status': "405",
        'error': 'metodo não permitido'
    }

    return ErrorResponse(data, status=status.HTTP_405_METHOD_NOT_ALLOWED)


def exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = func_exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:
        data = response.data
        response.data = {
            "status": response.status_code,
            "detail": data.get("detail", data.get("messages", data))
        }

    return response
