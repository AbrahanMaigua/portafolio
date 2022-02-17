from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here. 

class categoria(models.Model):
	name_categoria = models.CharField(max_length=40, verbose_name='categoria')
	def __str__(self):
		return self.name_categoria


class Post_Model(models.Model):
	titulo_principal = models.CharField(max_length=100, null=True, blank=True, verbose_name='Titulo Principal')
	resumen 		 = models.TextField(max_length=300, null=True, blank=True, verbose_name='Resumen')
	Categorias       = models.ManyToManyField(categoria)
	author           = models.ForeignKey(User, on_delete=models.CASCADE)
	text             = RichTextUploadingField()
	create_date      = models.DateTimeField(auto_now_add=True, verbose_name='Creacion')
	update_date      = models.DateTimeField(auto_now=True, verbose_name='Actualizacion')
	img	             = models.ImageField(verbose_name='' , upload_to='blog/media/', blank=True, null=True)

	def publish(self):
		self.save()

	def __str__(self):
		if self.titulo_principal is None:
			return str(self.titulo_principal)
		return self.titulo_principal
