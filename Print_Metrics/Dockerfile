# based on python3 debian image
FROM python:3-slim

# install gcc and psutil module
RUN apt-get -y update && apt-get install -y gcc
RUN pip3 install psutil
RUN mkdir /app
#COPY metrics.py /app
ENTRYPOINT ["python3", "/app/metrics.py"]
