from django.conf.urls import url
from blog.views import greetings, aboutme, blog_list
urlpatterns = [
    url(r'^greetings/$', greetings, name='greetings'),
    url(r'^xyz/$', aboutme, name='aboutme'),
    url(r'^post-list/$', blog_list, name='blog_list'),
]