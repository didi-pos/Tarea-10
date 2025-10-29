FROM python:3.11-slim

LABEL maintainer="didierposse@gmail.com"

RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    make \
    libgl1 \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender1 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /carrito

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY carrito.py .

ENV DISPLAY=:0

CMD ["python", "carrito.py"]
