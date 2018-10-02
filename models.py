from django.db import models


class Estudiante(models.Model):
	nombre = models.CharField('Nombre del alumno', max_length=60)
	apellidoPaterno = models.CharField('Primer apellido', max_length=60)
	apellidoMaterno = models.CharField('Segundo apellido', max_length=60)
	matricula = models.IntegerField('Ingresa matricula', blank=False)
	fechaNacimiento = models.DateTimeField('Fecha de nacimiento', auto_now_add=False)
	def __str__(self):
		return str(self.nombre)+ " tiene la matricula " + str(self.matricula)


#from django.utils import timezone

#class Post(models.Model):
#	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
 #   title = models.CharField(max_length=60)	
#    text = models.TextField()
 #   created_date = models.DateTimeField(default=timezone.now)
  #  published_date = models.DateTimeField(blank=True, null=True)

   # def publish(self):
     #   self.published_date = timezone.now()
    #    self.save()

   # def __str__(self):
    #    return self.title

# Create your models here.
