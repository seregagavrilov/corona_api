from django.urls import path, include
from .views import CountryViewSet

country_list_view = CountryViewSet.as_view({
    'get': 'list',
})

country_detail_view = CountryViewSet.as_view({
    'get': 'retrieve',
})

urlpatterns = [
    # path('get_countries/', get_countries_data, name='country_get_country'),
    path('', country_list_view, name='country_list_view'),
    path('<int:pk>/', country_detail_view, name='country_detail_view'),

]

