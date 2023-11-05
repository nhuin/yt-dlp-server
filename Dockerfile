FROM ubuntu:22.04
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get install -y python3 python3-pip ffmpeg
COPY . .
RUN python3 -m pip install -r requirements.txt
CMD python3 server.py

