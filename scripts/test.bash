#!/bin/bash
export SQLALCHEMY_SILENCE_UBER_WARNING=1
rasa test --domain data --quiet