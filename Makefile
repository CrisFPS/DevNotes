.PHONY: install run test help

install:
	pip install -r requirements.txt

run:
	uvicorn backend.app.main:app --reload --port 8000

test:
	pytest -v

help:
	@echo Comandos disponiveis:
	@echo   make install  - Instala as dependencias
	@echo   make run      - Inicia o servidor em localhost:8000
	@echo   make test     - Executa os testes
