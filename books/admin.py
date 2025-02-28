from django.contrib import admin
from . import models
from django import forms
from PIL import Image


class ImageForm(forms.ModelForm):
    class Meta:
        model = models.BookModel
        fields = '__all__'

    def clean(self):
        super().clean()
        if self.cleaned_data.get('image'):
            try:
                img = Image.open(self.cleaned_data.get('image'))
                width, height = img.size
                print("ширина и высота", width, height)
                if width >= 1500 or height >= 900:
                    raise forms.ValidationError('Размер картинки слишком большой пож загрузите меньше 1500 на 900')
            except Exception as e:
                raise forms.ValidationError(f'Ошибка в отроботке {e}')


class ImageBookForm(admin.ModelAdmin):
    form = ImageForm


admin.site.register(models.BookModel, ImageBookForm)
admin.site.register(models.Review)

