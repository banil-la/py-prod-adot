### Create requirements.txt

```
pip freeze > requirements.txt
```

### Run Local Server

```
uvicorn app.main:app --reload
```

### Build and run docker

```
docker build -t fastapi-clip .
docker run -p 8000:8000 fastapi-clip
```
