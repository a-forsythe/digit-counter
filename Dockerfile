FROM python:3.9.6-alpine

WORKDIR /app
COPY src/requirements.txt .
RUN pip install -r requirements.txt
COPY src/ .

ARG FAKE_SECRET
RUN python require_secret.py

EXPOSE 5000
ENV ENV=${ENV}
CMD python app.py
