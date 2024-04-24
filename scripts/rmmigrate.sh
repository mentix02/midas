#!/usr/bin/env bash

# deletes all migrations files and __pycache__ directories
# ONLY RUN THIS SCRIPT IF YOU KNOW WHAT YOU ARE DOING
# THAT TOO ONLY DURING DEVELOPMENT - NEVER IN PRODUCTION

find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete
find . -path "*/migrations/__pycache__" -delete
