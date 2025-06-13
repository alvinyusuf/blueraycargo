from rest_framework.views import APIView
from rest_framework.response import Response

class DestinationSearchAPI(APIView):
    def get(self, request):
        search = request.GET.get('search', '')
        dummy_destinations = [
            {'id': 1, 'city': 'Jakarta'},
            {'id': 2, 'city': 'Bandung'},
            {'id': 3, 'city': 'Surabaya'}
        ]
        filtered = [d for d in dummy_destinations if search.lower() in d['city'].lower()]
        return Response(filtered)