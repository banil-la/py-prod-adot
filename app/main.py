import os
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from google.cloud import vision
from google.oauth2 import service_account
from typing import List
from dotenv import load_dotenv

# 환경 변수 로드
load_dotenv()

# 서비스 계정 키 파일 경로 설정
SERVICE_ACCOUNT_FILE = os.getenv("SERVICE_ACCOUNT_FILE")
credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE)

# Vision API 클라이언트 초기화
client = vision.ImageAnnotatorClient(credentials=credentials)

# FastAPI 앱 초기화
app = FastAPI()

# CORS 설정
environment = os.getenv("ENVIRONMENT")
if environment == "local":
  origins = ["http://localhost:3000"]
else:  # production
  origins = ["https://dayneed.me"]

app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

# 이미지 분석 함수
def analyze_app_screen(content: bytes):
    image = vision.Image(content=content)

    # 1. 객체 감지 (UI 구성 요소 탐지)
    object_response = client.object_localization(image=image).localized_object_annotations
    objects = []
    for object_ in object_response:
        objects.append({
            "name": object_.name,  # 예: 'Button', 'Text', 'Icon'
            "confidence": object_.score,
            "bounding_poly": [(vertex.x, vertex.y) for vertex in object_.bounding_poly.normalized_vertices]
        })

    # 2. 텍스트 감지 (화면 내 텍스트 추출)
    text_response = client.text_detection(image=image)
    texts = []
    for text in text_response.text_annotations:
        texts.append({
            "text": text.description,
            "bounding_poly": [(vertex.x, vertex.y) for vertex in text.bounding_poly.vertices]
        })

    return {
        "objects": objects,
        "texts": texts
    }

# FastAPI 엔드포인트 설정
@app.post("/analyze-screen")
async def analyze_screen(file: UploadFile = File(...)):
    # 파일 내용을 읽어 분석 함수에 전달
    content = await file.read()
    result = analyze_app_screen(content)
    return result