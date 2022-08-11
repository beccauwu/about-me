from datetime import datetime
from django.views import generic
from .models import Post

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

from django.shortcuts import render
from django.http import HttpResponse
from .forms import BlogForm
from .models import BlogPost
from django.contrib import messages
# Create your views here.
def usblog(request):
    blogs = BlogPost.objects.all()
    return render(request, 'blog.html', {'blogs' : blogs})
  
def blog_detail(request):
    form = BlogForm(request.POST or None, request.FILES or None)
    if request.method =='POST':
          
        if form.is_valid():
              
            obj = form.save(commit = False)
            obj.user = request.user
            obj.date = datetime.now()
            obj.save()
            form = BlogForm()
            messages.success(request, "Successfully created")
          
  
    return render(request, 'blog_upload.html', {'form':form})
