from django.contrib import admin
from django.urls import path
from . views import *


urlpatterns = [

    path('detail/<int:roll>',student_detail, name='student_detail'),
    path('list',student_list, name='student_list'),
]
