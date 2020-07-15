.PHONY: all run shell test build clean force-clean upgrade integration-test

all: run

run: build
	docker-compose up

build: .build
.build: requirements.txt requirements-dev.txt Dockerfile
	docker-compose build
	echo > $@

shell: build
	docker-compose run api bash

test: build
	docker-compose run api bash -c 'flake8 && mypy .'

integration-test: build
	docker run -it --network host --rm -v $(CURDIR)/test/integration:/usr/src postman/newman run '/usr/src/quarantine_network_api.postman_collection.json' -e '/usr/src/quarantine_network_dev.postman_environment.json'

clean: 
	- rm .build
	- del .build
	- docker-compose down --rmi all

force-clean: clean
	-rm requirements.txt
	-del requirements.txt
	-rm requirements-dev.txt 
	-del requirements-dev.txt 

upgrade: force-clean requirements.txt requirements-dev.txt

requirements.txt: requirements.in
	docker run -it --rm -v $(CURDIR):/usr/src --entrypoint bash python:3.8 -c "pip install -qqqr /usr/src/requirements.in && pip freeze" > $@

requirements-dev.txt: requirements-dev.in
	docker run -it --rm -v $(CURDIR):/usr/src --entrypoint bash python:3.8 -c "pip install -qqqr /usr/src/requirements-dev.in && pip freeze" > $@

