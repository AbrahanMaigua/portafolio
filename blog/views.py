from .crispy_one_forms import add_post
from django.shortcuts import HttpResponse, render, redirect , get_object_or_404
from .models import categoria, Post_Model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.

def indice(request):
	Post = Post_Model.objects.all()
	return render(
	request ,
	"all.html",
	{"Post_Tag":Post})

def Categoria(request, categoria_id):
	cont  = categoria.objects.get(id=categoria_id)
	posts = Post_Model.objects.filter(Categorias=categoria_id)
	return render(request ,"all.html", {"Post_Tag":posts, 'cont':cont})

def ahutor(request, user):
	cont  = '@%s' % User.objects.get(id=user)
	posts = Post_Model.objects.filter(author=user)
	return render(request ,"all.html", {"Post_Tag":posts, 'cont':cont})

	

def articulo(request, articulo_id):
	posts = Post_Model.objects.filter(id=articulo_id)
	#titulo = Post_Model.objects.get()
	return render(request ,"articulo.html", {"post":posts})
	
@login_required(login_url='/user/')
def AdminPost(request):
	titulo = "<h1>soy un titulo en Python </h1>"
	return render(request ,"adminPost.html", {"titulo":titulo})

@login_required(login_url='/user/')
def Crear_post(request):
	if request.method == "POST":
		form = add_post(request.POST)
		if form.is_valid():
			post 		= form.save(commit=False)
			post.author = request.user
			post.img    = request.POST.get('img')
			post.save() 
			return redirect('AdminPost')
	else:
		form 	= add_post()

	return render(request, 'new_post.html', {'form': form})

	# return HttpResponse("Lo sentimos este post pudo ser eleiminado")
	
@login_required(login_url='/user/')
def post_edit(request, pk):
	post = get_object_or_404(pk=pk)
	if request.method == "POST":
		form =  Post_Model(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.img = request.POST.get('img')
			post.save()
			return redirect('inicio')
		else:
			form =  Post_Model(instance=post)
	return render(request, 'new_post.html', {'form': form})
