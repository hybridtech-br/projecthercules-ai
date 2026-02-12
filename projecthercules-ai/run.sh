#!/usr/bin/with-contenv bashio

echo "Starting Project Hercules AI..."

uvicorn main:app --host 0.0.0.0 --port 8099
