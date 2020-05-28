from django.contrib import admin

from apps.country.models import Country, CountryStatistic


class CountryStatisticInline(admin.TabularInline):
    model = CountryStatistic
    extra = 1


@admin.register(CountryStatistic)
class CountryStatisticAdmin(admin.ModelAdmin):
    list_display = (
        'country',
        'province',
        'confirmed',
        'deaths',
        'recovered',
        'last_updated'
    )
    list_display_links = ('country', )
    search_fields = ('country__name',)


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'code',
        'created_at',
        'updated_at'
    )
    list_display_links = ('name', )
    search_fields = ('name', 'code')
    inlines = (CountryStatisticInline,)
