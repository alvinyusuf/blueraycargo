from rest_framework.views import APIView
from rest_framework.response import Response
from core.models import Category

class CalculateFreightAPI(APIView):
    def post(self, request):
        category_id = request.data.get('category_id')
        destination_id = request.data.get('destination_id')
        weight = float(request.data.get('weight'))

        category = Category.objects.get(id=category_id)
        international_price = weight * category.price_per_kilo

        domestic_price = self.get_domestic_price(destination_id, weight)

        total_price = international_price + domestic_price

        response_data = {
            'origin': category.country.country_name,
            'destination': destination_id,
            'category_name': category.category_title,
            'international_price': international_price,
            'domestic_price': domestic_price,
            'total_price': total_price
        }
        return Response(response_data)

    def get_domestic_price(self, destination_id, weight):
        return weight * 10000
