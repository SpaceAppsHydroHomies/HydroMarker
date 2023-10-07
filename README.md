# changethislater



## To get the backend running
* python -m venv env
* source env/bin/activate
* pip install -r backend/requirements.txt
* cd backend
* uvicorn main:app --host 0.0.0.0 --port 8000 --reload
* open http://localhost:8000/ on a browser
