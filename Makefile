.PHONY: dev

all: dev

dev:
	@echo "Starting dev server..."
	flask --app app_factory run --host=0.0.0.0