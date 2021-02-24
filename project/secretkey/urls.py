from django.conf.urls import url
from django.urls import path

from .views import CreateSecretKeyView, RetrieveSecretKeyView

urlpatterns = [
    path('generate/', CreateSecretKeyView.as_view(), name='generate secret'),
    url('secrets/(?P<pk>[^/.]+)/', RetrieveSecretKeyView.as_view(), name='retrieve secret')
]