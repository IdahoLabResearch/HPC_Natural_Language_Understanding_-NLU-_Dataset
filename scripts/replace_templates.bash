#!/bin/bash
FILES=$(find data/ -type f -name "*.template")
for file in $FILES; do
    mv $file ${file%.*}
done