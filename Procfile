release: python manage.py migrate
web: gunicorn abigail.wsgi --bind=0.0.0.0:$PORT
