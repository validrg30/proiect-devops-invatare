# 1. Imaginea de baza (Python mic, versiunea 3.9)
FROM python:3.9-slim

# 2. Setam folderul de lucru
WORKDIR /app

# 3. Copiem DOAR lista de cerinte (pentru Cache eficient!)
COPY requirements.txt .

# 4. Instalam dependintele
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copiem restul codului
COPY . .

# 6. Deschidem portul 5000 (doar informativ pentru noi)
EXPOSE 5000

# 7. Comanda de start
CMD ["python", "app.py"]
