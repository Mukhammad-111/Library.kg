from django.shortcuts import render, redirect
from . import models, forms
from django.views import generic


class BookHouseListView(generic.ListView):
    template_name = 'parser_app/bookhouse_list.html'
    context_object_name = 'book_house'
    model = models.BookHouseModel

    def get_queryset(self):
        return models.BookHouseModel.objects.all().order_by('-id')


class RezkaListView(generic.ListView):
    template_name = 'parser_app/rezka_list.html'
    context_object_name = 'rezka'
    model = models.RezkaModel

    def get_queryset(self):
        return models.RezkaModel.objects.all().order_by('-id')


class MashinaListView(generic.ListView):
    template_name = 'parser_app/mashina_list.html'
    context_object_name = 'mashina'
    model = models.MashinaModel

    def get_queryset(self):
        return models.MashinaModel.objects.all().order_by('-id')


class ParsingFormView(generic.FormView):
    template_name = 'parser_app/parsing_form.html'
    form_class = forms.ParserForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parser_data()
            media_type = form.cleaned_data['media_type']
            if media_type == 'bookhouse.kg':
                return redirect('book_house_list')
            elif media_type == 'rezka.ag':
                return redirect('rezka_list')
            elif media_type == 'mashina.kg':
                return redirect('mashina_list')
        else:
            return super(ParsingFormView, self).post(request, *args, **kwargs)

