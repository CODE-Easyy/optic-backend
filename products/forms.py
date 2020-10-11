from django.forms import ModelForm
from django import forms

from .models import Product, SubCategory, Brand, Material, Radius, OpticalPower, Volume


class FramesForm(ModelForm):
    CATEGORIES = [
        ('glasses', 'Очки'),
        ('frames', 'Линзы'),
        ('outlet', 'outlet'),
    ]
    title = forms.CharField(label='Название',
                            widget=forms.TextInput(
                                attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Введите название Очков',
                                }
                            ))
    price = forms.IntegerField(label='Цена',
                               widget=forms.NumberInput(
                                   attrs={
                                       'class': 'form-control  ',
                                       'placeholder': 'Введите цену',
                                   }
                               ))
    img_1 = forms.ImageField(label='Фото №1',
                             required=False,
                             widget=forms.FileInput(
                                 attrs={
                                     'class': 'py-3',
                                     'placeholder': 'Введите название Очков',
                                 }
                             ))
    img_2 = forms.ImageField(label='Фото №2',
                             required=False,
                             widget=forms.FileInput(
                                 attrs={
                                     'class': 'py-3',
                                 }
                             ))
    img_3 = forms.ImageField(label='Фото №3',
                             required=False,
                             widget=forms.FileInput(
                                 attrs={
                                     'class': 'py-3',
                                 }
                             ))
    is_new = forms.BooleanField(label='Новый?',
                                required=False,
                                widget=forms.CheckboxInput(
                                    attrs={
                                        'class': 'py-4',
                                    }
                                ))
    is_discount = forms.BooleanField(label='Скидка?',
                                     required=False,
                                     widget=forms.CheckboxInput(
                                         attrs={
                                             'class': 'py-4',
                                         }
                                     ))
    is_leader = forms.BooleanField(label='ТОП?',
                                   required=False,
                                   widget=forms.CheckboxInput(
                                       attrs={
                                           'class': 'py-4',
                                       }
                                   ))
    discount = forms.IntegerField(label='Размер скидки',
                                  required=False,
                                  widget=forms.NumberInput(
                                      attrs={
                                          'class': 'form-control',
                                          'placeholder': 'Введите цену',
                                      }
                                  ))
    cat = forms.ChoiceField(label='Категория',
                            choices=CATEGORIES,
                            widget=forms.Select(
                                attrs={
                                    'class': 'form-control ',
                                    'placeholder': 'Выбор',
                                }
                            ))
    subcat = forms.ModelChoiceField(label='Субкатегория',
                                    required=False,
                                    queryset=SubCategory.objects.all().filter(),
                                    widget=forms.Select(
                                        attrs={
                                            'class': 'form-control',
                                            'placeholder': 'Выбор',
                                        }
                                    ))
    radius = forms.ModelChoiceField(label='Радиус',
                                   required=False,
                                   queryset=Radius.objects.all(),
                                   widget=forms.Select(
                                       attrs={
                                           'class': 'form-control',
                                           'placeholder': 'Выбор',
                                       }
                                   ))
    volume = forms.ModelChoiceField(label='Объем',
                                    required=False,
                                    queryset=Volume.objects.all(),
                                    widget=forms.Select(
                                        attrs={
                                            'class': 'form-control',
                                            'placeholder': 'Выбор',
                                        }
                                    ))
    opt_power = forms.ModelChoiceField(label='Оптическая сила',
                                      required=False,
                                      queryset=OpticalPower.objects.all(),
                                      widget=forms.Select(
                                          attrs={
                                              'class': 'form-control',
                                              'placeholder': 'Выбор',
                                          }
                                      ))
    description = forms.CharField(label='Описание',
                                  required=False,
                                  widget=forms.Textarea(
                                      attrs={
                                          'class': 'form-control',
                                          'placeholder': 'Введите описание Очков',
                                      }
                                  ))

    def __init__(self, *args, **kwargs):
        cat_val = kwargs.pop('cat', None)
        super(FramesForm, self).__init__(*args, **kwargs)

        if cat_val:
            self.fields['subcat'].queryset = SubCategory.objects.filter(cat=cat_val)

    class Meta:
        model = Product
        fields = (
        'is_discount', 'is_new', 'is_leader', 'title', 'cat', 'subcat', 'price', 'img_1', 'img_2', 'img_3', 'discount',
        'radius', 'opt_power', 'description', 'volume')


class GlassesForm(ModelForm):
    CATEGORIES = [
        ('glasses', 'Очки'),
        ('frames', 'Линзы'),
        ('outlet', 'outlet'),
    ]
    SEXES = (
        ('man', 'МУЖ'),
        ('woman', 'ЖЕН'),
        ('unisex', 'Унисекс'),
        ('child', 'Детский'),
    )
    title = forms.CharField(label='Название',
                            widget=forms.TextInput(
                                attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Введите название Очков',
                                }
                            ))
    price = forms.IntegerField(label='Цена',
                               widget=forms.NumberInput(
                                   attrs={
                                       'class': 'form-control  ',
                                       'placeholder': 'Введите цену',
                                   }
                               ))
    img_1 = forms.ImageField(label='Фото №1',
                             required=False,
                             widget=forms.FileInput(
                                 attrs={
                                     'class': 'py-3',
                                     'placeholder': 'Введите название Очков',
                                 }
                             ))
    img_2 = forms.ImageField(label='Фото №2',
                             required=False,
                             widget=forms.FileInput(
                                 attrs={
                                     'class': 'py-3',
                                 }
                             ))
    img_3 = forms.ImageField(label='Фото №3',
                             required=False,
                             widget=forms.FileInput(
                                 attrs={
                                     'class': 'py-3',
                                 }
                             ))
    is_new = forms.BooleanField(label='Новый?',
                                required=False,
                                widget=forms.CheckboxInput(
                                    attrs={
                                        'class': 'py-4',
                                    }
                                ))
    is_discount = forms.BooleanField(label='Скидка?',
                                     required=False,
                                     widget=forms.CheckboxInput(
                                         attrs={
                                             'class': 'py-4',
                                         }
                                     ))
    is_leader = forms.BooleanField(label='ТОП?',
                                   required=False,
                                   widget=forms.CheckboxInput(
                                       attrs={
                                           'class': 'py-4',
                                       }
                                   ))
    discount = forms.IntegerField(label='Размер скидки',
                                  required=False,
                                  widget=forms.NumberInput(
                                      attrs={
                                          'class': 'form-control',
                                          'placeholder': 'Введите цену',
                                      }
                                  ))
    cat = forms.ChoiceField(label='Категория',
                            choices=CATEGORIES,
                            widget=forms.Select(
                                attrs={
                                    'class': 'form-control ',
                                    'placeholder': 'Выбор',
                                }
                            ))
    sex = forms.ChoiceField(label='Пол',
                            required=False,
                            choices=SEXES,
                            widget=forms.Select(
                                attrs={
                                    'class': 'form-control ',
                                    'placeholder': 'Выбор',
                                }
                            ))
    subcat = forms.ModelChoiceField(label='Субкатегория',
                                    required=False,
                                    queryset=SubCategory.objects.all().filter(),
                                    widget=forms.Select(
                                        attrs={
                                            'class': 'form-control',
                                            'placeholder': 'Выбор',
                                        }
                                    ))
    brand = forms.ModelChoiceField(label='Бренд',
                                   required=False,
                                   queryset=Brand.objects.all(),
                                   widget=forms.Select(
                                       attrs={
                                           'class': 'form-control',
                                           'placeholder': 'Выбор',
                                       }
                                   ))
    material = forms.ModelChoiceField(label='Материал',
                                      required=False,
                                      queryset=Material.objects.all(),
                                      widget=forms.Select(
                                          attrs={
                                              'class': 'form-control',
                                              'placeholder': 'Выбор',
                                          }
                                      ))
    description = forms.CharField(label='Описание',
                                  required=False,
                                  widget=forms.Textarea(
                                      attrs={
                                          'class': 'form-control',
                                          'placeholder': 'Введите описание Очков',
                                      }
                                  ))

    def __init__(self, *args, **kwargs):
        cat_val = kwargs.pop('cat', None)
        super(GlassesForm, self).__init__(*args, **kwargs)

        if cat_val:
            self.fields['subcat'].queryset = SubCategory.objects.filter(cat=cat_val)

    class Meta:
        model = Product
        fields = (
        'is_discount', 'is_new', 'is_leader', 'title', 'cat', 'subcat', 'price', 'img_1', 'img_2', 'img_3', 'discount',
        'brand', 'material', 'sex', 'description')


class SubcatForm(ModelForm):
    CATEGORIES = [
        ('glasses', 'Очки'),
        ('frames', 'Линзы'),
        ('outlet', 'outlet'),
    ]
    cat = forms.ChoiceField(label='Категория',
                            choices=CATEGORIES,
                            widget=forms.Select(
                                attrs={
                                    'class': 'form-control ',
                                    'placeholder': 'Выбор',
                                }
                            ))
    value = forms.CharField(label='Название',
                            widget=forms.TextInput(
                                attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Введите название субкатегории',
                                }
                            ))
    class Meta:
        model = SubCategory
        fields = '__all__'