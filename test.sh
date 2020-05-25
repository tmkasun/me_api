#!/usr/bin/env bash

exec /usr/local/bin/gunicorn --bind 0.0.0.0:5001 me_api:app --workers 5