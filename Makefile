
.PHONY: help gen_proto reinstall test format lint

help:
	@echo "Please use 'make <target>' where <target> is one of"
	@echo ""
	@echo "  gen_proto    to generate protobuf files"
	@echo "  reinstall    to reinstall the package"
	@echo "  test         to run tests"
	@echo "  format       to run black"
	@echo "  lint         to run ruff"
	@echo ""

gen_proto:
	python -m grpc_tools.protoc \
		-I./libpg_query/protobuf \
		--python_out=pyi_out:./src/psqlparse2/pb \
		libpg_query/protobuf/*.proto

reinstall:
	python -m pip install --upgrade --force-reinstall -v '.[dev]'

test:
	python -m pytest -s -vv tests

format:
	black src/

lint:
	ruff check src/
