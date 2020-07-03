from django.contrib import admin
from django.urls import path
from . views import *


urlpatterns = [

    path('detail/<int:id>',district_detail, name='district-detail'),
    path('list',district_list, name='district-list'),
]
