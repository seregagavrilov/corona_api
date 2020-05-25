release: python manage.py migrate
web: gunicorn coronaapi.wsgi
worker: celery -A coronaapi worker
beat: celery -A osla coronaapi -S django