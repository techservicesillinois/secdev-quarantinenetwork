.PHONY: build run clean shell all
SRCS:=Dockerfile requirements.txt requirements-dev.txt app.py
IMAGE:=quaratine_api
PORT:=5000:5000
DARGS:=-it --rm -v $(CURDIR):/app
DOCKER_RUN?=docker run $(DARGS) -p $(PORT) $(IMAGE)

all: run

build: .build
.build: $(SRCS)
	docker build -t $(IMAGE) .
	echo > $@

run: build
	$(DOCKER_RUN)

test:
	$(DOCKER_RUN) -m flake8

shell: build
	docker run $(DARGS) --entrypoint /bin/bash $(IMAGE)

requirements.txt: requirements.in
	docker run -it --rm -v $(CURDIR):/usr/src --entrypoint bash python:3.8 -c 'pip install -qqqr /usr/src/requirements.in && pip freeze' > $@

requirements-dev.txt: requirements-dev.in
	docker run -it --rm -v $(CURDIR):/usr/src --entrypoint bash python:3.8 -c 'pip install -qqqr /usr/src/requirements-dev.in && pip freeze' > $@

deps:
	pip install -r requirements.txt
	pip install -r requirements-dev.txt

clean:
	- rm .build
	- docker rmi $(IMAGE)
