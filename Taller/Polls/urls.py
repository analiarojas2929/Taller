
from django.urls import path
from Polls.views import index, Contacto, Marcas, Productos, Reserva

urlpatterns = [
    path('', index, name="index"),
    path('contacto', Contacto, name="contacto"),
    path('marcas', Marcas, name="marcas"),
    path('productos', Productos, name="productos"),
]
