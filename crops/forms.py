
from django import forms


from .models import *

class CropForm(forms.ModelForm):
    class Meta:
        model = Crop
        fields = '__all__'
        can_delete = True
        
class VarietyForm(forms.ModelForm):
    class Meta:
        model = Variety
        fields = '__all__'
        
        
class MarketForm(forms.ModelForm):
    class Meta:
        model = Market       
        fields = '__all__'  
        
