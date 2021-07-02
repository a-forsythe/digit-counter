FROM python:3.9.6-alpine

WORKDIR /app
COPY src/requirements.txt .
RUN pip install -r requirements.txt
COPY src/ .

ENV FAKE_SECRET password123
RUN python require_secret.py

EXPOSE 5000
ENV ENV=${ENV}
CMD python app.py
