from django_filters import rest_framework as filters

from apps.country.models import Country


class CountryFilter(filters.FilterSet):

    code = filters.CharFilter()
    # last_updated = filters.CharFilter(field_name='statistic__last_updated', method='get_statistic_by_date')
    last_updated = filters.CharFilter(field_name='statistic__last_updated')

    class Meta:
        model = Country
        fields = (
            'code',
            'last_updated'
        )

    def get_statistic_by_date(self, queryset, name, value):
        pass
