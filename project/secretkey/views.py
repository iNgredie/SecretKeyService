from rest_framework.generics import CreateAPIView, RetrieveAPIView

from .serializers import CreateSecretKeySerializer, RetrieveSecretKeySerializer
from .models import Secret


class CreateSecretKeyView(CreateAPIView):
    queryset = Secret.objects.all()
    serializer_class = CreateSecretKeySerializer


class RetrieveSecretKeyView(RetrieveAPIView):
    serializer_class = RetrieveSecretKeySerializer
    def get_queryset(self):
        return Secret.objects.filter(key=self.kwargs['pk'])