from django.contrib import admin
from .models import categoria, Post_Model

# Register your models here.
class AdminPost_Model(admin.ModelAdmin):
	list_display = "titulo_principal", "author", "img",
	readonly_fields = "create_date","update_date"


admin.site.register(categoria)	
admin.site.register(Post_Model, AdminPost_Model)
