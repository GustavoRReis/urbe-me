from django.urls import path
from listaprojetos.views import index

urlpatterns = [
    path("", index),
]
