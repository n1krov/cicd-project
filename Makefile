.PHONY: build test

IMAGE_NAME = cicd-project-test

build:
	docker build -t $(IMAGE_NAME) .

test: build
	docker run --rm $(IMAGE_NAME)
