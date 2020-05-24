from django.shortcuts import get_object_or_404

from apps.country.models import Country


class CountyMixin:

    def initial(self, request, *args, **kwargs):
        self.country = get_object_or_404(Country, id=self.kwargs.get('pk'))
        super().initial(request, *args, **kwargs)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['country'] = self.country
        return context