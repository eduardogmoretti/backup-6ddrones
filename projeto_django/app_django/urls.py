from django.contrib import admin
from django.urls import path, include
urlpatterns = [
path("admin/", admin.site.urls),
path('', include('exemplo_autenticacao_autorizacao_app.urls'))
]