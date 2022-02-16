from django.db import models

# Create your models here.
class categorias(models.Model):
	category = models.CharField(max_length=40, verbose_name="Cattegoria.")
	def __str__(self):
		return self.category
class home(models.Model):
	category = models.ManyToManyField(categorias)
	title    = models.CharField(max_length=40, verbose_name="Titulo", null=False, blank=False)
	content  = models.TextField(max_length=300, null=True, blank=True, verbose_name="Resumen.")
	create   = models.DateTimeField(auto_now_add=True, verbose_name='Creacion')
	update   = models.DateTimeField(auto_now=True, verbose_name='Actualizacion')

	#img      = models.ImageField(verbose_name='' , upload_to='blog/media/', blank=True, null=True)
	
	def publish(self):
		self.seve() 

	def __str__(self):
		return self.title
