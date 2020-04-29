from django.shortcuts import render
from .models import Blog
# Create your views here.
blogs=Blog.objects.all()
#print (blogs.title)
def allblogs(request):
    return render(request, 'blog/allblogs.html',{'blogs':blogs})
