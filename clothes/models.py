from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Clothes(models.Model):
    title = models.CharField(max_length=30)
    price = models.PositiveIntegerField(default=400)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Одежду'
        verbose_name_plural = 'Одежды'