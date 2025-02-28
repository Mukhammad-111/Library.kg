from django import forms
from . import models


class MyOrdersForm(forms.ModelForm):
    class Meta:
        model = models.MyOrdersModel
        fields = '__all__'

