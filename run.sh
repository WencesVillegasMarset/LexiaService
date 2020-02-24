#!/bin/bash
gunicorn --worker-class gevent  --bind 0.0.0.0:5000 wsgi:app &
rq worker &