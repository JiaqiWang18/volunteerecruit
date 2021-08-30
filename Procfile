release: python manage.py migrate
web: gunicorn djangoBlog.wsgi
celery: celery -A djangoBlog worker -l INFO