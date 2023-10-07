FROM python:3.10-slim-buster

WORKDIR /app

COPY backend/requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "backend/water_api/manage.py", "runserver", "0.0.0.0:8000"]