from django.urls import path
from .views.web.home_views import home
from .views.web.auth_views import (
    register_view, login_view, logout_view
)
from .views.web.country_views import (
    country_list, country_add, country_edit, country_delete
)
from .views.web.category_views import (
    category_list, category_add, category_edit, category_delete
)
from .views.api.search_views import (
    CountrySearchAPI, CategorySearchAPI
)
from .views.api.destination_views import DestinationSearchAPI
from .views.api.freight_views import CalculateFreightAPI

urlpatterns = [
    path('', home, name='home'),

    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    path('countries/', country_list, name='country_list'),
    path('countries/add/', country_add, name='country_add'),
    path('countries/edit/<int:pk>/', country_edit, name='country_edit'),
    path('countries/delete/<int:pk>/', country_delete, name='country_delete'),

    path('categories/', category_list, name='category_list'),
    path('categories/add/', category_add, name='category_add'),
    path('categories/edit/<int:pk>/', category_edit, name='category_edit'),
    path('categories/delete/<int:pk>/', category_delete, name='category_delete'),
]

# API URLs
urlpatterns += [
    path('api/countries/', CountrySearchAPI.as_view(), name='api_countries'),
    path('api/categories/', CategorySearchAPI.as_view(), name='api_categories'),
    path('api/destination/', DestinationSearchAPI.as_view(), name='api_destination'),
    path('api/calculate/', CalculateFreightAPI.as_view(), name='api_calculate'),
]
