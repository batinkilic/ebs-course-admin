# Resmi Playwright Python imajı; içinde tüm bağımlılıklar var
FROM mcr.microsoft.com/playwright/python:v1.52.0-jammy

WORKDIR /app

# Yalnızca projenin ihtiyaç duyduğu pip paketlerini yükle
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Uygulama kodunu kopyala
COPY . .

# Scraper'ı çalıştır
CMD ["python", "scrape.py"]
