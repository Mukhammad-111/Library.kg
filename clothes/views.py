from django.shortcuts import render
from . import models
from django.views import generic
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.core.cache import cache


@method_decorator(cache_page(60*15), name='dispatch')
class ClothesListView(generic.ListView):
    template_name = 'clothes/all_clothes.html'
    context_object_name = 'all_clothes'
    model = models.Clothes

    def get_queryset(self):
        clothes = cache.get('clothes')
        if not clothes:
            clothes = self.model.objects.all().order_by('-id')
            cache.set('clothes', clothes, 60*15)
        return clothes


# def all_clothes(request):
#     if request.method == "GET":
#         query = models.Clothes.objects.all().order_by('-id')
#         context_object_name = {
#             'all_clothes': query,
#         }
#         return render(request, template_name='clothes/all_clothes.html', context=context_object_name)


#детская одежда

@method_decorator(cache_page(60*15), name='dispatch')
class ChildrenClothesView(generic.ListView):
    template_name = 'clothes/children_clothes.html'
    context_object_name = 'children_clothes'
    model = models.Clothes

    def get_queryset(self):
        children = cache.get('children')
        if not children:
            children = self.model.objects.all().order_by('-id')
            cache.set('children', children, 60*15)
        return children

# def children_clothes(request):
#     if request.method == "GET":
#         query = models.Clothes.objects.filter(tags__name='Детская одежда').order_by('-id')
#         context_object_name = {
#             'children_clothes': query,
#         }
#         return render(request, template_name='clothes/children_clothes.html', context=context_object_name)


#подростковая одежда

@method_decorator(cache_page(60*15), name='dispatch')
class TeenageClothesView(generic.ListView):
    template_name = 'clothes/teenage_clothes.html'
    context_object_name = 'teenage_clothes'
    model = models.Clothes

    def get_queryset(self):
        teenagers = cache.get('teenagers')
        if not teenagers:
            teenagers = self.model.objects.all().order_by('-id')
            cache.set('teenagers', teenagers, 60*15)
        return teenagers


# def teenage_clothes(request):
#     if request.method == "GET":
#         query = models.Clothes.objects.filter(tags__name='Подростковая одежда').order_by('-id')
#         context_object_name = {
#             'teenage_clothes': query,
#         }
#         return render(request, template_name='clothes/teenage_clothes.html', context=context_object_name)


# #Взрослая одежда
@method_decorator(cache_page(60*15), name='dispatch')
class AdultClothesView(generic.ListView):
    template_name = 'clothes/adult_clothes.html'
    context_object_name = 'adult_clothes'
    model = models.Clothes

    def get_queryset(self):
        adults = cache.get('adults')
        if not adults:
            adults = self.model.objects.all().order_by('-id')
            cache.set('adults', adults, 60*15)
        return adults


# def adult_clothes(request):
#     if request.method == "GET":
#         query = models.Clothes.objects.filter(tags__name='Взрослая одежда').order_by('-id')
#         context_object_name = {
#             'adult_clothes': query,
#         }
#         return render(request, template_name='clothes/adult_clothes.html', context=context_object_name)