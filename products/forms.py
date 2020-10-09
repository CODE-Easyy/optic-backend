from django.forms import ModelForm
from django import forms

from .models import Product, SubCategory

class GlassesForm(ModelForm):
    CATEGORIES = [
        ('glasses', 'glasses'),
        ('frames', 'frames'),
        ('outlet', 'outlet'),
    ]
    SEXES = (
        ('man', 'man'),
        ('woman', 'woman'),
        ('unisex', 'unisex'),
        ('child', 'child'),
    )
    title = forms.CharField(label='Название',
                            widget=forms.TextInput(
                                attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Введите название Очков',
                                }
                            ))
    cat = forms.ChoiceField(label='Категория',
                                 choices=CATEGORIES,
                            widget=forms.Select(
                                attrs={
                                    'class': 'form-control col-md-6',
                                    'placeholder': 'Выбор',
                                }
                            ))
    subcat = forms.ModelChoiceField(label='Субкатегория',
                            queryset= SubCategory.objects.all(),
                            widget=forms.Select(
                                attrs={
                                    'class': 'form-control col-md-6',
                                    'placeholder': 'Выбор',
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