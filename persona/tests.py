
from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase, RequestFactory
from persona.models import Persona
from persona.views import listarPersonas, detallesPersona

# Create your tests here.
def PruebaCajaBlanca(TestCase):
    def setup(self):
        persona = Persona()
        persona.nombre = "Carlos"
        persona.apellido = "Manosalvas"
        persona.cedula = "03254698745"
        persona.direccion = "Sauces 3"
        persona.ocupacion = "Estudiante"
        persona.save()
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='jacob', email='jacob@…', password='top_secret')
    def test_1(self):
        request = self.factory.get('/persona/listar')

        response = listarPersonas(request)
        self.assertEqual(response.status_code, 200)