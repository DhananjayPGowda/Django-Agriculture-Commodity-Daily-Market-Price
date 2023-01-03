from django.contrib import admin
from .models import *
from django.forms import ModelForm

# Register your models here.  
class VarietyInline(admin.TabularInline):
  model = Variety

class CropAdmin(admin.ModelAdmin):
  inlines=[VarietyInline]



  

admin.site.register(Crop,CropAdmin)
admin.site.register(Market)
admin.site.register(Items)