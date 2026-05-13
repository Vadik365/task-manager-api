FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN python manage.py collectstatic --noinput || true
CMD ["sh", "-c", "sleep 5 && python manage.py migrate && python manage.py shell -c \"from django.contrib.auth.models import User; User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', '', 'admin123')\" && gunicorn config.wsgi:application --bind 0.0.0.0:8000 --workers 1 --log-level debug --error-logfile - --access-logfile -"]