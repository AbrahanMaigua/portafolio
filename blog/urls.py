#my_saide_full URL Configuration
from django.urls import path, include
from .views import indice, Categoria,articulo, Crear_post, post_edit, AdminPost, ahutor


urlpatterns = [
   path('blog/', indice, name='blog'),
   path('blog/articulo/<int:articulo_id>/', articulo, name='articulo'),
   path('blog/ahutor/<str:user>', ahutor, name='ahutor'),
   path('blog/categoria/<int:categoria_id>/', Categoria, name='categoria'),
   path('blog/admin/', AdminPost, name='AdminPost'),
   path('blog/new-post', Crear_post, name='new_post'),
   path('blog/edit/<int:pk>/', post_edit, name='edit'),
   path('ckeditor/', include('ckeditor_uploader.urls')),



]