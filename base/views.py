from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render

from authentication.decorators import have_access
from .forms import (
    WebsiteForm,
    ProductForm
)
from django.contrib.auth.decorators import login_required
from .models import (
    Website,
    Product

)
from django.core.paginator import Paginator

from django.urls import reverse

def HomeView(request):
    template = "home.html"
    context = {

    }

    return render(request, template, context)

@login_required
@have_access
def CreateWebsite(request):
    template = "create-website.html"
    form = WebsiteForm()
    if request.method == "POST":
        form = WebsiteForm(request.POST, request.FILES)
        form.instance.user = request.user
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {
       'form' : form,
    }

    return render(request, template, context)

@login_required
def Dashboard(request):
    template = "dashboard.html"
    websites = Website.objects.filter(user=request.user)
    products = Product.objects.filter(user=request.user)[:5]
    context = {
       'websites' : websites,
       'products' : products,
       'length' : len(products),
    }

    return render(request, template, context)

def WebsiteInfo(request, pk):
    template = "website-info.html"
    website = Website.objects.get(id=pk)
    products = website.products.all().filter(is_active=True)
    p = Paginator(products.order_by('-id'), 10)
    page = request.GET.get('page')
    stuff = p.get_page(page)
    nums = "a" * stuff.paginator.num_pages
    context = {
        'website' : website,
        'products' : stuff,
        'nums' : nums,
    }

    return render(request, template, context)

@login_required
def AddtoWebsite(request, website_id, product_id):
        website = Website.objects.get(id=website_id)
        product = Product.objects.get(id=product_id)
        if website.user == request.user and product.user == request.user:
            if request.method == "POST":
                website.products.add(product)
                return HttpResponseRedirect(reverse('update', args=[str(website.id)]))
        else:
            return redirect('/')

@login_required
def RemoveFromWebsite(request, website_id, product_id):
        website = Website.objects.get(id=website_id)
        product = Product.objects.get(id=product_id)
        if website.user == request.user and product.user == request.user:
            if request.method == "POST":
                website.products.remove(product)
                return HttpResponseRedirect(reverse('update', args=[str(website.id)]))
        else:
            return redirect('/')

@login_required
def UpdateView(request, pk):
    website = Website.objects.get(id=pk)
    if request.user == website.user:
       template = "update-website.html"
       form = WebsiteForm(instance=website)
       products = Product.objects.filter(user=request.user)
       website_products = website.products.all()
       current_products = []
       for product in website_products:
           current_products.append(product.id)
       if request.method == "POST":
           form = WebsiteForm(request.POST, request.FILES, instance=website)
           if form.is_valid():
               form.save()
               return redirect(request.path)
       context = {
         'form' : form,
         'products' : products.filter(is_active=True),
         'current' : current_products,
         'website' : website,
       }
       return render(request, template, context)
    else:
        return redirect('home')

@login_required
@have_access
def CreateProductView(request):
    template = "products/create.html"
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        form.instance.user = request.user
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {
      'form' : form,
    }

    return render(request, template, context)

@login_required
def UpdateProductView(request, pk):
    product = Product.objects.get(id=pk)
    if product.user == request.user:
        template = "products/update.html"
        form = ProductForm(instance=product)
        if request.method == "POST":
            form = ProductForm(request.POST, request.FILES, instance=product)
            if form.is_valid():
                form.save()
                return redirect('dashboard')
        context = {
         'product' : product,
         'form' : form,
        }

        return render(request, template, context)
    else:
        return redirect('/')

@login_required
def DeleteProductView(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == "POST":
        if product.user == request.user:
            product.delete()
            return redirect('dashboard')
        else:
            return redirect('/')

@login_required
def DeleteWebsiteView(request, pk):
    website = Website.objects.get(id=pk)
    if request.method == "POST":
        if website.user == request.user:
            website.delete()
            return redirect('dashboard')
        else:
            return redirect('/')

@login_required
def ProductInfo(request, pk):
    product = Product.objects.get(id=pk)
    if product.user == request.user:
        template = "products/info.html"
        context = {
            'product' : product,
        }

        return render(request, template, context)
    else:
        return redirect('/')