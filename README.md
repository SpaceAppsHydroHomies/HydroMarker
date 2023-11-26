# HydroMarker
HydroMarker is a web application created in under 30 hours as part of the 2023 NASA SpaceApps Hackathon (What's Up With This Water Challenge). It utilizes open-source data to display the water quality and endangered species for all major waterways in the United States. It also provides environmental tips to conserve our waterways.

The frontend utilizes Vite and React and the backend utilizes Django and SQLite.
We used official data sources from the United States Geological Survey (USGS), Environmental Protection Agency (EPA), and databases from various non-profit organizations.

## 1. To Run The Django Backend API

```bash
python -m venv env
source env/bin/activate
pip install -r backend/requirements.txt
cd backend/water_api
python manage.py runserver
```

## 2. To Run The Webserver
```bash
npm install
npm run dev
```

## 3. To Run The Project as a Docker Container

```bash
docker build -t [image name] .
docker run -p 8000:8000 [image name]
```

After doing 1. and either 2. or 3.:
Open http://127.0.0.1:8000/ on a browser.
