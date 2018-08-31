FROM armhf/ubuntu

RUN apt-get update && apt-get install -y curl iputils-ping python-numpy python-pil python-setuptools python-dev build-essential python-pip  
WORKDIR /tmp

ADD ping.py /ping.py
ADD requirements.txt /requirements.txt

RUN pip install --upgrade pip
RUN pip install -r /requirements.txt

RUN rm -f /tmp/*.deb
RUN apt-get clean

WORKDIR /

ENTRYPOINT ["python"]
CMD ["/ping.py"]
