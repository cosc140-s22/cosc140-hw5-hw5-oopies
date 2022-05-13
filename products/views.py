from django.shortcuts import render, get_object_or_404
from django.db.models import Prefetch
from .models import Product
from .forms import ProductFilterForm
from django.db.models import Prefetch


def index(request):
   Product.objects.prefetch_related (Prefetch('productimage_set'))  
   products = Product.objects.all().order_by('name')
   form = ProductFilterForm(request.GET)

#part 2: sort function
   sort= request.GET.get("sort")
   if sort:
      if sort=='age':
        sort="minimum_age_appropriate"
      products=Product.objects.all().order_by(sort)
      
#part 3: search function
   if form.is_valid():
      name_search = form.cleaned_data['name_search']
      max_search = form.cleaned_data['max_price']
      min_search = form.cleaned_data['min_price']
      if name_search:
        products = products.filter(name__icontains=name_search)
      if max_search:
        products=products.filter(price__lt=max_search)
      if min_search:
        products=products.filter(price__gt=min_search)
   context = {'products': products, 'form': form}
   return render(request, 'products/index.html', context)

def show(request, product_id):
    p = get_object_or_404(Product, pk=product_id)
    context = { 'product':p }
    return render(request, 'products/show.html', context)
    
