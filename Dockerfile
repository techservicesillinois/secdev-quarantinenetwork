FROM python:3.8
WORKDIR /app
RUN apt-get update
COPY requirements.txt requirements-dev.txt /
RUN pip install -r /requirements.txt -r /requirements-dev.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
