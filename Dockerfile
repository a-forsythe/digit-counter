FROM python:3.9.6-alpine
WORKDIR /app
COPY src/requirements.txt .
RUN pip install -r requirements.txt
COPY src/ .
EXPOSE 5000
CMD flask run --host 0.0.0.0
