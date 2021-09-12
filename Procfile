release: python manage.py migrate
web: gunicorn djangoBlog.wsgi
worker: celery -A djangoBlog worker --without-heartbeat --without-gossip --without-mingle