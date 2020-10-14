from django import forms


from .models import Order

class OrderForm(forms.ModelForm):
    address = forms.CharField(label='Адрес',
                            widget=forms.TextInput(
                                attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Введите название субкатегории',
                                }
                            ))
    comment = forms.CharField(label='Коммент',
                              widget=forms.Textarea(
                                  attrs={
                                      'class': 'form-control',
                                      'placeholder': 'Введите название субкатегории',
                                  }
                              ))
    email = forms.EmailField(label='E-mail',
                              widget=forms.EmailInput(
                                  attrs={
                                      'class': 'form-control',
                                      'placeholder': 'Введите название субкатегории',
                                  }
                              ))
    name = forms.CharField(label='Имя',
                              widget=forms.TextInput(
                                  attrs={
                                      'class': 'form-control',
                                      'placeholder': 'Введите название субкатегории',
                                  }
                              ))
    phone = forms.CharField(label='Телефон',
                              widget=forms.TextInput(
                                  attrs={
                                      'class': 'form-control',
                                      'placeholder': 'Введите название субкатегории',
                                  }
                              ))
    date = forms.DateTimeField(label="Дата заказа",
                               widget=forms.SelectDateWidget())
    class Meta:
        model = Order
        fields = ('name', 'address', 'email', 'phone', 'comment', 'date')