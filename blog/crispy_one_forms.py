from django.utils.translation import gettext_lazy as _
from django.forms import ModelForm, TextInput
from .models import Post_Model
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class add_post(ModelForm):
	resumen = forms.CharField(max_length=200, 
		label='',
		widget=forms.Textarea(attrs={
			"placeholder":"resumen",
					"class":"form-control",
					'name':"place"}
					)
		)
	titulo_principal = forms.CharField(max_length=100, 
		label='',
		widget=TextInput(
				attrs={
					"placeholder":"Titulo principal ",
					"class":"form_input",
					'name':"place"})
		)
	text = forms.CharField(label="",widget=CKEditorUploadingWidget(attrs={
		"placeholder":"",
					"class":" form_input",
					'name':"place",
					"style":"display: inline-block;"

		})
	)


	class Meta:
		model  = Post_Model
		fields = ("titulo_principal",'resumen',"img","text", )
		 
		def  __str__(self) -> str:
			self.titulo_principal
