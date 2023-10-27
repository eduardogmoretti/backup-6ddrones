from django.urls import path
from app_django.views import CadastroNovoUsuarioView
from app_django.views import CadastroNovoGrupoView

urlpatterns = [
    path('signup/', CadastroNovoUsuarioView.as_view(), name='signup'),
    path('group/', CadastroNovoGrupoView.as_view(), name='group'),
]
