from django.forms import ModelForm
from django import forms



from products.models import (
    Brand,
    Material,
    Radius,
    OpticalPower,
    Volume
)


class BrandForm(ModelForm):
    value = forms.CharField(label='Значение', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Введите значение бренда...',
        }
    ))
    class Meta:
        model = Brand
        fields = '__all__'

class MaterialForm(ModelForm):
    value = forms.CharField(label='Значение', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Введите значение материала...',
        }
    ))
    class Meta:
        model = Material
        fields = '__all__'

class RadiusForm(ModelForm):
    value = forms.CharField(label='Значение', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Введите значение радиуса...',
        }
    ))
    class Meta:
        model = Radius
        fields = '__all__'

class OpticalPowerForm(ModelForm):
    value = forms.CharField(label='Значение', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Введите значение оптической силы...',
        }
    ))
    class Meta:
        model = OpticalPower
        fields = '__all__'

class VolumeForm(ModelForm):
    value = forms.CharField(label='Значение', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Введите значение объема...',
        }
    ))
    class Meta:
        model = Volume
        fields = '__all__'