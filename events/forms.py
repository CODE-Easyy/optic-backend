from django import forms

from .models import Event
from products.models import Product



class EventForm(forms.ModelForm):
    title = forms.CharField(label='Заголовок',
                            required=False,
                            widget=forms.TextInput(
                                attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Введите заголовок',
                                }
                            ))
    img = forms.ImageField(label='Фото',
                             required=False,
                             widget=forms.FileInput(
                                 attrs={
                                     'class': 'py-3',
                                 }
                             ))
    img_slide = forms.ImageField(label='Фото на слайде',
                             required=False,
                             widget=forms.FileInput(
                                 attrs={
                                     'class': 'py-3',
                                 }
                             ))
    description = forms.CharField(label='Описание',
                            required=False,
                           widget=forms.Textarea(
                               attrs={
                                   'class': 'form-control',
                                   'placeholder': 'Введите описание'
                               }
                           ))
    to_date = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        label='Конец акции',
        required=False,
        widget=forms.DateTimeInput(attrs={
            'id': 'datetimepicker1',
            'class': 'form-control',
        })
    )
    from_date = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        label='Начало акции',
        required=False,
        widget=forms.DateTimeInput(attrs={
            'id': 'datetimepicker',
            'class': 'form-control',
        })
    )

    is_active = forms.BooleanField(
        label='Активный?',
        required=False,
        # widget=forms.CheckboxInput(
            
        # )
    )

    products = forms.ModelMultipleChoiceField(
        label='Продукты',
        queryset=Product.objects.all(),
        widget=forms.SelectMultiple(
            attrs={
                'class': 'form-control js-example-basic-multiple w-100',
                'multiple':'multiple'
            }
        ),
    )

    class Meta:
        model = Event
        fields = ('id', 'title', 'img', 'img_slide', 'from_date', 'to_date', 'is_active', 'description', 'products')