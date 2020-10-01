from rest_framework import serializers

from . models import Codes, Empresa

class CodesSerializer(serializers.ModelSerializer):
    #empresa = serializers.HyperlinkedRelatedField(read_only=True, view_name='empresa-detail')
    class Meta:
        model = Codes
        fields = ['code', 'empresa', 'valor', 'usado']
        

class EmpresaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
	    model = Empresa
	    fields = ['nombre', 'tipo']
