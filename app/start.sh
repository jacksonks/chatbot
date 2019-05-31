#!/bin/bash
/usr/local/bin/gunicorn --bind=0.0.0.0:5002 --log-level=DEBUG --workers=2 --timeout=6000 app:app
