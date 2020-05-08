FROM python:3.8
WORKDIR /app
RUN apt-get update
COPY ./requirements /opt/requirements
RUN pip install -r /opt/requirements/requirements.in
ENTRYPOINT ["python"]
CMD ["app.py"]
