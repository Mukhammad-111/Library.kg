from django.db import models
from django.contrib.auth.models import User


intern_salary = 20000
junior_salary = 50000
middle_salary = 120000
senior_salary = 350000


class CustomUser(User):
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
    phone_number = models.CharField(max_length=16, default='+996')
    age = models.IntegerField(default=18)
    gender = models.CharField(max_length=10, choices=GENDER)
    experience = models.IntegerField(default=0)
    direction = models.CharField(max_length=30, choices=DEV_CHOICES)
    salary = models.CharField(max_length=100)
    
    def save(self, *args, **kwargs):
        if self.experience < 0:
            self.salary = 'Опыт не может быть отрицательным!'
        elif self.experience == 0:
            self.salary = intern_salary
        elif 1 <= self.experience < 3:
            self.salary = junior_salary
        elif 3 <= self.experience < 6:
            self.salary = middle_salary
        elif self.experience >= 6:
            self.salary = senior_salary
            
        super().save(*args, **kwargs)    