from django import forms
from . import models, parser_book_house, parser_rezka, parser_mashina


class ParserForm(forms.Form):
    MEDIA_CHOICES = (
        ('bookhouse.kg', 'bookhouse.kg'),
        ('rezka.ag', 'rezka.ag'),
        ('mashina.kg', 'mashina.kg'),
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)

    class Meta:
        fields = [
            'media_type',
        ]

    def parser_data(self):
        if self.data['media_type'] == 'bookhouse.kg':
            book_house_books = parser_book_house.parsing_book_house()
            for i in book_house_books:
                models.BookHouseModel.objects.create(
                    image=i['image'],
                    title=i['title'],
                    author=i['author'],
                    price=i['price']
                )
        elif self.data['media_type'] == 'rezka.ag':
            rezka_films = parser_rezka.parsing_rezka()
            for i in rezka_films:
                models.RezkaModel.objects.create(**i)
        elif self.data['media_type'] == 'mashina.kg':
            mashina_cars = parser_mashina.mashina_parsing()
            for i in mashina_cars:
                models.MashinaModel.objects.create(
                    title=i['title'],
                    price=i['price'],
                )

