release: python manage.py makemigrations --no-input
release: python manage.py migrate --no-input
release: export DISPLAY=:0


web: gunicorn --pythonpath . optic.wsgi
