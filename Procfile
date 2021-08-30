release: python manage.py migrate
web: gunicorn djangoBlog.wsgi
worker: celery -A djangoBlog worker -l INFO