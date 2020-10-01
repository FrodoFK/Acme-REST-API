from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from . serializers import CodesSerializer, EmpresaSerializer
from . models import Codes, Empresa


# Create your views here.
class CodeViewSet (viewsets.ModelViewSet):
	queryset = Codes.objects.all()
	serializer_class = CodesSerializer

class EmpresaViewSet (viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
