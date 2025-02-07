from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from . import models


def book_list_view(request):
    if request.method == "GET":
        query = models.BookModel.objects.all().order_by('-id')
        context_object_name = {
            'book': query,
        }
        return render(request, template_name='book.html', context=context_object_name)


def book_detail_view(request, id):
    if request.method == "GET":
        query = get_object_or_404(models.BookModel, id=id)
        context_object_name = {
            'book_id': query,
        }
        return render(request, template_name='book_detail.html', context=context_object_name)





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