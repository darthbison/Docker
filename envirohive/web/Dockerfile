FROM python:3.6.5-jessie
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
