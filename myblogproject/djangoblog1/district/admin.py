from django.contrib import admin
from .models import District

class DistrictListAdmin(admin.ModelAdmin):
    list_display = ['name', 'description','numberofthana','thananame','created_at']
    list_editable = ['description']

admin.site.register(District, DistrictListAdmin)


