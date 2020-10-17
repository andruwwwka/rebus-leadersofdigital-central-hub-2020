from rest_framework import serializers, viewsets
from rest_framework.pagination import PageNumberPagination

from ..models import BanContent


class BanContentSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000


class BanContentSerializer(serializers.ModelSerializer):
    """Сериализатор для запрещенных ресурсов."""

    class Meta:
        model = BanContent
        fields = '__all__'


class BanContentViewSet(viewsets.ModelViewSet):
    """Представление для запрещенных ресурсов."""

    queryset = BanContent.objects.all()
    serializer_class = BanContentSerializer
    pagination_class = BanContentSetPagination
