from django.shortcuts import render
from . import models


def all_clothes(request):
    if request.method == "GET":
        query = models.Clothes.objects.all().order_by('-id')
        context_object_name = {
            'all_clothes': query,
        }
        return render(request, template_name='clothes/all_clothes.html', context=context_object_name)


#детская одежда
def children_clothes(request):
    if request.method == "GET":
        query = models.Clothes.objects.filter(tags__name='Детская одежда').order_by('-id')
        context_object_name = {
            'children_clothes': query,
        }
        return render(request, template_name='clothes/children_clothes.html', context=context_object_name)


#подростковая одежда
def teenage_clothes(request):
    if request.method == "GET":
        query = models.Clothes.objects.filter(tags__name='Подростковая одежда').order_by('-id')
        context_object_name = {
            'teenage_clothes': query,
        }
        return render(request, template_name='clothes/teenage_clothes.html', context=context_object_name)


#Взрослая одежда
def adult_clothes(request):
    if request.method == "GET":
        query = models.Clothes.objects.filter(tags__name='Взрослая одежда').order_by('-id')
        context_object_name = {
            'adult_clothes': query,
        }
        return render(request, template_name='clothes/adult_clothes.html', context=context_object_name)