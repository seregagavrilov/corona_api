from apps.country.models import Country, CountryStatistic
from collections import OrderedDict
import datetime
import pytz

utc = pytz.UTC


def create_country_latest_statistic():
    pass


def create_current_timeline_data(amount_type, current_timeline_data, current_country):
    current_timeline_data = current_timeline_data.get('timeline')
    for time, amount in current_timeline_data.items():
        statistic, created = CountryStatistic.objects.update_or_create(
            country=current_country,
            last_updated=time,
            defaults={amount_type: amount}
        )


class StatisticLoader:
    def __init__(self, data):
        self.locations = data.get('locations')

        self.current_country_code = ''
        self.current_country_name = ''
        self.current_country = None

        self.current_province = ''
        self.current_location = None
        self.current_timelines = None

        self.indicators = ('confirmed', 'deaths', 'recovered')

    def set_current_data(self, current_location):
        self.current_province = current_location.get('province')
        self.current_country_code = current_location.get('country_code')
        self.current_country_name = current_location.get('country')
        self.current_timelines = current_location.get('timelines')
        self.current_location = current_location

    def create_country_statistic(self):
        if self.current_country and self.current_timelines:
            self.init_country_statistic()

    def load_statistic(self):
        for location in self.locations:
            self.set_current_data(location)
            self.create_country()
            self.create_country_statistic()

    def create_country(self):
        if self.current_country_code and self.current_country_name:
            self.current_country, created = Country.objects.get_or_create(
                code=self.current_country_code,
                defaults={'name': self.current_country_name},
            )

    def create_current_timeline_data(self, current_indicator, current_timeline):
        current_timeline = current_timeline.get('timeline')
        for time, amount in current_timeline.items():
            CountryStatistic.objects.update_or_create(
                country=self.current_country,
                last_updated=time,
                province=self.current_province,
                defaults={current_indicator: amount}
            )

    def init_country_statistic(self):
        country_statistic = CountryStatistic.objects.filter(
            country=self.current_country,
            province=self.current_province
        )
        if not country_statistic:
            for indicator in self.indicators:
                self.create_current_timeline_data(indicator, self.current_timelines.get(indicator))
        else:
            self.update_country_statistic(country_statistic, self.current_timelines)

    def get_last_confirmed_date_in_data(self):
        current_confirmed_timelines = self.current_timelines.get('confirmed')
        timelines = current_confirmed_timelines.get('timeline')
        ordered_data = OrderedDict(timelines)
        if ordered_data:
            return datetime.datetime.strptime(list(ordered_data.keys())[-1], '%Y-%m-%dT%H:%M:%SZ')

    def get_latest_loaded_data(self, history, start_date, end_date):
        string_start_date = datetime.datetime.strftime(start_date, '%Y-%m-%d %H:%M:%S')
        string_end_date = datetime.datetime.strftime(end_date, '%Y-%m-%dT%H:%M:%SZ')
        timelines = history.get('timeline')
        for date, entry in timelines.items():
            if start_date < string_start_date < string_end_date:
                yield date, entry

    def update_timeline_data(self, current_indicator, current_amount, current_time):
        CountryStatistic.objects.update_or_create(
            country=self.current_country,
            province=self.current_province,
            last_updated=current_time,
            defaults={current_indicator: current_amount}
        )

    def update_country_statistic(self, current_country_statistic, current_timeline):
        latest_statistic_date = current_country_statistic.latest('last_updated').last_updated
        latest_confirmed_data = self.get_last_confirmed_date_in_data()
        if latest_confirmed_data > latest_statistic_date:
            for indicator in self.indicators:
                for time, amount in self.get_latest_loaded_data(
                        current_timeline.get(indicator), latest_statistic_date, latest_confirmed_data):
                    self.update_timeline_data(indicator, amount, time)


def create_country_statistic(data):
    locations = data.get('locations')
    for location in locations:
        code = location.get('country_code')
        if code:
            name = location.get('country')
            last_updated = location.get('last_updated')
            country, created = Country.objects.get_or_create(
                code=code,
                defaults={'name': name},
            )

            timelines = location.get('timelines')
            if not timelines:
                return None
            current_country_statistic = CountryStatistic.objects.filter(country=country)
            if current_country_statistic:

                latest_statistic = current_country_statistic.latest('last_updated')
                current_confirmed = timelines.get('confirmed')
                current_confirmed_timeline = current_confirmed.get('timeline')

                ordd = OrderedDict(current_confirmed_timeline)
                # currrent_datetime_last = utc.localize(
                #     datetime.datetime.strptime(list(ordd.keys())[-1], '%Y-%m-%dT%H:%M:%SZ')
                # )
                currrent_datetime_last = datetime.datetime.strptime(list(ordd.keys())[-1], '%Y-%m-%dT%H:%M:%SZ')


                # confirmed = current_confirmed.get('latest')
                # deaths = timelines.get('deaths').get('latest')
                # recovered = timelines.get('recovered').get('latest')

                if currrent_datetime_last > latest_statistic.last_updated:
                    for key in ['confirmed', 'deaths', 'recovered']:
                        string_last_upd = datetime.datetime.strftime(latest_statistic.last_updated, '%Y-%m-%d %H:%M:%S')
                        string_last_cdt = datetime.datetime.strftime(currrent_datetime_last, '%Y-%m-%dT%H:%M:%SZ')
                        for time, amount in get_records(timelines.get(key), string_last_upd, string_last_cdt):
                            CountryStatistic.objects.update_or_create(
                                country=country,
                                last_updated=time,
                                defaults={key: amount}
                            )
            else:
                for key in ['confirmed', 'deaths', 'recovered']:
                    create_current_timeline_data(key, timelines.get(key), country)
