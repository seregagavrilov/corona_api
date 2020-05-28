from rest_framework import serializers
from apps.country.models import Country, CountryStatistic


class CountryStatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryStatistic
        fields = (
            'confirmed',
            'deaths',
            'recovered',
            'last_updated'
        )
        read_only_fields = fields


class CountrySerializer(serializers.ModelSerializer):
    statistic = CountryStatisticSerializer(read_only=True, many=True)

    class Meta:
        model = Country
        fields = (
            'id',
            'name',
            'code',
            'statistic'
        )
        read_only_fields = fields


# class CountrySerializer(CountryListSerializer):
#     statistic = CountryStatisticSerializer(read_only=True)
#
#     class Meta:
#         model = Country
#         fields = CountryListSerializer.Meta.fields
#         read_only_fields = fields
