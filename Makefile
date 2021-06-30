default:
	@printf "$$HELP"

help:
	@printf "$$HELP"

build-xycrypt:
	docker build -t image_xycrypt .

run-xycrypt:
	docker run --rm -it --name container_xycrypt -v $(PWD)/datos:/opt/datos image_xycrypt

define HELP
Please execute "make <command>". Example: make help
Available commands
- make build-xycrypt
\t Build the xycrypt docker image.
- make run-xycrypt
\t Run the application into a docker container.

endef

export HELP