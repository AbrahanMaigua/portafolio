from django.shortcuts import render
from django.http import HttpResponse

from .models import home

# Create your views here.
def index(request):
	post = home.objects.all()
	
	print(post)
	return render(request, "index.html", {"post":post})