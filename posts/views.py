from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Post

# Create your views here.

def index(request):
	all_posts=Post.objects.all()
	context={'all_posts':all_posts,}
	return render(request,'posts/index.html',context)

def detail(request, post_id):
	return HttpResponse("<h2>THIS IS THE DETAIL FOR "+str(post_id)+"</h2>")
