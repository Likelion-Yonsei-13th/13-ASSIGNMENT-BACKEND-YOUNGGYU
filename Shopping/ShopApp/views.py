from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Shop

# Create your views here.
def shop(request):
    if request.user.is_authenticated:
        products = Shop.objects.filter(user=request.user)
    else:
        products = [] 
    return render(request, 'shop.html', {'products': products})

def detail(request, id):
    product = get_object_or_404(Shop, pk =id)
    return render(request, 'detail.html', {'product': product})

def new(request):
    return render(request, 'new.html')

def create(request):
    new_product = Shop()
    new_product.user=request.user
    new_product.product_name = request.POST['product_name']
    new_product.product_price = request.POST['product_price']
    new_product.product_explain = request.POST['product_explain']
    new_product.created_at = timezone.now()
    new_product.updated_at = timezone.now()
    new_product.save()

    return redirect('detail', new_product.id)

def edit(request, id):
    edit_product = Shop.objects.get(id=id)
    return render(request, 'edit.html',{'product': edit_product})

def update(request,id):
    update_product = Shop.objects.get(id=id)
    update_product.product_name = request.POST['product_name']
    update_product.product_price = request.POST['product_price']
    update_product.product_explain = request.POST['product_explain']
    update_product.updated_at = timezone.now()
    update_product.save()

    return redirect('detail', update_product.id)

def delete(request, id):
    delete_product = Shop.objects.get(id=id)
    delete_product.delete()
    return redirect('shop')
