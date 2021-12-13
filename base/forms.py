from .models import (
    Website,
    Product
)
from django import forms

class WebsiteForm(forms.ModelForm):
    class Meta:
        model = Website
        fields = ('name', 'image1', 'image2', 'image3')

        widgets = {
            'name' : forms.TextInput(attrs={'class' : 'form-control'}),
            # 'image1' : forms.FileInput(attrs={'class' : 'form-control'}),
            # 'image2' : forms.FileInput(attrs={'class' : 'form-control'}),
            # 'image3' : forms.FileInput(attrs={'class' : 'form-control'}),
        }

class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = ('name', 'link', 'is_active', 'description', 'image')

        labels = {
            'is_active' : "Active"
        }

        widgets = {
            'name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'link' : forms.URLInput(attrs={'class' : 'form-control'}),
            'description' : forms.Textarea(attrs={'class' : 'form-control'}),

        }
