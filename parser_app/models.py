from django.db import models


class BookHouseModel(models.Model):
    image = models.URLField()
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=250)
    price = models.CharField(max_length=250)

    def __str__(self):
        return self.title


class RezkaModel(models.Model):
    title = models.CharField(max_length=500)

    def __str__(self):
        return self.title


class MashinaModel(models.Model):
    title = models.CharField(max_length=200)
    price = models.CharField(max_length=200)

    def __str__(self):
        return self.title

