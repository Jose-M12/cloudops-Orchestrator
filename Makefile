PY=python3
PIP=pip
APP=app.main:app

.PHONY: setup fmt lint test run migrate upgrade docker-build

setup:
	$(PIP) install -r requirements/dev.txt
	pre-commit install

fmt:
	ruff check --fix .
	black .

lint:
	ruff check .
	mypy app tests

test:
	pytest --cov=app --cov-report=term-missing

run:
	uvicorn $(APP) --host 0.0.0.0 --port 8080 --reload

migrate:
	alembic revision --autogenerate -m "$(m)"

upgrade:
	alembic upgrade head

docker-build:
	docker build -t cloudops-orchestrator:dev .
