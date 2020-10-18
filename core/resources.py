from rest_framework import views
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response

from .storage_backends import MediaStorage


class FileUploadView(views.APIView):
    """Представление для загрузки файлов."""

    parser_classes = [FileUploadParser]

    def put(self, request, format=None):
        file_obj = request.data['file']
        media_storage = MediaStorage()
        media_storage.save(file_obj.name, file_obj)
        file_url = media_storage.url(file_obj.name)
        return Response({'file_url': file_url}, status=204)
