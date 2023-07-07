#!/bin/bash
export SQLALCHEMY_SILENCE_UBER_WARNING=1
rasa data validate --domain data --data data --quiet
