# Python 3.11-slim 이미지 사용
FROM python:3.11-slim

# 작업 디렉토리 설정
WORKDIR /app

# 필수 패키지 설치
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# 필요 라이브러리 설치
COPY requirements_locked.txt .
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements_locked.txt

# 애플리케이션 파일 복사
COPY . .

# 환경 변수 설정
ENV GOOGLE_APPLICATION_CREDENTIALS="/py-prdo-adot-e205b1126ce8.json"

# 포트 노출
EXPOSE 8080

# 애플리케이션 실행 명령어
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]