
from django.urls import path
from Polls.views import index

urlpatterns = [
    path('', index, name="index"),
]
