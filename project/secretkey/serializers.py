from rest_framework.serializers import ModelSerializer

from .models import Secret


class CreateSecretKeySerializer(ModelSerializer):
    class Meta:
        model = Secret
        fields = '__all__'