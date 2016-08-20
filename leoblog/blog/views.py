from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render_to_response
from blog.models import Post

def greetings(request):
    return HttpResponse("GooD Morning")



def aboutme(request):
    name = "MicroPyramid"
    age = 5
    return render_to_response('aboutme.html', {
        'name': name,
        'age': age
    })

def blog_list(request):
    post_list = Post.objects.all()
    return render_to_response('postlist.html', {
        'post_list': post_list
    })