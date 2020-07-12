from django.contrib import admin
from django.urls import path
from . views import *


urlpatterns = [
    path('posts', post_list, name='post_list'),
    path('test', test, name='test'),
    path('detail/<int:post_id>', post_detail, name='post_detail'),
    path('authors', author_list, name='authors'),
    path('authors/<author_name>', authors_post, name='author_post'),
]
