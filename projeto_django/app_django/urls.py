from django.urls import path
from app_django.views import CadastroNovoUsuarioView

urlpatterns = [
    path('signup/', CadastroNovoUsuarioView.as_view(), name='signup'),
]
