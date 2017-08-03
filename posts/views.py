from django.views import generic
from .models import Post
from django.views.generic.edit import CreateView,UpdateView,DeleteView

class IndexView(generic.ListView):
    template_name='posts/index.html'

    def get_queryset(self):
    	return Post.objects.all()

class DetailView(generic.DetailView):
	model=Post
	template_name='posts/detail.html'

class PostCreate(CreateView):
	model=Post
	fields=['title','content']
    
 

