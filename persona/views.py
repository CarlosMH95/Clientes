from django.shortcuts import render
from persona.models import Persona


def listarPersonas(request):
    personas=Persona.objects.all()
    data={
        "personas":personas
    }
    return render(request, 'persona/listartodos.html', data)

def detallesPersona(request, cedula):
    personas = Persona.objects.all()
    data = {}
    if cedula:
        try:
            persona= Persona.objects.get(cedula=cedula)
            data2 = {
                "p":persona
            }
        except:
            return render(request, 'persona/noexiste.html', data)
        return render(request, 'persona/listaruno.html', data2)

    return render(request, 'persona/noexiste.html', data)
