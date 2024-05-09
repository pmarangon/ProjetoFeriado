from django.urls import path
from . import views
app_name = 'core'
urlpatterns = [
    path('', views.feriado),
    path('cadastro', views.cadastro, name='cadastro')
]