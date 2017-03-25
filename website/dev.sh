#!/bin/bash
EVENTAPP_ENV="eventapp-env"

if [ ! -d "$EVENTAPP_ENV" ]; then
    virtualenv $EVENTAPP_ENV
    source $EVENTAPP_ENV/bin/activate
    pip install -r requirements.txt
else
    source $EVENTAPP_ENV/bin/activate
fi