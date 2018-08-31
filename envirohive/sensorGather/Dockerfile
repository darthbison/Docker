FROM armhf/ubuntu

RUN apt-get update && apt-get install -y curl mosquitto mosquitto-clients python-numpy python-pil python-setuptools python-dev build-essential python-pip  
WORKDIR /tmp

ADD start.sh /start.sh
ADD gather.py /gather.py
ADD requirements.txt /requirements.txt

RUN pip install --upgrade pip
RUN pip install -r /requirements.txt

RUN rm -f /tmp/*.deb
RUN apt-get clean

WORKDIR /

EXPOSE 1883 9001

ENTRYPOINT ["/start.sh"]
