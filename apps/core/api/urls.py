from django.urls import include, path

urlpatterns = [
    path('countries/', include('apps.country.api.urls')),
]