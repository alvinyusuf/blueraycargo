from rest_framework.views import APIView
from rest_framework.response import Response
from core.services.rajaongkir_service import RajaOngkirService

class DestinationSearchAPI(APIView):
    def get(self, request):
        search = request.GET.get('search', '')
        destinations = RajaOngkirService.get_cities(search)
        return Response(destinations)
