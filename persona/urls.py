from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include, url
from persona.views import listarPersonas, detallesPersona

urlpatterns = [
    url(r'^listar/', listarPersonas, name='todos'),
    url(r'^(?P<cedula>[0-9]+)/', detallesPersona, name='uno'),
]
