#!/bin/bash
export SQLALCHEMY_SILENCE_UBER_WARNING=1
rasa train --quiet --force --config config.yml \
    --domain data \
    --data data