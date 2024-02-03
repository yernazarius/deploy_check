#!/bin/bash

cd backend


if [[ "${1}" == "celery" ]]; then
  celery -A task.email_service:celery worker -l INFO
elif [[ "${1}" == "flower" ]]; then
  celery -A task.email_service:celery flower
 fi