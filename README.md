# Run on a host operating system
Prerequisites:
- Python 3

1) Create python venv
- python3 -m venv ./venv
- source venv/bin/activate
- pip install -r requirements.txt

2) Initialize database
- python manage.py makemigrations server
- python manage.py migrate

3) create super user
- python manage.py createsuperuser

4) Run application
- python manage.py runserver

# Run using Docker
Prerequisites:
- Docker, docker-compose

2) Initialize database
- docker-compose run server python manage.py makemigrations server
- docker-compose run server python manage.py migrate

3) create super user
- docker-compose run server python manage.py createsuperuser

4) Run application
- docker-compose up

# Run using Podman
TBD

# Using application
- Application is running on http://127.0.0.1:8000/api/v1/
- Api can be explored using html view
- To post data, you have to be logged in using super user details
- requests support pagination of size 10

## Examples
Examples use curl, but any tool/framework can be used for standard http requests

- Post new sensors measurements (login credentials have to provided to post data) - http://127.0.0.1:8000/api/v1/data/:
```bash
curl -H "Accept: application/json" -H "Content-Type: application/json" -X POST -u USER_NAME:USER_PASSWORD -d ' { 
    "sensor1": {
        "voltage": 30,
        "current": 30,
        "power": 30,
        "energy": 30,
        "charge_cycles": 30,
        "temperature": 30,
        "status": 1,
        "error": 0
    },
    "sensor2": {
        "voltage": 40,
        "current": 40,
        "power": 40,
        "energy": 40,
        "charge_cycles": 40,
        "temperature": 40,
        "status": 1,
        "error": 0
    }
}' http://127.0.0.1:8000/api/v1/data/
```

- Get data from all sensor measurements - http://127.0.0.1:8000/api/v1/data/:
```bash
curl -i -H "Accept: application/json" -H "Content-Type: application/json" -X GET http://127.0.0.1:8000/api/v1/data/
```

Response:
```bash
HTTP/1.1 200 OK
Date: Sun, 06 Jun 2021 12:02:14 GMT
Server: WSGIServer/0.2 CPython/3.9.5
Content-Type: application/json
Vary: Accept, Cookie
Allow: GET, POST, HEAD, OPTIONS
X-Frame-Options: DENY
Content-Length: 553
X-Content-Type-Options: nosniff
Referrer-Policy: same-origin

{"count":1,"next":null,"previous":null,"results":[{"url":"http://127.0.0.1:8000/api/v1/data/1/","id":1,"sensor1":{"url":"http://127.0.0.1:8000/api/v1/sensor1/1/","id":1,"voltage":30.0,"current":30.0,"power":30.0,"energy":30.0,"charge_cycles":30.0,"temperature":30.0,"status":30,"error":50,"time":"2021-06-06T12:00:08.071676Z"},"sensor2":{"url":"http://127.0.0.1:8000/api/v1/sensor2/1/","id":1,"voltage":40.0,"current":40.0,"power":40.0,"energy":40.0,"charge_cycles":40.0,"temperature":40.0,"status":40,"error":50,"time":"2021-06-06T12:00:08.136530Z"}}]}
```

- Get Sensor1 measurement 1 - http://127.0.0.1:8000/api/v1/sensor1/1/:
```bash
curl -i -H "Accept: application/json" -H "Content-Type: application/json" -X GET http://127.0.0.1:8000/api/v1/sensor1/1/
```