from django.forms import ModelForm
from django import forms

from .models import Product

class GlassesDetailForm(ModelForm):
    title = forms.CharField(label='Название',
                            widget=forms.TextInput(
                                attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Введите название Очков',
                                }
                            ))
    description = forms.CharField(label='Описание',
                            widget=forms.Textarea(
                                attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Введите описание Очков',
                                }
                            ))

    class Meta:
        model = Product
        fields = '__all__'