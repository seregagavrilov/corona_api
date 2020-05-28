from coronaapi.celery import app as celery
from apps.country.hendlers import StatisticLoader
from django.conf import settings
import requests


@celery.task(bind=True)
def update_virus_data(self):
    try:
        res = requests.get(settings.VIRUS_API_URL, params={'timelines': True}, timeout=10)
    except requests.exceptions.ReadTimeout:
        return None
    if res.status_code == 200:
        loader = StatisticLoader(res.json())
        loader.load_statistic()

