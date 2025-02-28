from django.shortcuts import render, redirect, get_object_or_404
from . import models, forms
from django.views import generic
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.core.cache import cache


# @method_decorator(cache_page(60*15), name='dispatch')
class CartListView(generic.ListView):
    template_name = 'my_orders/cart_list.html'
    context_object_name = 'cart_list'
    model = models.MyOrdersModel

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')
        # orders = cache.get('orders')
        # if not orders:
        #     orders = self.model.objects.all().order_by('-id')
        #     cache.set('orders', orders, 60*15)
        # return orders


# def cart_list_view(request):
#     if request.method == "GET":
#         query = models.MyOrdersModel.objects.all().order_by("-id")
#         context_object_name = {
#             'cart_list': query,
#         }
#         return render(request, template_name='my_orders/cart_list.html', context=context_object_name)


class CreateCartView(generic.CreateView):
    template_name = 'my_orders/create_cart.html'
    form_class = forms.MyOrdersForm
    success_url = '/cart_list/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateCartView, self).form_valid(form=form)


# def create_cart_view(request):
#     if request.method == "POST":
#         form = forms.MyOrdersForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('cart_list')
#     else:
#         form = forms.MyOrdersForm
#     return render(request, template_name='my_orders/create_cart.html', context={'form': form})


class DeleteCartView(generic.DeleteView):
    template_name = 'my_orders/confirm_delete.html'
    success_url = '/cart_list/'

    def get_object(self, *args, **kwargs):
        cart_id = self.kwargs.get('id')
        return get_object_or_404(models.MyOrdersModel, id=cart_id)


# def delete_cart_view(request, id):
#     cart_id = get_object_or_404(models.MyOrdersModel, id=id)
#     cart_id.delete()
#     return redirect("cart_list")


class UpdateCartView(generic.UpdateView):
    template_name = 'my_orders/update_cart.html'
    form_class = forms.MyOrdersForm
    success_url = '/cart_list/'

    def get_object(self, *args, **kwargs):
        cart_id = self.kwargs.get('id')
        return get_object_or_404(models.MyOrdersModel, id=cart_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(UpdateCartView, self).form_valid(form=form)


# def update_cart_view(request, id):
#     cart_id = get_object_or_404(models.MyOrdersModel, id=id)
#     if request.method == "POST":
#         form = forms.MyOrdersForm(request.POST, instance=cart_id)
#         if form.is_valid():
#             form.save()
#             return redirect("cart_list")
#     else:
#         form = forms.MyOrdersForm(instance=cart_id)
#     return render(request, template_name='my_orders/update_cart.html', context={
#         'form': form,
#         'cart_id': cart_id,
#     })


class OrderCartView(generic.UpdateView):
    template_name = 'my_orders/order_cart.html'
    form_class = forms.MyOrdersForm
    success_url = '/cart_list/'

    def get_object(self, *args, **kwargs):
        cart_id = self.kwargs.get('id')
        return get_object_or_404(models.MyOrdersModel, id=cart_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = self.get_object()
        context['cart'] = cart
        return context

    def form_valid(self, form):
        cart = self.get_object()
        form.instance = cart
        form.save()
        return super().form_valid(form)


# def order_cart_view(request, id):
#     cart_id = get_object_or_404(models.MyOrdersModel, id=id)
#     if request.method == "POST":
#         form = forms.MyOrdersForm(request.POST, instance=cart_id)
#         if form.is_valid():
#             form.save()
#             return redirect('cart_list')
#     else:
#         form = forms.MyOrdersForm(instance=cart_id)
#     return render(request, template_name='my_orders/order_cart.html', context={
#         'form': form,
#         'cart_id': cart_id,
#     })

