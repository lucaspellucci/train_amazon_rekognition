DOCKER_IID_FILE := .id

# $(CURDIR) is built-in variable
WORK_DIR ?= $(CURDIR)/work
IMG_DIR ?= $(CURDIR)/img


RUN_OPT ?= help

# To build IID file (Write the image ID to the file) / @a is the filename of the target (.id):
build: $(DOCKER_IID_FILE)
$(DOCKER_IID_FILE):
	docker build --iidfile=$@ .

rebuild:
	-rm .id
	docker build --iidfile=$(DOCKER_IID_FILE) .

run: $(DOCKER_IID_FILE)
	-docker run -ti --rm -v "$(WORK_DIR)":/work -v "$(IMG_DIR)":/img -e AWS_ACCESS_KEY_ID -e AWS_SECRET_ACCESS_KEY -e AWS_DEFAULT_REGION $(shell cat $<) $(RUN_OPT)
clean:
#	-rm -f any-other-artifacts

.PHONY: build rebuild clean
