# Generated by Django 5.1.5 on 2025-02-25 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='age',
            field=models.IntegerField(default=18),
        ),
    ]
