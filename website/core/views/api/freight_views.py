from rest_framework.views import APIView
from rest_framework.response import Response
from core.models import Category, Country

class CalculateFreightAPI(APIView):
    def post(self, request):
        country_id = request.data.get('country_id')
        category_id = request.data.get('category_id')
        destination_id = request.data.get('destination_id')
        weight = request.data.get('weight')

        category = Category.objects.get(id=category_id)
        origin = Country.objects.get(id=country_id)
        destination = Country.objects.get(id=destination_id)

        international_price = weight * category.price_per_kilo

        domestic_price = self.get_domestic_price(destination_id, weight)

        total_price = international_price + domestic_price

        response_data = {
            'origin': origin.country_name,
            'destination': destination.country_name,
            'category_name': category.category_title,
            'international_price': international_price,
            'domestic_price': domestic_price,
            'total_price': total_price
        }
        return Response(response_data)

    def get_domestic_price(self, weight):
        return weight * 10000
