FROM python:3.11
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["gunicorn", "weather_project.wsgi:application", "--bind", "0.0.0.0:8000"]