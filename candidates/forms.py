from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models


GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

DEV_CHOICES = (
    ('BACKEND', 'BACKEND'),
    ('FRONTEND', 'FRONTEND'),
    ('FULLSTACK', 'FULLSTACK'),
    ('MOBILE', 'MOBILE'),
    ('DEVOPS', 'DEVOPS'),
    ('DATA_SCIENCE', 'DATA_SCIENCE'),
    ('AI_ML', 'AI_ML'),
    ('GAME_DEV', 'GAME_DEV'),
    ('EMBEDDED', 'EMBEDDED'),
    ('CYBERSECURITY', 'CYBERSECURITY'),
    ('BLOCKCHAIN', 'BLOCKCHAIN')
)


class CustomRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Введите Email')
    phone = forms.CharField(required=True, label='Введите номер телефона')
    age = forms.IntegerField(required=True, label='Укажите возраст')
    gender = forms.ChoiceField(required=True, choices=GENDER, label='Укажите пол')
    direction = forms.ChoiceField(required=True, choices=DEV_CHOICES, label='Выберите направление разработки, в котором работайте')
    experience = forms.IntegerField(required=True, label="Укажите опыт работы в годах, если опыта нет, укажите 0")

    class Meta:
        model = models.CustomUser

        fields = (
            'username',
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'direction',
            'experience',
            'age',
            'gender',
            'phone',
        )

        def save(self, commit=True):
            applicant = self.save(commit=False)
            applicant.email = self.cleaned_data('email')
            applicant.phone = self.cleaned_data('phone')
            applicant.age = self.cleaned_data('age')
            applicant.gender = self.cleaned_data('gender')
            applicant.direction = self.cleaned_data('direction')
            applicant.experience = self.cleaned_data('experience')
            if commit:
                applicant.save()
            return applicant