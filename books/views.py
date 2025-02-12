from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from datetime import datetime
from . import models
from django.views.decorators.csrf import csrf_exempt
from .models import Review, BookModel


@csrf_exempt
def add_review(request, id):
    if request.method == "POST":
        try:
            book = BookModel.objects.get(id=id)
            review_text = request.POST.get("review_text", "").strip()
            grade = request.POST.get("grade", "3")

            if not review_text:
                return JsonResponse({"success": False, "error": "Комментарий не может быть пустым!"})

            new_review = Review.objects.create(
                choice_book=book,
                review_text=review_text,
                grade=grade
            )

            return JsonResponse({
                "success": True,
                "review_text": new_review.review_text,
                "grade": new_review.grade,
                "created_at": datetime.now().strftime("%Y-%m-%d %H:%M")
            })
        except BookModel.DoesNotExist:
            return JsonResponse({"success": False, "error": "Книга не найдена!"})
        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)})

    return JsonResponse({"success": False, "error": "Неверный метод запроса!"})

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