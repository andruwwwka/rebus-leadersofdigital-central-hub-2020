from rest_framework import serializers, viewsets

from ..models import ObsceneWord


class ObsceneWordSerializer(serializers.ModelSerializer):

    class Meta:
        model = ObsceneWord
        fields = '__all__'


class ObsceneWordViewSet(viewsets.ModelViewSet):

    queryset = ObsceneWord.objects.all()
    serializer_class = ObsceneWordSerializer
