from django.db import models
from books.models import BookModel


class MyOrdersModel(models.Model):
    choice_book = models.ForeignKey(BookModel, on_delete=models.CASCADE, verbose_name="Книга")
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата')
    address = models.TextField(verbose_name='укажите адрес доставки', null=True, blank=True)

    def __str__(self):
        return f'{self.choice_book} x {self.quantity}'

