from rest_framework.views import APIView
from rest_framework.response import Response
from core.models import Country, Category

class CountrySearchAPI(APIView):
    def get(self, request):
        search = request.GET.get('search')

        if search:
            countries = Country.objects.filter(country_name__icontains=search)
        else:
            countries = Country.objects.all()

        data = [
            {
                'id': c.id,
                'country_name': c.country_name,
                'country_currency': c.country_currency
            }
            for c in countries
        ]
        return Response(data)

class CategorySearchAPI(APIView):
    def get(self, request):
        country_id = request.GET.get('country_id')
        search = request.GET.get('search', '')

        categories = Category.objects.all()

        if country_id:
            categories = categories.filter(country_id=country_id)

        if search:
            categories = categories.filter(category_title__icontains=search)

        data = [
            {
                'id': cat.id,
                'country_id': cat.country_id,
                'category_title': cat.category_title,
                'price_per_kilo': cat.price_per_kilo
            }
            for cat in categories
        ]
        return Response(data)
