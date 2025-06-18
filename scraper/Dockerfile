# Resmi Playwright Python imajı; içinde tüm bağımlılıklar var
FROM mcr.microsoft.com/playwright/python:latest

WORKDIR /app

# Yalnızca projenin ihtiyaç duyduğu pip paketlerini yükle
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Uygulama kodunu kopyala
COPY . .

# Scraper'ı çalıştır
CMD ["python", "scrape.py"]
