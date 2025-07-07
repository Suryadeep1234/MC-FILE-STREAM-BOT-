#FROM python:3.12-slim
#WORKDIR /app
#COPY . /app/
#RUN pip install --upgrade pip \
  #  && pip install -r requirements.txt
#EXPOSE 8080
#CMD ["python", "bot.py"]

FROM python:3.12-slim

# Install system dependencies for Pillow, tgcrypto, and git-based installs
RUN apt-get update && apt-get install -y \
    gcc \
    build-essential \
    git \
    libjpeg-dev \
    zlib1g-dev \
    libpng-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . /app/

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

EXPOSE 8080
CMD ["python", "bot.py"]
