from django.shortcuts import render, redirect, get_object_or_404
from . import models, forms


def cart_list_view(request):
    if request.method == "GET":
        query = models.MyOrdersModel.objects.all().order_by("-id")
        context_object_name = {
            'cart_list': query,
        }
        return render(request, template_name='my_orders/cart_list.html', context=context_object_name)


def create_cart_view(request):
    if request.method == "POST":
        form = forms.MyOrdersForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('cart_list')
    else:
        form = forms.MyOrdersForm
    return render(request, template_name='my_orders/create_cart.html', context={'form': form})


def delete_cart_view(request, id):
    cart_id = get_object_or_404(models.MyOrdersModel, id=id)
    cart_id.delete()
    return redirect("cart_list")


def update_cart_view(request, id):
    cart_id = get_object_or_404(models.MyOrdersModel, id=id)
    if request.method == "POST":
        form = forms.MyOrdersForm(request.POST, instance=cart_id)
        if form.is_valid():
            form.save()
            return redirect("cart_list")
    else:
        form = forms.MyOrdersForm(instance=cart_id)
    return render(request, template_name='my_orders/update_cart.html', context={
        'form': form,
        'cart_id': cart_id,
    })


def order_cart_view(request, id):
    cart_id = get_object_or_404(models.MyOrdersModel, id=id)
    if request.method == "POST":
        form = forms.MyOrdersForm(request.POST, instance=cart_id)
        if form.is_valid():
            form.save()
            return redirect('cart_list')
    else:
        form = forms.MyOrdersForm(instance=cart_id)
    return render(request, template_name='my_orders/order_cart.html', context={
        'form': form,
        'cart_id': cart_id,
    })

