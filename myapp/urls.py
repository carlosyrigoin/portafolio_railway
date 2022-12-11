from django.urls import path
from django.views.decorators.cache import cache_page
from . import views

urlpatterns = [
    path('', views.PortafolioView.as_view(), name="index"),
    path('administracion/', views.AdministracionView.as_view(), name="administracion"),
    path('portafolio/', views.PortafolioCreate.as_view(), name="portafolio"),
    path('delete/<int:id>', views.portafolioDelete, name="delete"),
]
