from django import forms

from .models import Delivery, Contact, AboutUs

class DeliveryForm(forms.ModelForm):
    title = forms.CharField(label='Заголовок',
                            widget=forms.TextInput(
                                attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Введите заголовок',
                                }
                            ))
    description = forms.CharField(label='Описание',
                           widget=forms.Textarea(
                               attrs={
                                   'class': 'form-control',
                                   'placeholder': 'Введите описание'
                               }
                           ))
    class Meta:
        model = Delivery
        fields = '__all__'


class AboutUsForm(forms.ModelForm):
    text = forms.CharField(label='О нас',
                           widget=forms.Textarea(
                               attrs={
                                   'class': 'form-control',
                                   'placeholder': 'Введите описание о нас'
                               }
                           ))
    class Meta:
        model = AboutUs
        fields = '__all__'

class ContactForm(forms.ModelForm):
    email = forms.CharField(label='E-mail',
                            widget=forms.TextInput(
                                attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Введите почту',
                                }
                            ))
    phone = forms.CharField(label='Телефон',
                            widget=forms.TextInput(
                                attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Введите телефон',
                                }
                            ))
    whats_app_phone = forms.CharField(label='Whatsapp номер',
                            widget=forms.TextInput(
                                attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Введите номер Whatsapp',
                                }
                            ))

    vk_url = forms.URLField(label='VK ссылка',
                            widget=forms.URLInput(
                                attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Введите ссылку на ВК',
                                }
                            ))
    insta_url = forms.URLField(label='INSTAGRAM ссылка',
                            widget=forms.URLInput(
                                attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Введите ссылку на Instagram',
                                }
                            ))
    class Meta:
        model = Contact
        fields = '__all__'