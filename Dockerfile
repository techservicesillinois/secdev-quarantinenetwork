FROM python:3.8 as base
WORKDIR /app
ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0
COPY requirements.txt /
RUN pip install -r /requirements.txt
CMD ["flask", "run"]

FROM base as dev
COPY requirements-dev.txt /
RUN pip install -r /requirements-dev.txt

FROM base
USER nobody