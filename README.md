# changethislater

## To get the backend running

```bash
python -m venv env
source env/bin/activate
pip install -r backend/requirements.txt
cd backend/water_api
python manage.py runserver
```



## To run on a docker container

```bash
docker build -t [image name] .
docker run -p 8000:8000 [image name]
```

After doing either of these:

open http://127.0.0.1:8000/ on a browser