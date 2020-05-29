from coronaapi.celery import app as celery
from apps.country.hendlers import StatisticLoader
from django.conf import settings
import requests


@celery.task(bind=True, max_retries=3)
def update_virus_data(self):
    try:
        res = requests.get(settings.VIRUS_API_URL, params={'timelines': True}, timeout=15)
    except requests.exceptions.ReadTimeout:
        self.retry(countdown=3**self.request.retries)
    if res.status_code == 200:
        loader = StatisticLoader(res.json())
        loader.load_statistic()

