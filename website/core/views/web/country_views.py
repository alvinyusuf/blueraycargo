from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from core.models import Country

@login_required
def country_list(request):
    countries = Country.objects.all()
    return render(request, 'core/country_list.html', {'countries': countries})

@login_required
def country_add(request):
    if request.method == 'POST':
        name = request.POST['country_name']
        flag = request.POST['country_flag']
        currency = request.POST['country_currency']
        Country.objects.create(country_name=name, country_flag=flag, country_currency=currency)
        return redirect('country_list')
    return render(request, 'core/country_form.html')

@login_required
def country_edit(request, pk):
    country = get_object_or_404(Country, pk=pk)
    if request.method == 'POST':
        country.country_name = request.POST['country_name']
        country.country_flag = request.POST['country_flag']
        country.country_currency = request.POST['country_currency']
        country.save()
        return redirect('country_list')
    return render(request, 'core/country_form.html', {'country': country})

@login_required
def country_delete(request, pk):
    country = get_object_or_404(Country, pk=pk)
    country.delete()
    return redirect('country_list')
