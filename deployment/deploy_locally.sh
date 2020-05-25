#!/usr/bin/env bash

# sudo ps -aux | grep gunicorn
# echo "Killing existing . . ."
# pkill gunicorn
# gunicorn --bind 0.0.0.0:5000 me_api:app --daemon --workers 5
# echo "Started!"

scp -v -r ../../me_api tmkasun@jetson.knnect.com:/home/tmkasun/projects/