from django.urls import path, include
from .views import CountryStatisticViewSet, get_countries_data

country_list_view = CountryStatisticViewSet.as_view({
    'get': 'list',
})

country_detail_view = CountryStatisticViewSet.as_view({
    'get': 'retrieve',
})

urlpatterns = [
    path('get_countries/', get_countries_data, name='country_get_country'),
    path('', country_list_view, name='country_list_view'),
    path('<int:pk>/', country_detail_view, name='country_detail_view'),

]

