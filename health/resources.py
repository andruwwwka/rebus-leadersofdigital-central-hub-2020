from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class Health(APIView):
    """Представления проверки работоспособности API."""
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        """Метод проверки работоспособности API."""
        return Response({'alive': True})
