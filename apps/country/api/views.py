from django.http import JsonResponse
from django.shortcuts import redirect, reverse
from django.shortcuts import render
import requests
from rest_framework import viewsets
from rest_framework.status import HTTP_200_OK

from apps.country.api.filters import CountryFilter
from apps.country.mixins import CountyMixin
from rest_framework.response import Response
from apps.country.models import Country
from apps.country.api.serializers import CountrySerializer
from apps.country.tasks import update_virus_data



def get_countries_data(r):
    update_virus_data()
    return Response(status=HTTP_200_OK)


class CountryStatisticViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    filterset_class = CountryFilter
    # ordering = ('-created_at',)
    # lookup_url_kwarg = 'country_id'

    # def get_serializer_class(self):
    #     if self.action == 'list':
    #         return CountryListSerializer
    #     return CountrySerializer
    # def get_queryset(self):
    #     q = super().get_queryset()
    #     return q.filter(country=self.country)




# class BuildingProductFileModerateViewSet(BuildingMixin, viewsets.ModelViewSet):
#     authentication_classes = (TokenAuthentication, IsPurchaserOnly, IsOwnerBuilding)
#     permission_classes = (IsAuthenticated, )
#     queryset = ModerateBuildingUploadFile.objects
#     serializer_class = BuildingProductImportFileModerateSerializer
#
#     def get_queryset(self):
#         q = super().get_queryset()
#         return q.filter(building=self.building)