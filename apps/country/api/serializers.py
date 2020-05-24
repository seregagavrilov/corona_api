from rest_framework import serializers
from apps.country.models import Country, CountryStatistic


class CountryStatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryStatistic
        fields = (
            'confirmed',
            'deaths',
            'recovered',
            'created_at',
            'updated_at'
        )
        read_only_fields = fields


class CountryListSerializer(serializers.ModelSerializer):
    statistic = CountryStatisticSerializer(read_only=True)

    class Meta:
        model = Country
        fields = (
            'id',
            'name',
            'code',
            'statistic'
        )
        read_only_fields = fields


class CountrySerializer(CountryListSerializer):
    statistic = CountryStatisticSerializer(read_only=True)

    class Meta:
        model = Country
        fields = CountryListSerializer.Meta.fields
        read_only_fields = fields

    def create(self, validated_data):
        pass