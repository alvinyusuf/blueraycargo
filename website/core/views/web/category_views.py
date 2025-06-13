from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from core.models import Country, Category

@login_required
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'core/category_list.html', {'categories': categories})

@login_required
def category_add(request):
    countries = Country.objects.all()
    if request.method == 'POST':
        country_id = request.POST['country']
        title = request.POST['category_title']
        price = request.POST['price_per_kilo']
        country = Country.objects.get(id=country_id)
        Category.objects.create(country=country, category_title=title, price_per_kilo=price)
        return redirect('category_list')
    return render(request, 'core/category_form.html', {'countries': countries})

@login_required
def category_edit(request, pk):
    category = get_object_or_404(Category, pk=pk)
    countries = Country.objects.all()
    if request.method == 'POST':
        country_id = request.POST['country']
        title = request.POST['category_title']
        price = request.POST['price_per_kilo']
        country = Country.objects.get(id=country_id)
        category.country = country
        category.category_title = title
        category.price_per_kilo = price
        category.save()
        return redirect('category_list')
    return render(request, 'core/category_form.html', {'category': category, 'countries': countries})

@login_required
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('category_list')