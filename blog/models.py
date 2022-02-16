from django.db import models
from django_editorjs import EditorJsField as editorjs
# Create your models here.

class blog(models.Model):
	title = models.CharField(max_length=255, verbose_name="Titulo")
	body = editorjs()

	def __str__(self):
		return self.title