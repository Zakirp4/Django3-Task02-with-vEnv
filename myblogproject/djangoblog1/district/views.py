from django.shortcuts import render
from .models import District

def district_list(request):
    districts = District.objects.all()
    context = {
        'district_list': districts
    }

    return render(request,'district/district_list.html', context)

def district_detail(request, district_id):
    district = District.objects.get(id=district_id)
    context = {
        'post': district
    }
    return render(request, 'district/district_detail.html', context)

