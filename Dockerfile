FROM python:3.9.6-alpine
WORKDIR /app
COPY src/requirements.txt .
RUN pip install -r requirements.txt
COPY src/ .
EXPOSE 5000
ENV ENV=${ENV}
CMD python app.py
