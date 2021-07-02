# digit-counter

This state-of-the-art web API will count the number of numeric digits `[0-9]` in whatever string you pass to it.

## Usage

- `GET /?s=hello12345` -> `{"count":5,"message":"I reckon I see 5 digits."}`

## Running the app

### Local testing

- `cd src`
- `python3 -m venv .venv`
- `source .venv/bin/activate`
- `pip install -r requirements.txt`
- `flask run`
- API will be running at http://127.0.0.1:5000

To run unit tests:

- `pytest tests`

### Docker

- `docker build -t digit-counter .`
- `docker run -p 5000:5000 digit=-counter`
- API will be running at http://127.0.0.1:5000

To run unit tests:

- `docker run -e ENV=test digit-counter`

### Docker Compose

- `docker-compose up --build`
- API will be running at http://127.0.0.1:5000

To run unit tests:

- `docker-compose -f docker-compose.yml -f docker-compose.test.yml up --build`
