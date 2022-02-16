from django.shortcuts import render, redirect
from django.forms import ModelForm
from .models import blog
from django.contrib import messages
# Create your views here.

class postModel(ModelForm):
	class meta:
		model=blog
		fields=['title', 'body']

def create(request):
	if request.method == "POST":
		form = postModel()
		if form.is_valid():
			post = form.save()
			messages.success(request, f"submited succesfully {post} ")
			return redirect("/")


	form = postModel()

	return render(request, "newarticule.html", {"form":form})