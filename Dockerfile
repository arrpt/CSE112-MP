#FROM --platform=amd64 gcc
#RUN apt update && apt upgrade -y
#RUN apt install -y git
#RUN apt clean && rm -rf /var/lib/apt/lists/*
FROM --platform=amd64 python:latest
RUN apt update && apt upgrade -y
RUN apt install -y git
RUN apt clean && rm -rf /var/lib/apt/lists/*