
# [:octocat: Nginx / Gunicorn / Flask :snake: / Celery / SocketIO / MySQL / Redis / Docker :whale: sample application](https://github.com/alexOarga/docker-nginx-flask-celery-mysql-redis) 

[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)]() 

Basic [Docker Compose](https://docs.docker.com/compose/) template application for orchestating [Flask](https://flask.palletsprojects.com/en/2.0.x/) with a [Celery](https://docs.celeryproject.org/en/stable/) queue task, [Redis](https://redis.io/) message broker, [MySQL](https://www.mysql.com/) database and support for [SocketIO](https://socket.io/) protocol.

Deployed with [Nginx](https://nginx.org/en/) server and [Gunicorn](https://gunicorn.org/) WSGI.

[Flower](https://flower.readthedocs.io/en/latest/) supervision of Celery workers is also available. SocketIO is implemented through [Flask-SocketIO](https://flask-socketio.readthedocs.io/en/latest/).

Note that this application is almost production-ready. To see a production-ready application that follows this template check out [CONTRABASS-webservices](https://github.com/openCONTRABASS/CONTRABASS-webservice).

This template is intended for **asynchronous tasks**, **periodical tasks** and apps that require **asynchronous communication** through WebSockets-like protocols. 
Note that this makes an ideal backend for long-time execution web apps. 

Notice that this application is **horizontally scalable** as it allows replication through multiple nginx, gunicorn, and celery workers. 

## Requirements
- Python :snake: >= 3.6
- [Docker](https://docs.docker.com/engine/install/) :whale:
- [Docker compose](https://docs.docker.com/compose/install/) :whale:

## Run
First setup variables on ```.docker.env```.
Assuming you have [Docker](https://docs.docker.com/install/) and [docker-compose](https://docs.docker.com/compose/install/) installed, run on terminal:
```bash
docker-compose up
```

In order to bring it down run:
```bash
docker-compose down
```

Go too:
  - http://127.0.0.1/hello/MyApplicationExample
  
- Flower management page
  - http://127.0.0.1:5555




## Test

```
pytest -v
```

## Maintainers
[@alexOarga](https://github.com/alexOarga)

