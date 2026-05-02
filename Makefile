PYTHON ?= python
APP ?= backend.app.main:app
PORT ?= 8000

.PHONY: install run test format clean help

install:
	$(PYTHON) -m pip install -r requirements.txt

run:
	$(PYTHON) -m uvicorn $(APP) --reload --port $(PORT)

test:
	$(PYTHON) -m pytest -v

format:
	$(PYTHON) -m black backend tests

clean:
	$(PYTHON) -c "import pathlib, shutil; [shutil.rmtree(p, ignore_errors=True) for p in ['.pytest_cache', '.tmp_pytest', '.tmp_pytest_run']]; [shutil.rmtree(p, ignore_errors=True) for p in pathlib.Path('.').glob('.pytest_tmp*')]; [shutil.rmtree(p, ignore_errors=True) for p in pathlib.Path('.').glob('pytest-cache-files-*')]; [shutil.rmtree(p, ignore_errors=True) for p in pathlib.Path('.').rglob('__pycache__')]"

help:
	@echo Comandos disponiveis:
	@echo   make install  - Instala as dependencias
	@echo   make run      - Inicia o servidor em localhost:8000
	@echo   make test     - Executa os testes
	@echo   make format   - Formata o codigo Python com Black
	@echo   make clean    - Remove caches e arquivos temporarios
	@echo   PYTHON=...    - Opcional: define o interpretador Python usado pelo Makefile
