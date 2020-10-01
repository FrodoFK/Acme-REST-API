from django.shortcuts import render
from django import forms
from ACMEREST import models
from ACMEREST import serializers

codigos = models.Codes.objects.all()

class CodeForm(forms.Form):
    code = forms.IntegerField(label='Código a Verificar')

# Create your views here.
def index(request):
    return render(request, 'checks/index.html',{
        'form': CodeForm()
        })

def respuesta(request):
    if request.method == 'GET':
        form = CodeForm(request.GET)
        if form.is_valid():
            given_code = form.cleaned_data['code']
            for codigo in codigos:
                if given_code == codigo.code:
                    status = codigo.usado
                    return render(request, 'checks/respuesta.html',{
                        'respuesta': given_code,
                        'status' : status
                        })
                else:
                    status = "No existe"
    return render(request, 'checks/respuesta.html',
        {
        'respuesta': given_code,
        'status' : status
        })