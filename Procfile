release: python manage.py migrate
web: gunicorn coronaapi.wsgi
worker: celery -A coronaapi worker
beat: celery -A coronaapi beat -S django