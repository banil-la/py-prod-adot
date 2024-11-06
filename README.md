### Create requirements.txt

```
pip freeze > requirements.txt
```

#### RESET

```
pip uninstall -r requirements.txt -y
pip install -r requirements.txt
```

### Run Local Server

```
uvicorn app.main:app --reload
```

### Build & Deploy docker

```
docker buildx build --platform linux/amd64 -t gcr.io/py-prdo-adot/fastapi-vision-app --push .
gcloud run deploy fastapi-vision-app --image gcr.io/py-prdo-adot/fastapi-vision-app --platform managed --region asia-northeast1 --allow-unauthenticated
```
