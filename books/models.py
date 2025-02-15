from django.db import models


class BookModel(models.Model):
    GENRE_CHOICES = (
        ('PSYCHOLOGY', 'PSYCHOLOGY'),
        ('NOVEL', 'NOVEL'),
        ('LITERARY', 'LITERARY'),
        ('FANTASY', 'FANTASY')
    )
    image = models.ImageField(upload_to='books/', verbose_name='загрузите фото')
    title = models.CharField(max_length=150, verbose_name='укажите название книги')
    description = models.TextField(verbose_name='укажите описание книг', blank=True)
    price = models.PositiveIntegerField(verbose_name='укажите цену книг', default=300)
    created_at = models.DateField(auto_now_add=True)
    genre = models.CharField(max_length=25, choices=GENRE_CHOICES, default='NOVEL',
                             verbose_name='выберите жанр')
    email = models.TextField(verbose_name='укажите почту')
    author = models.CharField(max_length=200, verbose_name="укажите автора", default='Исаков Иса')
    trailer = models.URLField(verbose_name='оставьте ссылку из YOUTUBE')


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'книгу'
        verbose_name_plural = 'книги'


class Review(models.Model):
    ESTIMATES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    choice_book = models.ForeignKey(BookModel, on_delete=models.CASCADE, related_name='books')
    created_at = models.DateField(auto_now_add=True)
    review_text = models.TextField(default="Отличная книга")
    grade = models.TextField(max_length=10, choices=ESTIMATES, default='3')

    def __str__(self):
        return f'{self.review_text} - {self.choice_book.title}'



