### 새로 가상환경 생성 및 활성화

python -m venv venv
source venv/bin/activate # Windows는 venv\Scripts\activate

### 수정한 requirements.txt 설치

pip install -r requirements.txt

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
