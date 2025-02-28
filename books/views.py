from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from datetime import datetime


from . import models, forms
from django.views import generic
from django.urls import reverse
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.core.cache import cache


#create review

class SearchView(generic.ListView):
    template_name = 'book.html'
    context_object_name = 'book'

    def get_queryset(self):
        return models.BookModel.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context


class CreateReviewView(generic.CreateView):
    template_name = 'create_review.html'
    form_class = forms.CreateReviewForm

    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('book_detail', kwargs={'id': self.object.choice_book.id})

    
# def create_review_view(request):
#     if request.method == "POST":
#         form = forms.CreateReviewForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save(commit=False)
#             book_id = form.cleaned_data['choice_book'].id
#             form.save()
#             return redirect('book_detail', id=book_id)
#     else:
#         form = forms.CreateReviewForm()
#     return render(request, template_name='create_review.html', context={'form': form,})


@method_decorator(cache_page(60*15), name='dispatch')
class BookListView(generic.ListView):
    template_name = 'book.html'
    context_object_name = 'book'
    model = models.BookModel

    def get_queryset(self):
        books = cache.get('books')
        if not books:
            books = self.model.objects.all().order_by('-id')
            cache.set('books', books, 60*15)
        return books


# def book_list_view(request):
#     if request.method == "GET":
#         query = models.BookModel.objects.all().order_by('-id')
#         context_object_name = {
#             'book': query,
#         }
#         return render(request, template_name='book.html', context=context_object_name)


class BookDetailView(generic.DetailView):
    template_name = 'book_detail.html'
    context_object_name = 'book_id'

    def get_object(self, *args, **kwargs):
        book_id = self.kwargs.get('id')
        return get_object_or_404(models.BookModel, id=book_id)


# def book_detail_view(request, id):
#     if request.method == "GET":
#         query = get_object_or_404(models.BookModel, id=id)
#         context_object_name = {
#             'book_id': query,
#         }
#         return render(request, template_name='book_detail.html', context=context_object_name)





def about_me(request):
    if request.method == "GET":
        return HttpResponse("Я Искандар уулу Мухаммад, учусь в Политехе, мне 20")


def text_and_photo(request):
    if request.method == "GET":
        return HttpResponse('<h1>1970 Cadillac DeVille | Classic Auto Mall</h1>'
                            '<img src="https://bringatrailer.com/wp-content/uploads/2022/10/1970_cadillac_coupe-deville_1970_cadillac_coupe-deville_147fc4ea-46d6-4dbd-8882-7b74700e8798-ShriLl-72131-72132-scaled.jpg" />')


def system_time(request):
    if request.method == "GET":
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return HttpResponse(f"Текущее число и время: {current_time}")