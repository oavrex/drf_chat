FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
	build-essential libpq-dev && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

copy . /app

RUN python manage.py migrate

RUN echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin','admin@admin.com','admin')" | python manage.py shell

EXPOSE 8000

CMD ['python', 'manage.py','runserver','0.0.0.0:8000']











