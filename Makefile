.PHONY: venv install test fast api behave ui

venv:
	python -m venv .venv

install:
	pip install -r requirements.txt

test:
	pytest -q

fast:
	pytest -m "not slow and not perf" -q

api:
	uvicorn src.server.main:app --reload --port 8000

behave:
	behave

ui:
	RUN_UI=1 pytest tests/ui/test_ui_smoke.py -q
