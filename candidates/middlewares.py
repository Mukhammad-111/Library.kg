from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseBadRequest


intern_salary = 20000
junior_salary = 50000
middle_salary = 120000
senior_salary = 350000


class ExperienceSalaryMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path == '/register/' and request.method == 'POST':
            try:
                experience = int(request.POST.get('experience'))
            except ValueError:
                return HttpResponseBadRequest('Неверное значение опыта')
            if experience < 0:
                return HttpResponseBadRequest('Опыт не может быть отрицательным!')
            elif experience == 0:
                request.salary = intern_salary
            elif 1 <= experience < 3:
                request.salary = junior_salary
            elif 3 <= experience < 6:
                request.salary = middle_salary
            elif experience >= 6:
                request.salary = senior_salary
        elif request.path == '/register/' and request.method == 'POST':
            setattr(request, 'salary', 'Извините зарплата не определена')