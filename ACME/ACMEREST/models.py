from django.db import models

# Create your models here.
class Empresa(models.Model):
    nombre = models.CharField(max_length=100, primary_key=True)
    tipo = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

class Codes(models.Model):
	code = models.IntegerField()
	empresa = models.ForeignKey('Empresa', on_delete=models.CASCADE)
	valor = models.CharField(max_length=100)
	usado = models.CharField(max_length=2)

	def __str__(self):
		return "El código %s %s está usado" % (self.code, self.usado)