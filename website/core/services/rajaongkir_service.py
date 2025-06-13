import requests
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

class RajaOngkirService:
    BASE_URL = "https://rajaongkir.komerce.id/api/v1"
    API_KEY = settings.RAJAONGKIR_API_KEY

    @classmethod
    def get_cities(cls, search=None):
        url = f"{cls.BASE_URL}/destination/domestic-destination"
        headers = {
            "key": cls.API_KEY
        }
        params = {
            "search": search or ""
        }

        try:
            response = requests.get(url, headers=headers, params=params, timeout=10)
            response.raise_for_status()

            data = response.json()

            return data.get('data')

        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching cities from RajaOngkir: {str(e)}")
            return [
                {
                    'error': "Error fetching cities from RajaOngkir",
                    'details': str(e)
                }
            ]

        except Exception as e:
            logger.exception(f"Unhandled error in get_cities: {str(e)}")
            return [
                {
                    'error': 'Unhandled error',
                    'details': str(e)
                }
            ]
