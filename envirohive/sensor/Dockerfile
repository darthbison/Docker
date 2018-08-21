FROM armhf/ubuntu

RUN apt-get update && apt-get install -y curl python-numpy python-pil python-setuptools python-dev build-essential python-pip  
WORKDIR /tmp

RUN curl -LO  https://archive.raspberrypi.org/debian/pool/main/r/rtimulib/librtimulib-dev_7.2.1-3_armhf.deb \
 && curl -LO https://archive.raspberrypi.org/debian/pool/main/r/rtimulib//librtimulib-utils_7.2.1-3_armhf.deb \
 && curl -LO https://archive.raspberrypi.org/debian/pool/main/r/rtimulib/librtimulib7_7.2.1-3_armhf.deb \
 && curl -LO https://archive.raspberrypi.org/debian/pool/main/r/rtimulib/python-rtimulib_7.2.1-3_armhf.deb \
 && curl -LO https://archive.raspberrypi.org/debian/pool/main/p/python-sense-hat/python-sense-hat_2.1.0-1_armhf.deb
 
RUN dpkg -i librtimulib-dev_7.2.1-3_armhf.deb librtimulib-utils_7.2.1-3_armhf.deb librtimulib7_7.2.1-3_armhf.deb python-rtimulib_7.2.1-3_armhf.deb python-sense-hat_2.1.0-1_armhf.deb

ADD telemetry.py /telemetry.py
ADD telemetryRedis.py /telemetryRedis.py
ADD temperature.py /temperature.py
ADD testRedis.py /testRedis.py
ADD humidity.py /humidity.py
ADD requirements.txt /requirements.txt

RUN pip install --upgrade pip
RUN pip install -r /requirements.txt

RUN rm -f /tmp/*.deb
RUN apt-get clean

WORKDIR /

ENTRYPOINT ["python"]
CMD ["/telemetryRedis.py"]
