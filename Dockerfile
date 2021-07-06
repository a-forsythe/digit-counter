FROM python:3.9.6-slim

RUN apt-get update && apt-get install -y cowsay
ENV PATH "/usr/games:${PATH}"

WORKDIR /app
COPY src/requirements.txt .
RUN pip install -r requirements.txt
COPY src/ .

ARG FAKE_SECRET
RUN --mount=type=secret,id=fake FAKE_SECRET="${FAKE_SECRET:-$(cat /run/secrets/fake)}" \
	python require_secret.py

EXPOSE 5000
ENV ENV=${ENV}
CMD python app.py
