#FROM python:3.12-slim
#WORKDIR /app
#COPY . /app/
#RUN pip install --upgrade pip \
 #   && pip install -r requirements.txt
#EXPOSE 8080
#CMD ["python", "bot.py"]
FROM python:3.12-slim

# Install git (required for pip to install from git+https URLs)
RUN apt-get update && apt-get install -y git \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . /app/

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

EXPOSE 8080
CMD ["python", "bot.py"]
