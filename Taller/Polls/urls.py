
from django.urls import path
from Polls.views import index, Contacto, Marcas, Productos, Reserva

urlpatterns = [
    path('', index, name="index"),
]
