from rest_framework.response import Response


class ErrorResponse(Response):

    def __init__(self, data, status, *args, **kwargs):
        if isinstance(data, list):
            data = [item for item in data if len(item) > 0]
        new_data = {
            "status": status,
            "detail": data
        }
        super().__init__(data=new_data, status=status, *args, **kwargs)
