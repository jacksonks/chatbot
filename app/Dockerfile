FROM python:3.6

RUN mkdir -p /opt/chatbot/app/src
COPY . /opt/chatbot/app/src
WORKDIR /opt/chatbot/app/src
RUN pip install -r requirements.txt
EXPOSE 5002

# run server
CMD ["python","app.py"]
