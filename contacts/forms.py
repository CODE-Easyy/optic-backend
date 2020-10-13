# from django import forms
#
# from .models import Delivery, Contact, AboutUs
#
#
#
# class SubcatForm(forms.ModelForm):
#     title = forms.ChoiceField(label='',
#                             widget=forms.Select(
#                                 attrs={
#                                     'class': 'form-control ',
#                                     'placeholder': 'Выбор',
#                                 }
#                             ))
#     value = forms.CharField(label='Название',
#                             widget=forms.TextInput(
#                                 attrs={
#                                     'class': 'form-control',
#                                     'placeholder': 'Введите название субкатегории',
#                                 }
#                             ))
#     class Meta:
#         model = Delivery
#         fields = '__all__'