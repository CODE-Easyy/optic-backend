from django.forms import ModelForm
from django import forms

from .models import Product

class GlassesForm(ModelForm):
    title = forms.CharField(label='Название',
                            widget=forms.TextInput(
                                attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Введите название Очков',
                                }
                            ))
    cat = forms.ChoiceField(label='Категория',
                            widget=forms.Select(
                                attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Введите описание Очков',
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
        fields = ('title', 'cat', 'subcat', 'price', 'img_1', 'img_2', 'img_3', 'is_discount', 'discount', 'is_leader', 'is_new', 'brand', 'material', 'sex', 'description')