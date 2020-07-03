from django.contrib import admin
from django.urls import path
from . views import *


urlpatterns = [

    path('detail/<int:district_id>',district_detail, name='district_detail'),
    path('list',district_list, name='district_list'),
]
