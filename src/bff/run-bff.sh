#!/bin/bash
DIR=$PWD

if [ -z $1 ]; then
    echo "No environment specified. Using Flask default (likely production). Pass 'development' as a parameter to run in development mode."
fi

JOB_DIFF_UI_SETTINGS=$DIR/bff.conf PYTHONDONTWRITEBYTECODE=1 FLASK_ENV=${1} FLASK_APP=app.py flask run --host=0.0.0.0

