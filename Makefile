.PHONY: build run clean shell
SRCS:=Dockerfile requirements/requirements.in app.py
IMAGE:=quaratine_api
PORT:=5000:5000
DARGS:=-it --rm -v $(CURDIR):/app

all: requirements.txt run

build: .build
.build: $(SRCS)
	docker build -t $(IMAGE) .
	echo > $@

run: build
	docker run $(DARGS) -p $(PORT) $(IMAGE)

shell: build
	docker run $(DARGS) --entrypoint /bin/bash $(IMAGE)

requirements.txt: build
	docker run -it --rm $(IMAGE) -m pip freeze > $@

clean:
	- rm .build
	- docker rmi $(IMAGE)
