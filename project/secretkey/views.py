from rest_framework.generics import CreateAPIView, RetrieveAPIView

from .serializers import CreateSecretKeySerializer
from .models import Secret


class CreateSecretKeyView(CreateAPIView):
    queryset = Secret.objects.all()
    serializer_class = CreateSecretKeySerializer


class RetrieveSecretKeyView(RetrieveAPIView):
    def get_queryset(self):
        return Secret.objects.filter(key=self.kwargs['pk'])