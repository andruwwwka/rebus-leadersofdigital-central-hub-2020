from rest_framework import views
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response


class FileUploadView(views.APIView):
    """Представление для загрузки файлов."""

    parser_classes = [FileUploadParser]

    def post(self, request, format=None):
        file_obj = request.data['file']
        a = 1
        return Response(status=204)
