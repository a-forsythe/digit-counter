FROM python:3.9.6-alpine

WORKDIR /app
COPY src/requirements.txt .
RUN pip install -r requirements.txt
COPY src/ .

RUN --mount=type=secret,id=fake FAKE_SECRET="${FAKE_SECRET:-$(cat /run/secrets/fake)}" python require_secret.py

EXPOSE 5000
ENV ENV=${ENV}
CMD python app.py
