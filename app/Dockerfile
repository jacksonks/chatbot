FROM python:3.6

# Make working directory
RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app

RUN pip install -r requirements.txt

# Copy project to docker work directory
ADD . /app

EXPOSE 5002

ENTRYPOINT ["sh", "start.sh"]

#CMD ["gunicorn", "-b", "0.0.0.0:5002", "app:app"]

#CMD ["python", "app.py"]
# run server
#CMD ["gunicorn", "-b", "0.0.0.0:5002", "app:application"]
