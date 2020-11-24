#!/usr/bin/env bash

# format code
black .

# gather requirements
pip freeze > requirements.txt

# sort requirements
sort -o requirements.txt requirements.txt

# commit with prompts
git add .
git status
git commit -m "$1"
git push origin master