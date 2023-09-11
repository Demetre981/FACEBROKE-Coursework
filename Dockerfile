FROM python

WORKDIR /app

COPY . .

RUN apt update && \
    apt install nano && \
    pip install -r requirements.txt

EXPOSE 8000
