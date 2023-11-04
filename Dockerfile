FROM ubuntu:20.04
RUN apt-get update && apt-get install -y python3 python3-pip
COPY . .
RUN python3 -m pip install -r requirements.txt
CMD python3 server.py

