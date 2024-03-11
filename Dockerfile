FROM --platform=amd64 python:latest
RUN apt update && apt upgrade -y
RUN apt install -y git
RUN apt clean && rm -rf /var/lib/apt/lists/*