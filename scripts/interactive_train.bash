#!/bin/bash
export SQLALCHEMY_SILENCE_UBER_WARNING=1
model=$(ls -Art models/ | tail -n 1)
rasa interactive --skip-visualization --model models/${model} 