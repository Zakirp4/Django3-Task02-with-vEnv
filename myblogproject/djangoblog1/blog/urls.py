from django.contrib import admin
from django.urls import path
from . views import *


urlpatterns = [
    path('posts', post_list, name='post_list'),
    path('detail/<int:post_id>', post_detail, name='post_detail'),
]
